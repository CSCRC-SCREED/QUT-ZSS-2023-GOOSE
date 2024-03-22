## Testbed essential scripts

The testbed simulates both the primary plant and secondary plant of an electricity distribution substation, especially the physical distribution process and the process bus communications based on the IEC 61850 standard. The testbed runs on an Oracle VirtualBox with five virtual machines (VMs). One VM simulates a small-scale primary plant of a distribution substation using [**MATLAB/Simulink**](https://www.mathworks.com/products/simulink). The other three VMs represent three instantaneous-overcurrent-protection relays using [**OpenPLC**](https://www.openplcproject.com). Communication interfaces among each VM, such as GOOSE and SV messages between IEDs and the primary plant, are written in C++ based on an open-source library - [**libiec61850**](http://libiec61850.com). The last VM simulates the process bus network switch.

**Each folder/directory contains various essential scripts for one particular Virtual Machine. These include:**
- Primary plant: the physical process
- XFMR1 OverCur Prot: the overcurrent protection IED/relays  for transformer1
- XFMR2 OverCur Prot: the overcurrent protection IED/relays  for transformer2
- FDR OverCur Prot: the overcurrent protection IED/relays  for feeders
- Process bus Switch: Network switch in the process bus

> Port summary.xlsx: indicates all the UDP port numbers for communication between Simulink and OpenPLC

> **Sincerely thanks [Thiago Alves](https://github.com/thiagoralves) for helping me solve issues regarding OpenPLC_Simulink-Interface.**
