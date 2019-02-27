"""Tree Topology

A tree topology

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.

TCULinks are required to support the delays.

Run a test to ping every node from every other node with the command:
`sudo mn --custom topo-tree-sp3-d4-delay.py --topo treetopo --link tc --test pingall`


"""

from mininet.topo import Topo

class TreeTopoGeneric(Topo):
    "Simple topology example."

    def __init__( self ):
        "Create tree topo."

        # Initialize topology
        Topo.__init__(self)

        spread = 3
        depth = 4

        # 10 Mbps bandwidth, 20 ms delay, 1% packet loss on each link
        linkopts = dict(bw=10, delay='20ms', loss=1, use_htb=True)

        # Add hosts and switches

        # switch naming convention:
        #   s{level}{previous_switch_number}{switch_number}


        switches = [[None for x in range(spread ** depth)] for y in range(depth)]
        hosts = [None for x in range(spread ** depth)]

        for i in range(depth):
            for j in range(spread ** i):
                if i == depth - 1:
                    hosts[j] = self.addHost('h' + str(j))
                else:
                    sw_name = 's' + str(i) + str(j)
                    switches[i][j] = self.addSwitch(sw_name)


topos = { 'treetopogeneric': ( lambda: TreeTopoGeneric() ) }
