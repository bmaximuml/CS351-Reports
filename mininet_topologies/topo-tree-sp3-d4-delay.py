"""Tree Topology

A tree topology with a spread of 3 and a depth of 4
                       s
        s              s               s
    s   s   s      s   s   s       s   s   s
   hhh hhh hhh    hhh hhh hhh     hhh hhh hhh

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.

TCULinks are required to support the delays.

Run a test to ping every node from every other node with the command:
`sudo mn --custom topo-tree-sp3-d4-delay.py --topo treetopo --link tc --test pingall`


"""

from mininet.topo import Topo

class TreeTopo(Topo):
    "Simple topology example."

    def __init__( self ):
        "Create tree topo."

        # Initialize topology
        Topo.__init__(self)

        # 10 Mbps bandwidth, 20 ms delay, 1% packet loss on each link
        linkopts = dict(bw=10, delay='20ms', loss=1, use_htb=True)

        # Add hosts and switches

        # switch naming convention:
        #   s{level}{previous_switch_number}{switch_number}

        s011 = self.addSwitch('s011')

        s111 = self.addSwitch('s111')
        s112 = self.addSwitch('s112')
        s113 = self.addSwitch('s113')

        self.addLink(s011, s111, **linkopts)
        self.addLink(s011, s112, **linkopts)
        self.addLink(s011, s113, **linkopts)

        s211 = self.addSwitch('s211')
        s212 = self.addSwitch('s212')
        s213 = self.addSwitch('s213')

        self.addLink(s111, s211, **linkopts)
        self.addLink(s111, s212, **linkopts)
        self.addLink(s111, s213, **linkopts)

        s221 = self.addSwitch('s221')
        s222 = self.addSwitch('s222')
        s223 = self.addSwitch('s223')

        self.addLink(s112, s221, **linkopts)
        self.addLink(s112, s222, **linkopts)
        self.addLink(s112, s223, **linkopts)

        s231 = self.addSwitch('s231')
        s232 = self.addSwitch('s232')
        s233 = self.addSwitch('s233')        

        self.addLink(s113, s231, **linkopts)
        self.addLink(s113, s232, **linkopts)
        self.addLink(s113, s233, **linkopts)

        hosts = []
        for i in range(27):
            hosts.append(self.addHost('h' + str(i)))
            if i < 3:
                self.addLink(s211, hosts[i], **linkopts)
            elif i < 6:
                self.addLink(s212, hosts[i], **linkopts)

            elif i < 9:
                self.addLink(s213, hosts[i], **linkopts)

            elif i < 12:
                self.addLink(s221, hosts[i], **linkopts)

            elif i < 15:
                self.addLink(s222, hosts[i], **linkopts)

            elif i < 18:
                self.addLink(s223, hosts[i], **linkopts)

            elif i < 21:
                self.addLink(s231, hosts[i], **linkopts)

            elif i < 24:
                self.addLink(s232, hosts[i], **linkopts)

            else:
                self.addLink(s233, hosts[i], **linkopts)


topos = { 'treetopo': ( lambda: TreeTopo() ) }
