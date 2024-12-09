import time
import requests
import json

BASE_URL = "http://localhost:8181/restconf"
AUTH = ("admin", "admin")


def get_hosts_from_topology():
    """Fetch host-like nodes from the OpenDaylight network-topology."""
    url = f"{BASE_URL}/operational/network-topology:network-topology"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, auth=AUTH, headers=headers)
        if response.status_code == 200:
            topology_data = response.json()
            hosts = []

            for topology in topology_data.get("network-topology", {}).get("topology", []):
                for node in topology.get("node", []):
                    if "termination-point" in node:
                        for termination in node.get("termination-point", []):
                            host_info = {
                                "id": node.get("node-id"),
                                "attachment-point": termination.get("tp-id"),
                            }
                            hosts.append(host_info)

            return hosts
        else:
            print(f"Failed to fetch hosts. Status: {response.status_code}, Error: {response.text}")
            return []
    except Exception as e:
        print(f"Error while fetching hosts: {e}")
        return []


def create_flow(switch_id, flow_id, match, actions, priority=100):
    url = f"{BASE_URL}/config/opendaylight-inventory:nodes/node/{switch_id}/table/0/flow/{flow_id}"

    # Flow definition
    flow = {
        "flow": {
            "id": str(flow_id),
            "priority": priority,
            "match": match,
            "instructions": {
                "instruction": [
                    {
                        "order": 0,
                        "apply-actions": {
                            "action": actions
                        }
                    }
                ]
            }
        }
    }

    # Send the RESTCONF request
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.put(url, auth=AUTH, headers=headers, data=json.dumps(flow))

    # Check response
    if response.status_code in [200, 201]:
        print(f"Flow {flow_id} successfully added to {switch_id}.")
    else:
        print(f"Failed to add flow {flow_id} to {switch_id}. Status: {response.status_code}, Error: {response.text}")


def configure_vlan(switch_id, vlan_id, in_port, out_ports):
    # Rule 1: Tag ingress traffic with VLAN ID
    create_flow(
        switch_id=switch_id,
        flow_id=f"ingress-{in_port}",
        match={"in-port": str(in_port)},
        actions=[
            {"order": 0, "push-vlan-action": {"ethernet-type": 33024}},
            {"order": 1, "set-field": {"vlan-match": {"vlan-id": {"vlan-id": vlan_id, "vlan-id-present": True}}}}
        ],
    )

    # Rule 2: Forward traffic with VLAN tag to correct ports
    for out_port in out_ports:
        create_flow(
            switch_id=switch_id,
            flow_id=f"forward-{vlan_id}-{out_port}",
            match={"vlan-match": {"vlan-id": {"vlan-id": vlan_id, "vlan-id-present": True}}},
            actions=[
                {"order": 0, "pop-vlan-action": {}},
                {"order": 1, "output-action": {"output-node-connector": str(out_port)}}
            ],
        )

    # Rule 3: Drop traffic with mismatched VLAN
    create_flow(
        switch_id=switch_id,
        flow_id=f"drop-{vlan_id}",
        match={"vlan-match": {"vlan-id": {"vlan-id": vlan_id, "vlan-id-present": False}}},
        actions=[],  # No actions = drop
        priority=50
    )


def resolve_ports_and_switch(attachment_point):
    """Resolve switch ID and in/out ports from the attachment point."""
    # Example format: "openflow:1:2" -> switch_id: openflow:1, in_port: 2
    parts = attachment_point.split(":")
    switch_id = ":".join(parts[:-1])  # Everything before the last part
    in_port = int(parts[-1])  # Last part is the port number
    return switch_id, in_port


hosts = get_hosts_from_topology()
vlan_ids = [10, 20]
host_vlan_map = {}  # Keep track of which host is on which VLAN


# Initial provisioning
def assign_vlans():
    for idx, host in enumerate(hosts):
        if host["attachment-point"].split(":")[-1] == 'LOCAL':
            continue
        vlan_id = vlan_ids[idx % len(vlan_ids)]  # Alternate VLAN assignment
        switch_id, in_port = resolve_ports_and_switch(host["attachment-point"])
        out_ports = [p for p in range(1, 5) if p != in_port]  # Example: Ports 1-4 minus in_port
        configure_vlan(switch_id, vlan_id, in_port, out_ports)
        host_vlan_map[host["id"]] = vlan_id


assign_vlans()


while True:
    try:
        new_hosts = get_hosts_from_topology()
        # Find newly added hosts
        new_host_ids = set(h["id"] for h in new_hosts) - set(host_vlan_map.keys())

        if new_host_ids:
            print(f"New hosts detected: {new_host_ids}")
            for host_id in new_host_ids:
                host = next(h for h in new_hosts if h["id"] == host_id)
                if host["attachment-point"].split(":")[-1] == 'LOCAL':
                    continue
                vlan_id = vlan_ids[len(host_vlan_map) % len(vlan_ids)]  # Alternate VLAN assignment
                switch_id, in_port = resolve_ports_and_switch(host["attachment-point"])
                out_ports = [p for p in range(1, 5) if p != in_port]  # Adjust based on topology
                configure_vlan(switch_id, vlan_id, in_port, out_ports)
                host_vlan_map[host_id] = vlan_id
        else:
            print("No new hosts detected.")

        # Update the hosts list
        hosts = new_hosts

        time.sleep(1)  # Avoid busy waiting
    except KeyboardInterrupt:
        print("Exiting...")
        break