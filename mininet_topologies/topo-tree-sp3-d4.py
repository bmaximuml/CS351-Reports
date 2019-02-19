"""Tree Topology

A tree topology with a spread of 3 and a depth of 4
                       s
        s              s               s
    s   s   s      s   s   s       s   s   s
   hhh hhh hhh    hhh hhh hhh     hhh hhh hhh

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class TreeTopo(Topo):
    "Simple topology example."

    def __init__( self ):
        "Create tree topo."

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        # switch naming convention:
        #   s{level}{previous_switch_number}{switch_number}
        s111 = self.addSwitch('s111')

        s211 = self.addSwitch('s211')
        s212 = self.addSwitch('s212')
        s213 = self.addSwitch('s213')

        self.addLink(s111, s211)
        self.addLink(s111, s212)
        self.addLink(s111, s213)

        s311 = self.addSwitch('s311')
        s312 = self.addSwitch('s312')
        s313 = self.addSwitch('s313')

        self.addLink(s211, s311)
        self.addLink(s211, s312)
        self.addLink(s211, s313)

        s321 = self.addSwitch('s321')
        s322 = self.addSwitch('s322')
        s323 = self.addSwitch('s323')

        self.addLink(s212, s321)
        self.addLink(s212, s322)
        self.addLink(s212, s323)

        s331 = self.addSwitch('s331')
        s332 = self.addSwitch('s332')
        s333 = self.addSwitch('s333')        

        self.addLink(s213, s331)
        self.addLink(s213, s332)
        self.addLink(s213, s333)

        
        for i in range(27):
            hosts[i] = self.addHost(f'h{i]')
            if i < 3:
                self.addLink(s311, hosts[i])
            elif i < 6:
                self.addLink(s312, hosts[i])

            elif i < 9:
                self.addLink(s313, hosts[i])

            elif i < 12:
                self.addLink(s321, hosts[i])

            elif i < 15:
                self.addLink(s322, hosts[i])

            elif i < 18:
                self.addLink(s323, hosts[i])

            elif i < 21:
                self.addLink(s331, hosts[i])

            elif i < 24:
                self.addLink(s332, hosts[i])

            else:
                self.addLink(s333, hosts[i])


topos = { 'treetopo': ( lambda: TreeTopo() ) }
