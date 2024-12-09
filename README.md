# Term Project for Data Modelling for Intelligent Networks

This term project focuses on creation and allocation of VLANs using OpenDaylight and RESTCONF

By automating the creation of VLANs and allocation of devices to VLANs, we can save time and avoid errors that could happen by misjudgement or typos.
The devices could be added to VLANs based on different criteria such as location, MAC address, connection type or Round Robin

An example python program has been provided on how the implemenetation could work.
The example expects a locally running opendaylight controller, but the IP can be changed in the file.
The provided example chooses a round-robin approach to the VLAN allocation, which means the first device is allocated to VLAN 10 and then the next to VLAN 20, and then goes to VLAN 10 again

This is a very simple implementation, but there can also be more advanced versions which could create new VLANs when an appropriate one is not available. 
Or there could be a limit to the device amount in a VLAN, where the system would then have to create a new VLAN for the newly connected device.
There is a provided example using YANG data models to configure the VLAN. However, at the time of writing it is not incorporated in OpenDaylight and therefore does not work.

The PDF of the report can also be seen in this git repo.
