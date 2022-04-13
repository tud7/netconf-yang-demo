import argparse
import click
import atexit

import xml.dom.minidom

from ncclient import manager

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
@click.argument("schema-name")
def get_schema(schema_name:str):
    """Get NETCONF Schema"""
    if schema_name:
      print( mgr.get_schema(schema_name) )
    
    
@cli.command()
@click.option("-f", "--filter-file", help="Full path to the filter XML file", default=None)
def get_config(filter_file):
    """Get NETCONF Config"""
    
    filter_xml = None

    if filter_file is not None:
      with open(filter_file, "r") as ff:
         #read whole file to a string
         filter_xml = ff.read()
 
    netconf_reply = mgr.get_config('running', filter=filter_xml)
    config_dom    = xml.dom.minidom.parseString(netconf_reply.xml)
    print( config_dom.toprettyxml(indent='   ') )


@cli.command()
@click.option("-f", "--config-file", help="Full path to config file")
def edit_config(config_file:str):
    """Edit NETCONF Config"""
           
    #open text file in read mode
    with open(config_file, "r") as cf:
 
        #read whole file to a string
        config = cf.read()
        data = mgr.edit_config(config=config, target='running', default_operation="replace")
        print(data)
    

def main():
    cli()


def on_exit():
    mgr.close_session()

atexit.register(on_exit)

if __name__ == '__main__':
   main()
   
   
   
