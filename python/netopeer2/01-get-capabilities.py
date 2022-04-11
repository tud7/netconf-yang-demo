from ncclient import manager

mgr = manager.connect(host='localhost',
                    port=1831,
                    username='root',
                    password='root',
                    hostkey_verify=False)

for capability in mgr.server_capabilities:
    print (capability)

mgr.close_session()
