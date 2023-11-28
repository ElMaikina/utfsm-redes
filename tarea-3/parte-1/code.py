
#!/usr/bin/env python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.topolib import TreeNet
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf

def Interconectado():
    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller, waitConnected=True )

    info( '*** Adding controller\n' )
    net.addController( 'c0' , port=6633 )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='127.0.0.1' )
    h2 = net.addHost( 'h2', ip='127.0.0.2' )
    h3 = net.addHost( 'h3', ip='127.0.0.3' )
    h4 = net.addHost( 'h4', ip='127.0.0.4' )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1', stp=True)
    s2 = net.addSwitch( 's2', stp=True)
    s3 = net.addSwitch( 's3', stp=True)
    s4 = net.addSwitch( 's4', stp=True)

    info( '*** Creating links\n' )
    net.addLink( s1, h1 )
    net.addLink( s2, h2 )
    net.addLink( s3, h3 )
    net.addLink( s4, h4 )

    net.addLink( s1, s2 )
    net.addLink( s1, s3 )
    net.addLink( s2, s3 )
    net.addLink( s3, s4 )
    net.addLink( s4, s1 )

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    Interconectado()
