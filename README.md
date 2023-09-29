# QUT Zone Substation Security Datasets (2023)

## Background
Zone Substations are used to transform sub-transmission voltages (typically 34.5 kV to 69 kV) to high-voltage distribution voltages (typically 11 kV to 22 kV) and to act as controlling points between different high-voltage networks. The figure below illustrates the overall architecture and process of common power girds.

<img src="PowerGrids.jpg" alt="" width="600" height="552" />

**Retrieved and edited from https://www.copper.org/environment/sustainable-energy/grid-infrastructure/**

The datasets were generated and collected from a software-based simulation testbed. The testbed simulates a small-scale smart zone substation, including the primary plant (physical process), the control devices (Intelligent electronic devices or IEDs), and the process bus communication networks. The figure below demonstrates the testbed architecture.

<img src="Testbed design.jpg" alt="" width="800" height="553" />

In summary, the datasets contain a wide variety of network and physical behaviours in an IEC-61850-compliant zone substation. The datasets are compatible with actual substation network traffic, including both Generic Object-Oriented Substation Event (GOOSE) and Sampled Value (SV) network packets. Most importantly, all datasets have been labelled accurately based on the different behaviours.

All attack scenarios in our datasets are false data injection (FDI) attacks and replay attacks. We implemented all three forms of FDI attacks targeting both GOOSE and SV communications, including 1) deletion of data from the original message; 2) modification of data in the original message, and 3) addition of fake data or fake messages.

## GOOSE Attack Dataset
The dataset consists of four types of behaviours in smart zone substations: 1) fault-free operations when no unusual events happen, 2) emergency operations when non-malicious events (e.g., short-circuit faults) happen, 3) false data injection (FDI) attacks originated from untrusted intelligent electronic devices (IEDs) and target GOOSE communications.

### Dataset summary
A total of 55 scenarios were collected from the testbed, including one pure fault-free scenario (label 0), 14 emergency scenarios (labels 101-114), and 21 attack scenarios (labels 811-813, 821-823, 831-833, 841-843, 851-853, 861-863, 871-873). Except for the pure fault-free scenario only contains one fault-free behaviour, the rest of the scenarios involve multiple successive behaviours, including fault-free behaviours, overcurrent protection behaviours, breaker failure protection behaviours, and attack behaviours.

During fault-free operations, from the adversaries’ perspective, the final objective of un-trusted components is to interrupt normal energy transmissions. Although untrusted companies may also harvest secret information, maintain secret remote access, and spread malware to affect more targets, the ultimate goal of a substation attack is to disrupt energy transmissions during fault-free operations after all these preparations.

During emergency operations, from the adversaries’ perspective, there may be two final objectives using untrusted components. One goal is triggering undesirable protection actions, and exacerbating the impacts of emergency situations, such as a blackout. Another more destructive intention is stopping designed protection mechanisms and bringing chaos to a substation, such as transformer explosions.

## SV Attack Dataset
The dataset consists of four types of behaviours in smart zone substations: 1) fault-free operations when no unusual events happen, 2) emergency operations when non-malicious events (e.g., short-circuit faults) happen, and 3) false data injection (FDI) attacks originated from untrusted merging units (MUs) and target SV communications.
