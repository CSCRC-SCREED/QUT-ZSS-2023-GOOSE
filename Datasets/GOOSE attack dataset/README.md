## GOOSE Attack Dataset
The GOOSE attack dataset consists of two versions
1. Raw dataset: raw network traffic capture file (\*.pcap). Rough labelling with different behaviours in approximate time periods. 
2. Processed dataset: ready for supervised machine learning. A comprehensive feature engineering process was conducted to choose essential features from both GOOSE and SV packets. Most importantly, all samples were labelled based on 55 types of behaviours.

### Dataset summary
A total of 55 scenarios were collected from the testbed, including one pure fault-free scenario (label 0), 14 emergency scenarios (labels 101-114), and 21 attack scenarios (labels 811-813, 821-823, 831-833, 841-843, 851-853, 861-863, 871-873). Except for the pure fault-free scenario only contains one fault-free behaviour, the rest of the scenarios involve multiple successive behaviours, including fault-free behaviours, overcurrent protection behaviours, breaker failure protection behaviours, and attack behaviours.

Although it is called GOOSE attack dataset, each scenario still consists of four types of behaviours in smart zone substations: 1) fault-free operations when no unusual events happen, 2) emergency operations when non-malicious events (e.g., short-circuit faults) happen, 3) false data injection (FDI) attacks originated from untrusted intelligent electronic devices (IEDs) and target GOOSE communications.

During fault-free operations, from the adversaries’ perspective, the final objective of un-trusted components is to interrupt normal energy transmissions. Although untrusted companies may also harvest secret information, maintain secret remote access, and spread malware to affect more targets, the ultimate goal of a substation attack is to disrupt energy transmissions during fault-free operations after all these preparations.

During emergency operations, from the adversaries’ perspective, there may be two final objectives using untrusted components. One goal is triggering undesirable protection actions, and exacerbating the impacts of emergency situations, such as a blackout. Another more destructive intention is stopping designed protection mechanisms and bringing chaos to a substation, such as transformer explosions.