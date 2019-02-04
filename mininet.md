# [Mininet](http://mininet.org) Notes

## Install from source

1. git clone git://github.com/mininet/mininet
2. cd mininet
3. git tag # list available versions
4. git checkout -b 2.2.2 2.2.2
5. cd ..
6. mininet/util/install.sh -a
7. sudo mn --test pingall # test basic Mininet functionality

## Introduction

### Creating a Network
You can create a network with a single command. For example,

`sudo mn --switch ovs --controller ref --topo tree,depth=2,fanout=8 --test pingall`

starts a network with a tree topology of depth 2 and fanout 8 (i.e. 64 hosts connected to 9 switches), using Open vSwitch switches under the control of the OpenFlow/Stanford reference controller, and runs the pingall test to check connectivity between every pair of nodes. (This takes about 67 seconds on Iroh.)

### Customizing a Network

Mininet’s API allows you to create custom networks with a few lines of Python. For example, the following script

```
from mininet.net import Mininet
from mininet.topolib import TreeTopo
tree4 = TreeTopo(depth=2,fanout=2)
net = Mininet(topo=tree4)
net.start()
h1, h4  = net.hosts[0], net.hosts[3]
print h1.cmd('ping -c1 %s' % h4.IP())
net.stop()
```

creates a small network (4 hosts, 3 switches), and pings one host from another (in about 4 seconds with the current version.)

The Mininet distribution includes several text-based and graphical (see above) applications which we hope will be instructive and inspire you to create cool and useful apps for your own network designs.

## Walkthrough

* `$` preceeds Linux commands that should be typed at the shell prompt
* `mininet>` preceeds Mininet commands that should be typed at Mininet’s CLI,
* `#` preceeds Linux commands that are typed at a root shell prompt

`$ sudo mn -h` Mininet help

`$ sudo wireshark &` View control traffic using OpenFlow Wireshark dissector

`$ sudo mn -h` Start a minimal topology and enter the CLI.
This topology constitutes one switch, two hosts, and the OpenFlow reference controller.

`mininet> help` Display Mininet CLI commands

`mininet> nodes` Display nodes

`mininet> net` Display links

`mininet> dump` Display information about all nodes

If the first string typed into the Mininet CLI is a host, switch or controller name, the command is executed on that node. For example: `mininet> h1 ifconfig -a`
