from ncclient import manager

mgr = manager.connect(host='localhost',
                    port=1831,
                    username='root',
                    password='root',
                    hostkey_verify=False)


schema = mgr.get_schema('ietf-netconf-monitoring')
print(schema)

mgr.close_session()
