* Explain FPGAs
  * why are FPGAs applicable to this project
* Explain networking
  * with specific reference to this project
    * explain SDN
      * P4
      * OpenFlow

    * Explain ping
      * ICMP
  * generally
* Mininet
  * Broad, useful tool
  * limited capability
  * Python API
    * pros
    * cons
  * Adds dependency chain
  * Use of git submodules
  * Installation with bash script

* Relevance to CSE

* Project Management
  * Open Source
    * GitHub
  * git
  * Trello
  * Good software development practices
    * pylint
    * PEP 8
    * Fully documented (?)
    * pydoc?
  * PyCharm
  * Atom
  * LaTeX
  * VirtualBox
  * Docker

* Python
  * PEP8
  * PyPI
  * Scalable
  * Click
  * CLI options

* Explain project
  * Sending data to cloud has a large latency. Sending SO MUCH data has a very large latency. Currently, most network architectures involve large datacentres performing most of the compute.
    * Attempts have been made to solve this problem, such as "edge nodes", however these have significant drawbacks, such as the additional latency involved with processing the data in these nodes.
    * An alternative solution is to avoid pulling the data out from its original path. This concept led to the idea of performing the computation inside of network switches.
    * ASICs and general purpose CPUs both offer certain advantages over FPGAs, and could theoretically replace FPGAs in these smart switches. However, ASICs are only able to compute one algorithm once they have been fabricated. This makes them extremely inflexible, as naturally each user of the FPGA smart switches will have different algorithms and different data. CPUs on the other hand are extremely slow compared to FPGAs and ASICs, since they are so general purpose. Unlike ASICs and FPGAs, CPUs are also not standalone devices, requiring other components such as RAM, motherboards, and storage in order to process data.
    * FPGAs construct circuits in hardware based on the algorithm they are programmed. While still not as fast as ASICs, this makes them significantly faster than a general purpose CPU. In addition, unlike ASICs, they are not limited to a single algorithm, and can be programmed using popular hardware description languages such as Verilog or VHDL.
  *


* Applications / Use cases
  * Education
  * Medicine
  * IoT
    * Hugo Fiennes & Electric Imp

* How would the project be expanded to NetFPGA

* References
