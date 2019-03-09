#!/usr/bin/python

"""
Simple example of setting network and CPU parameters

NOTE: link params limit BW, add latency, and loss.
There is a high chance that pings WILL fail and that
iperf will hang indefinitely if the TCP handshake fails
to complete.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

# from mininet_topologies import TreeTopo

# from sys import argv

class TreeTopoGeneric(Topo):
    "Simple topology example."

    def __init__(self):
        "Create tree topo."

        # Initialize topology
        Topo.__init__(self)

        spread = 3
        depth = 4
        bw = 10
        delay = '20ms'
        loss = 1

        # 10 Mbps bandwidth, 20 ms delay, 1% packet loss on each link
        linkopts = dict(bw=bw, delay=delay, loss=loss, use_htb=True)

        # Add hosts and switches

        # switch naming convention:
        #   s[level][switch_number]


        switches = [[None for x in range(spread ** depth)] for y in range(depth - 1)]
        hosts = [None for x in range(spread ** depth)]

        for i in range(depth):
            for j in range(spread ** i):
                if i == (depth - 1):
                    hosts[j] = self.addHost('h' + str(j))
                else:
                    sw_name = 's' + str(i) + str(j)
                    switches[i][j] = self.addSwitch(sw_name)


        for i, row in enumerate(switches):
            for j, switch in enumerate(row):
                if switch is None:
                    break;
                if i == (depth - 2):
                    for k in range(spread):
                        # add a link between the current switch, and all hosts
                        # directly beneath it.
                        # (spread * j) + k will get all the appropriate hosts
                        self.addLink(switch, hosts[(spread * j) + k])

                else:
                    for k in range(spread):
                        # add a link between the current switch, and all
                        # switches directly beneath it.
                        # i + 1 refers to 1 level deeper in the tree, and
                        # (spread * j) + k will get all the appropriate child
                        # switches on that level.
                        self.addLink(switch, switches[i + 1][(spread * j) + k])


def perfTest():
    "Create network and run simple performance test"
    topo = TreeTopoGeneric()
    net = Mininet(topo=topo,
                  host=CPULimitedHost, link=TCLink,
                  autoStaticArp=True)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)

    print "Running ping test between all hosts"
    net.pingAll()

    print "Testing bandwidth between first and last hosts"
    # h1, h4 = net.getNodeByName('h1', 'h4')
    net.iperf()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    # Prevent test_simpleperf from failing due to packet loss
    perfTest()
