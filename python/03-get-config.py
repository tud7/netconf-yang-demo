from ncclient import manager

mgr = manager.connect(host='sandbox-iosxe-latest-1.cisco.com',
                    port=830,
                    username='developer',
                    password='C1sco12345',
                    hostkey_verify=False,
                    device_params={'name':'csr'})


config = mgr.get_config('running')
print(config)

mgr.close_session()
