* Research fibre cabinets (such as those provided by Openreach), and Local Distribution Units
* Think about common sense scenarios for max switches between datacentre and edge
    * Floor plans for buildings / skyscrapers etc could help with this
* Does mininet support Poisson distribution for switch latency?
    * [netem](https://wiki.linuxfoundation.org/networking/netem#delay_distribution)
    * Switch latency is added through mininet [Links](http://mininet.org/api/classmininet_1_1link_1_1Link.html)
* You need to create different graphs of tree topologies with smart switches at different levels in the topology
    * Vary this further by applying different performance decrease of smart switch
    * And different latencies at switches

* Hierarchical Token Bucket (HTB) rate limiting algorithm (use_htb=true on links)
