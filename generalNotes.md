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

* https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/ was used for much of the logging scripts.

* pylint used to lint python
    * Conforms to PEP8, and other good practices
* Code made open source
    * git
    * Hosted publicly on GitHub
    * Hopefully will be available on the Docker Hub


* Use `git rebase --exec 'git commit --amend --no-edit -n -S' -i development` to sign commits with GPG after committing them

* ICMP defined in [RFC 792](https://tools.ietf.org/html/rfc792)

https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.poisson.html

https://matplotlib.org/api/pyplot_api.html
