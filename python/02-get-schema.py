from ncclient import manager

mgr = manager.connect(host='sandbox-iosxe-latest-1.cisco.com',
                    port=830,
                    username='developer',
                    password='C1sco12345',
                    hostkey_verify=False,
                    device_params={'name':'csr'})


schema = mgr.get_schema('Cisco-IOS-XE-native')
print(schema)

mgr.close_session()
