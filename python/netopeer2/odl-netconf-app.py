import os
import argparse
from urllib import response
import click
import atexit
import requests

'''
# DEBUG
import logging

try: # for Python 3
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
HTTPConnection.debuglevel = 1

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# DEBUG
'''

import xml.dom.minidom

from requests.auth import HTTPBasicAuth

os.environ['http_proxy'] = '' # temporary work-around: disable proxy for localhost... TODO: find a long-term solution

@click.group()
def cli():
    pass

@cli.command()
def get_devices():
    """Get List of NETCONF Devices"""

    url        = 'http://localhost:8181/restconf/operational/network-topology:network-topology/topology/topology-netconf'
    response   = _get_request(url)    
    topologies = response['topology']

    for topo in topologies:
        nodes = topo['node']
        for node in nodes:
            print("%s: %s " %(node['node-id'], node['netconf-node-topology:connection-status']))


@cli.command()
@click.argument("node-name")
def get_capability(node_name):
    """Get NETCONF Capabilities"""

    url = 'http://localhost:8181/restconf/operational/network-topology:network-topology/topology/topology-netconf/node/%s' %node_name

    response     = _get_request(url)
    capabilities = response['node'][0]['netconf-node-topology:available-capabilities']['available-capability']

    for c in capabilities:
        print(c['capability'])


@cli.command()
@click.argument("schema-name")
def get_schema(schema_name:str):
    """Get NETCONF Schema"""
    print("Not Supported")
    
    
@cli.command()
@click.option("-f", "--filter-file", help="Full path to the filter XML file", default=None)
def get_config(filter_file):
    """Get NETCONF Config"""
    
    filter_xml = None

    if filter_file is not None:
      with open(filter_file, "r") as ff:
         #read whole file to a string
         filter_xml = ff.read()
 
    print("Not Supported")


@cli.command()
@click.option("-f", "--config-file", help="Full path to config file")
def edit_config(config_file:str):
    """Edit NETCONF Config"""
           
    print("Not Supported")


def _get_request(url):

    if url is None:
        raise RuntimeError('URL is None')

    response = requests.get(url, auth=HTTPBasicAuth('admin', 'admin'))
    response.raise_for_status()
    
    return response.json()
    

def main():
    cli()


if __name__ == '__main__':
   main()
   
   
   
