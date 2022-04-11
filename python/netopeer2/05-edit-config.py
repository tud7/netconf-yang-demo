from ncclient import manager

mgr = manager.connect(host='localhost',
                    port=1831,
                    username='root',
                    password='root',
                    hostkey_verify=False)

CONFIGURATION  = """
<data xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"/>
"""

data = mgr.edit_config(config=CONFIGURATION, target='running', default_operation="merge")
print(data)

mgr.close_session()
