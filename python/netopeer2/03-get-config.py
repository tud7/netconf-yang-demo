from ncclient import manager

mgr = manager.connect(host='localhost',
                    port=1831,
                    username='root',
                    password='root',
                    hostkey_verify=False)


config = mgr.get_config('running').data_xml
print(config)

mgr.close_session()
