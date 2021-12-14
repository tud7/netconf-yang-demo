from ncclient import manager

mgr = manager.connect(host='sandbox-iosxe-latest-1.cisco.com',
                    port=830,
                    username='developer',
                    password='C1sco12345',
                    hostkey_verify=False,
                    device_params={'name':'csr'})

# Filter hostname
FILTER = """
<native 
    xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname></hostname>
</native>
"""

config = mgr.get_config('running', filter=("subtree", FILTER))
print(config)

mgr.close_session()
