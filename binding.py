# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.yangtypes import YANGBinary
from pyangbind.lib.yangtypes import YANGBitsType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal

import builtins as __builtin__
long = int
class yc_port_vlan_config__vlan_provisioning_switch_vlan_port(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module vlan-config - based on the path /vlan-provisioning/switch/vlan/port. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of ports in this VLAN
  """
  __slots__ = ('_path_helper', '_extmethods', '__port_id',)

  _yang_name = 'port'
  _yang_namespace = 'urn:group4:vlan-config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__port_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='uint32', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['vlan-provisioning', 'switch', 'vlan', 'port']

  def _get_port_id(self):
    """
    Getter method for port_id, mapped from YANG variable /vlan_provisioning/switch/vlan/port/port_id (uint32)

    YANG Description: Port number associated with this VLAN
    """
    return self.__port_id
      
  def _set_port_id(self, v, load=False):
    """
    Setter method for port_id, mapped from YANG variable /vlan_provisioning/switch/vlan/port/port_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_id() directly.

    YANG Description: Port number associated with this VLAN
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='uint32', is_config=True)""",
        })

    self.__port_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_id(self):
    self.__port_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="port-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='uint32', is_config=True)

  port_id = __builtin__.property(_get_port_id, _set_port_id)


  _pyangbind_elements = OrderedDict([('port_id', port_id), ])


class yc_vlan_vlan_config__vlan_provisioning_switch_vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module vlan-config - based on the path /vlan-provisioning/switch/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A list of VLAN configurations on the switch
  """
  __slots__ = ('_path_helper', '_extmethods', '__vlan_id','__port',)

  _yang_name = 'vlan'
  _yang_namespace = 'urn:group4:vlan-config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='uint16', is_config=True)
    self.__port = YANGDynClass(base=YANGListType("port_id",yc_port_vlan_config__vlan_provisioning_switch_vlan_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-id', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['vlan-provisioning', 'switch', 'vlan']

  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /vlan_provisioning/switch/vlan/vlan_id (uint16)

    YANG Description: The VLAN ID (1-4094)
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /vlan_provisioning/switch/vlan/vlan_id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: The VLAN ID (1-4094)
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='uint16', is_config=True)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='uint16', is_config=True)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /vlan_provisioning/switch/vlan/port (list)

    YANG Description: List of ports in this VLAN
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /vlan_provisioning/switch/vlan/port (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: List of ports in this VLAN
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("port_id",yc_port_vlan_config__vlan_provisioning_switch_vlan_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-id', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("port_id",yc_port_vlan_config__vlan_provisioning_switch_vlan_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-id', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=YANGListType("port_id",yc_port_vlan_config__vlan_provisioning_switch_vlan_port, yang_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-id', extensions=None), is_container='list', yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)

  vlan_id = __builtin__.property(_get_vlan_id, _set_vlan_id)
  port = __builtin__.property(_get_port, _set_port)


  _pyangbind_elements = OrderedDict([('vlan_id', vlan_id), ('port', port), ])


class yc_switch_vlan_config__vlan_provisioning_switch(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module vlan-config - based on the path /vlan-provisioning/switch. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A list of switches with VLAN configurations
  """
  __slots__ = ('_path_helper', '_extmethods', '__switch_id','__vlan',)

  _yang_name = 'switch'
  _yang_namespace = 'urn:group4:vlan-config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__switch_id = YANGDynClass(base=str, is_leaf=True, yang_name="switch-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='string', is_config=True)
    self.__vlan = YANGDynClass(base=YANGListType("vlan_id",yc_vlan_vlan_config__vlan_provisioning_switch_vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['vlan-provisioning', 'switch']

  def _get_switch_id(self):
    """
    Getter method for switch_id, mapped from YANG variable /vlan_provisioning/switch/switch_id (string)

    YANG Description: Unique ID for the switch (e.g., openflow:1)
    """
    return self.__switch_id
      
  def _set_switch_id(self, v, load=False):
    """
    Setter method for switch_id, mapped from YANG variable /vlan_provisioning/switch/switch_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_switch_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_switch_id() directly.

    YANG Description: Unique ID for the switch (e.g., openflow:1)
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=str, is_leaf=True, yang_name="switch-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """switch_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=str, is_leaf=True, yang_name="switch-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='string', is_config=True)""",
        })

    self.__switch_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_switch_id(self):
    self.__switch_id = YANGDynClass(base=str, is_leaf=True, yang_name="switch-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='string', is_config=True)


  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /vlan_provisioning/switch/vlan (list)

    YANG Description: A list of VLAN configurations on the switch
    """
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /vlan_provisioning/switch/vlan (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.

    YANG Description: A list of VLAN configurations on the switch
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_id",yc_vlan_vlan_config__vlan_provisioning_switch_vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_id",yc_vlan_vlan_config__vlan_provisioning_switch_vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(base=YANGListType("vlan_id",yc_vlan_vlan_config__vlan_provisioning_switch_vlan, yang_name="vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions=None), is_container='list', yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)

  switch_id = __builtin__.property(_get_switch_id, _set_switch_id)
  vlan = __builtin__.property(_get_vlan, _set_vlan)


  _pyangbind_elements = OrderedDict([('switch_id', switch_id), ('vlan', vlan), ])


class yc_vlan_provisioning_vlan_config__vlan_provisioning(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module vlan-config - based on the path /vlan-provisioning. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: VLAN provisioning configuration container
  """
  __slots__ = ('_path_helper', '_extmethods', '__switch',)

  _yang_name = 'vlan-provisioning'
  _yang_namespace = 'urn:group4:vlan-config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__switch = YANGDynClass(base=YANGListType("switch_id",yc_switch_vlan_config__vlan_provisioning_switch, yang_name="switch", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='switch-id', extensions=None), is_container='list', yang_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['vlan-provisioning']

  def _get_switch(self):
    """
    Getter method for switch, mapped from YANG variable /vlan_provisioning/switch (list)

    YANG Description: A list of switches with VLAN configurations
    """
    return self.__switch
      
  def _set_switch(self, v, load=False):
    """
    Setter method for switch, mapped from YANG variable /vlan_provisioning/switch (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_switch is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_switch() directly.

    YANG Description: A list of switches with VLAN configurations
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("switch_id",yc_switch_vlan_config__vlan_provisioning_switch, yang_name="switch", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='switch-id', extensions=None), is_container='list', yang_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """switch must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("switch_id",yc_switch_vlan_config__vlan_provisioning_switch, yang_name="switch", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='switch-id', extensions=None), is_container='list', yang_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)""",
        })

    self.__switch = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_switch(self):
    self.__switch = YANGDynClass(base=YANGListType("switch_id",yc_switch_vlan_config__vlan_provisioning_switch, yang_name="switch", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='switch-id', extensions=None), is_container='list', yang_name="switch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='list', is_config=True)

  switch = __builtin__.property(_get_switch, _set_switch)


  _pyangbind_elements = OrderedDict([('switch', switch), ])


class vlan_config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module vlan-config - based on the path /vlan-config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: YANG model for VLAN configuration
  """
  __slots__ = ('_path_helper', '_extmethods', '__vlan_provisioning',)

  _yang_name = 'vlan-config'
  _yang_namespace = 'urn:group4:vlan-config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan_provisioning = YANGDynClass(base=yc_vlan_provisioning_vlan_config__vlan_provisioning, is_container='container', yang_name="vlan-provisioning", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return []

  def _get_vlan_provisioning(self):
    """
    Getter method for vlan_provisioning, mapped from YANG variable /vlan_provisioning (container)

    YANG Description: VLAN provisioning configuration container
    """
    return self.__vlan_provisioning
      
  def _set_vlan_provisioning(self, v, load=False):
    """
    Setter method for vlan_provisioning, mapped from YANG variable /vlan_provisioning (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_provisioning is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_provisioning() directly.

    YANG Description: VLAN provisioning configuration container
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_vlan_provisioning_vlan_config__vlan_provisioning, is_container='container', yang_name="vlan-provisioning", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_provisioning must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_vlan_provisioning_vlan_config__vlan_provisioning, is_container='container', yang_name="vlan-provisioning", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='container', is_config=True)""",
        })

    self.__vlan_provisioning = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_provisioning(self):
    self.__vlan_provisioning = YANGDynClass(base=yc_vlan_provisioning_vlan_config__vlan_provisioning, is_container='container', yang_name="vlan-provisioning", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:group4:vlan-config', defining_module='vlan-config', yang_type='container', is_config=True)

  vlan_provisioning = __builtin__.property(_get_vlan_provisioning, _set_vlan_provisioning)


  _pyangbind_elements = OrderedDict([('vlan_provisioning', vlan_provisioning), ])


