import argparse
import click
import atexit

import xml.dom.minidom

from ncclient import manager

'''mgr = manager.connect(host='sandbox-iosxe-latest-1.cisco.com',
                    port=830,
                    username='developer',
                    password='C1sco12345',
                    hostkey_verify=False,
                    device_params={'name':'csr'})
'''                 
'''
mgr = manager.connect(host='localhost',
                    port=1831,
                    username='root',
                    password='root',
                    hostkey_verify=False)
'''
mgr = manager.connect(host='localhost',
                    port=830,
                    username='netconf',
                    password='netconf',
                    hostkey_verify=False)

@click.group()
def cli():
    pass


@cli.command()
def get_capability():
    """Get NETCONF Capabilities"""
    
    for capability in mgr.server_capabilities:
        print(capability)

@cli.command()
@click.option("-n", "--schema-name", default="ietf-netconf-monitoring", help="Schema Name")
def get_schema(schema_name:str):
    """Get schema"""
    print( mgr.get_schema(schema_name) )
    
    
@cli.command()
def get_config():
    """Get Config"""
    netconf_reply = mgr.get_config('running')
    config_dom    = xml.dom.minidom.parseString(netconf_reply.xml)
    print( config_dom.toprettyxml(indent='   ') )


@cli.command()
@click.option("-c", "--config-file", help="Full path to config file")
def edit_config(config_file:str):
    """Edit Config"""
    
    """CONFIGURATION  = 
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                <hostname>tmd12345</hostname>
            </native>
        </config>
    """
    '''
    CONFIGURATION  = """
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <netconf-server xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-server">
         <listen>
            <endpoint>
               <name>default-ssh</name>
               <ssh>
                  <tcp-server-parameters>
                     <local-address>0.0.0.0</local-address>
                     <keepalives>
                        <idle-time>2</idle-time>
                        <max-probes>10</max-probes>
                        <probe-interval>5</probe-interval>
                     </keepalives>
                  </tcp-server-parameters>
                  <ssh-server-parameters>
                     <server-identity>
                        <host-key>
                           <name>default-key</name>
                           <public-key>
                              <keystore-reference>genkey</keystore-reference>
                           </public-key>
                        </host-key>
                     </server-identity>
                     <client-authentication>
                        <supported-authentication-methods>
                           <publickey/>
                           <passsword/>
                           <other>interactive</other>
                        </supported-authentication-methods>
                        <users/>
                     </client-authentication>
                  </ssh-server-parameters>
               </ssh>
            </endpoint>
         </listen>
      </netconf-server>

    </config>
    """
    '''
    
    #open text file in read mode
    with open(config_file, "r") as cf:
 
        #read whole file to a string
        config = cf.read()
        
        data = mgr.edit_config(config=config, target='running', default_operation="merge")
        print(data)
    

def main():
    cli()


def on_exit():
    mgr.close_session()

atexit.register(on_exit)

if __name__ == '__main__':
   main()
   
   
   
