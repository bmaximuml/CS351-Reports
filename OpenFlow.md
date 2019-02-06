# [OpenFlow](https://github.com/mininet/openflow-tutorial/wiki) notes

* `ovs-ofctl` can be used to show and modify information about the flow table for an Open vSwitch switch.

  * `# ovs-ofctl add-flow s1 in_port=1,actions=output:2` Forward packets coming in at port 1 to port 2 on switch s1
  * `# ovs-ofctl add-flow s1 in_port=2,actions=output:1` Forward packets coming in at port 2 to port 1 on switch s1

* [POX](https://noxrepo.github.io/pox-doc/html/) is a Python-based SDN controller platform geared towards research and education.
