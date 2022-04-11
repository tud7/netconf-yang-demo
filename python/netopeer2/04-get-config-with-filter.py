from ncclient import manager

mgr = manager.connect(host='localhost',
                    port=1831,
                    username='root',
                    password='root',
                    hostkey_verify=False)

# Filter hostname
FILTER = """
    <nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">
        <write-default>permit</write-default>
    </nacm>"""

config = mgr.get(filter=("subtree", FILTER))
print(config)

mgr.close_session()
