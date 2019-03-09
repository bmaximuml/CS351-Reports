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
from mininet.clean import Cleanup

import click
import re

# from sys import argv

class TreeTopoGeneric(Topo):
    "Simple topology example."

    def __init__(self, spread, depth, bandwidth, delay, loss):
        "Create tree topo."

        # Initialize topology
        Topo.__init__(self)

        # 10 Mbps bandwidth, 20 ms delay, 1% packet loss on each link
        linkopts = dict(bw=bandwidth, delay=delay, loss=loss, use_htb=True)

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
                        self.addLink(switch, hosts[(spread * j) + k], **linkopts)

                else:
                    for k in range(spread):
                        # add a link between the current switch, and all
                        # switches directly beneath it.
                        # i + 1 refers to 1 level deeper in the tree, and
                        # (spread * j) + k will get all the appropriate child
                        # switches on that level.
                        self.addLink(switch, switches[i + 1][(spread * j) + k], **linkopts)



def validate_delay(ctx, param, value):
    valid_time = re.compile("^[0-9]+[PTGMkmunpf]?s$")
    # This will allow any valid time, such as '10ms', '23s', '1Gs', etc.
    # Naturally 1 Ps is both an absurd unit and not a very useful delay, but it should technically be valid.
    if not valid_time.match(value):
        raise click.BadParameter("delay must be in the format <time><unit>s. E.g. '10ms', '23s', '200ns'.")


@click.command()
@click.option('-s', '--spread', default=3, show_default=True, help='Number of children each node will have')
@click.option('-d', '--depth', default=4, show_default=True, help='Number of levels in the tree')
@click.option('-b', '--bandwidth', default=10, show_default=True, help='Max bandwidth of all links in Mbps')
@click.option('-e', '--delay', default='20ms', show_default=True, help='Max bandwidth of all links', callback=validate_delay)
@click.option('-l', '--loss', default=0, show_default=True, help='% chance of packet loss for all links')
@click.option('--log', default='info', show_default=True, help='Set the log level')


def performance_test(log, spread, depth, bandwidth, delay, loss):
    Cleanup.cleanup()
    setLogLevel(log)
    "Create network and run simple performance test"
    topo = TreeTopoGeneric(spread, depth, bandwidth, delay, loss)
    net = Mininet(topo=topo,
                  host=CPULimitedHost, link=TCLink,
                  autoStaticArp=True)
    net.start()
    click.echo("Dumping host connections")
    dumpNodeConnections(net.hosts)

    click.echo("Running ping test between all hosts")
    net.pingAll()

    click.echo("Testing bandwidth between first and last hosts")
    # h1, h4 = net.getNodeByName('h1', 'h4')
    net.iperf()
    net.stop()

if __name__ == '__main__':
    performance_test()
