## GOOSE Attack Dataset
The GOOSE attack dataset consists of two versions
1. **Raw dataset**: raw network traffic capture file (\*.pcapng). Rough time period estimation of different behaviours, see "List of Scenarios.xlsx" for details.
2. **Processed dataset**: ready for supervised machine learning (\*.csv). A comprehensive feature engineering process was conducted to choose essential features from both GOOSE and SV packets. Most importantly, all samples were labelled based on 32 types of behaviours, including one pure fault-free scenario (label 0), 10 emergency scenarios (labels 101-110), and 21 attack scenarios (labels 811-813, 821-823, 831-833, 841-843, 851-853, 861-863, 871-873).

### Dataset summary
During fault-free operations, from the adversaries’ perspective, the final objective of untrusted components is to interrupt normal energy transmissions. Although untrusted companies may also harvest secret information, maintain secret remote access, and spread malware to affect more targets, the ultimate goal of a substation attack is to disrupt energy transmissions during fault-free operations after all these preparations. Therefore, during fault-free operations, to achieve this goal in our simulation testbed, we implemented three attack scenarios 811-813 (addition of fake data or fake messages) and three attack scenarios 821-823 (modification of data in the original message).

During emergency operations, from the adversaries’ perspective, there may be two final objectives using untrusted components. One goal is triggering undesirable protection actions, and exacerbating the impacts of emergency situations, such as a blackout. Another more destructive intention is stopping designed protection mechanisms and bringing chaos to a substation, such as transformer explosions. Therefore, during emergency operations, to achieve the first attack objective in our simulation testbed, we implemented three attack scenarios 851-853 (addition of fake data or fake messages) and three attack scenarios 861-863 (modification of data in the original message). Additionally, to achieve the second attack objective in our simulation testbed, we implemented three attack scenarios 831-833 (addition of fake data or fake messages), three attack scenarios 841-843 (modification of data in the original message), and three attack scenarios 871-873 (deletion of the original message).

In summary, a total of 21 scenarios (811-813, 821-823, 831-833, 841-843, 851-853, 861-863, 871-873) were generated from the testbed. Each scenario consists of different numbers of sub-scenarios, and a total of 178 sub-scenarios were generated in the GOOSE Attack Dataset. The details of each scenario and sub-scenario are discussed in "List of Scenarios.xlsx". Although it is called attack dataset, each sub-scenario not only contains one particular attack behaviour, but also includes non-malicious behaviours, such as 1) fault-free operations when no unusual events happen (labelling as 0), and 2) emergency operations when non-malicious events (e.g., short-circuit faults) happen. 

There are a total of 10 emergency scenarios, which were labelled from 101 to 110. The details of each scenairo are listed below:
- **101**: When a short-circuit fault occurs on Fault_66bus1, associated protection mechanism acts immediately and isolates the fault effectively.
- **102**: When a short-circuit fault occurs on Fault_66bus2, associated protection mechanism acts immediately and isolates the fault effectively.
- **103**: When a short-circuit fault occurs on Fault_XFMR1, associated protection mechanism acts immediately and isolates the fault effectively. 
- **104**: When a short-circuit fault occurs on Fault_XFMR2, associated protection mechanism acts immediately and isolates the fault effectively. 
- **105**: When a short-circuit fault occurs on Fault_22bus1, associated protection mechanism acts immediately and isolates the fault effectively. 
- **106**: When a short-circuit fault occurs on Fault_22bus2, associated protection mechanism acts immediately and isolates the fault effectively.
- **107**: When a short-circuit fault occurs on Fault_FDR1, associated protection mechanism acts immediately and isolates the fault effectively. 
- **108**: When a short-circuit fault occurs on Fault_FDR2, associated protection mechanism acts immediately and isolates the fault effectively.
- **109**: When a short-circuit fault occurs on Fault_FDR3, associated protection mechanism acts immediately and isolates the fault effectively.
- **110**: When a short-circuit fault occurs on Fault_FDR4, associated protection mechanism acts immediately and isolates the fault effectively.

> The labelling of 101-110 start when the fault happens, and stops when systems start to recover (the fault was eliminated).

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510" />