from ncclient import manager

mgr = manager.connect(host='sandbox-iosxe-latest-1.cisco.com',
                    port=830,
                    username='developer',
                    password='C1sco12345',
                    hostkey_verify=False,
                    device_params={'name':'csr'})

for RTR_Capability in mgr.server_capabilities:
    print (RTR_Capability)

mgr.close_session()
