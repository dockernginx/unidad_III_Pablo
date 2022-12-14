import xml.dom.minidom

from ncclient import manager

m=manager.connect(
    host="10.10.20.48", 
    port=830,
    username="developer",
    password="C1sco12345", 
    hostkey_verify=False
)

netconf_data = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>NEWHOSTNAME</hostname>
  </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get_config(source="running", filter=netconf_filter)
print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )