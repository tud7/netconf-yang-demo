from ncclient import manager

mgr = manager.connect(host='sandbox-iosxe-latest-1.cisco.com',
                    port=830,
                    username='developer',
                    password='C1sco12345',
                    hostkey_verify=False,
                    device_params={'name':'csr'})

CONFIGURATION  = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>tmd12345</hostname>
    </native>
</config>
"""

data = mgr.edit_config(config=CONFIGURATION, target='running')
print(data)

mgr.close_session()
