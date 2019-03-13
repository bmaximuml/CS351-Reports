# [Mininet](http://mininet.org) Notes

## Install from source

1. `git clone https://github.com/mininet/mininet`
2. `cd mininet`
3. `git tag` # list available versions
4. `git checkout -b 2.2.2 2.2.2`
5. `cd ..`
6. `mininet/util/install.sh -a`
7. `sudo mn --test pingall` # test basic Mininet functionality

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

### Part 1: Everyday Mininet Usage

* `$ sudo mn -h` Mininet help

* `$ sudo wireshark &` View control traffic using OpenFlow Wireshark dissector

* `$ sudo mn` Start a minimal topology and enter the CLI.
This topology constitutes one switch, two hosts, and the OpenFlow reference controller.

* `mininet> help` Display Mininet CLI commands

* `mininet> nodes` Display nodes

* `mininet> net` Display links

* `mininet> dump` Display information about all nodes

* If the first string typed into the Mininet CLI is a host, switch or controller name, the command is executed on that node. For example: `mininet> h1 ifconfig -a`

* `mininet> pingall` Test ping between all pairs

* `mininet> h1 python -m SimpleHTTPServer 80 &` Run a simple web server on *h1*

* `mininet> exit` Exit mininet CLI

* `$ sudo mn -c` Cleanup mininet

### Part 2: Advanced Startup Options

* Commands can be run on a Mininet topology without dropping into the CLI.

  * `$ sudo mn --test pingpair` Create a minimal topology, run an all pairs ping test, then tear down.

  * `$ sudo mn --test iperf` Create a minimal topology, test TCP bandwidth between hosts, then tear down.

* The `--topo` flag can be used to change the topology.

  * `$ sudo mn --test pingall --topo single,3` Three hosts instead of default two.

  * `$ sudo mn --test pingall --topo linear,4` Linear topology (where each switch has one host, and all switches connect in a line).

* Mininet 2.0 allows you to set link parameters, and these can even be set automatially from the command line

  * `$ sudo mn --link tc,bw=10,delay=10ms` Set bandwidth to 10Mb/s, add a 10ms delay. *tc* refers to a TCLink.

* The Python API can be used to define more complex custom topologies. The CLI can take a *.py* file as an argument to a flag and use that to define the topology.
  * `$ sudo mn --custom ~/mininet/custom/topo-2sw-2host.py --topo mytopo --test pingall` Create a custom topology from the Python file.

* `$ sudo mn --mac` Set the MAC and IP addresses to small, unique, easy to read IDs.

* `$ sudo mn -x` Start an xterm for every host and switch

* Different types of switch can be used, such as *user-space (`--switch user`)* or *Open vSwitch (`--switch ovs`)*

* `$ sudo mn --test none` Record the time to set up and tear down a topology. (0.205s on Iroh for default topology)

* */mininet/examples* contains examples of how to use Mininet's Python API, as well as potentially useful code that has not been integreated into the main code base

* `$ sudo ~/mininet/examples/sshd.py` Start an SSH daemon on a host
