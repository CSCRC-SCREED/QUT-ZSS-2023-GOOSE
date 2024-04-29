## Scenario 831
In this scenario, the malicious program injects counterfeit GOOSE packets when a short-circuit fault happens. Such an attack will mislead circuit breakers with fake closing signals to disable safety protection. The scenario contains a total of ${\color{red}16}$ sub-scenarios, which are combinations of ${\color{red}four}$ attack targets and ${\color{red}four}$ attack configurations.

> In this scenario, there is an approximately 30-second DMZ period. The DMZ here represents a buffer between the 1st attack cycle and the 2nd attack cycle. The data within the DMZ period is either valid (labelled as **0**) or invalid (labelled as **N/V**) according to different sub-scenarios. Please see the README file in each sub-scenario folder for details.

**QUTZS_GOOSE.csv extracts all GOOSE features of all GOOSE packets from the raw network traffic**

**QUTZS_SV.csv extracts all SV features of all SV packets from the raw network traffic**

**QUTZS_final.xlsx merges both GOOSE and SV features based on packet arrival timestamp, and most importantly labels each merged sample based on 32 types of behaviours**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: disrupting the safety protection when a short-circuit fault happens in Fault_66bus1
   - **b**: disrupting the safety protection when a short-circuit fault happens in Fault_XFMR1
   - **c**: disrupting the safety protection when a short-circuit fault happens in Fault_66bus2
   - **d**: disrupting the safety protection when a short-circuit fault happens in Fault_XFMR2
2. **${\color{red}Four}$ attack configurations**:
   - **8311**: injecting packets with a fixed heartbeat of 500ms when a short-circuit fault happens
   - **8312**: injecting only 40 packets with a fixed heartbeat of 500ms when a short-circuit fault happens
   - **8313**: injecting packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms when a short-circuit fault happens
   - **8314**: injecting only 30 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms when a short-circuit fault happens

> <sup>*</sup> The dynamic heartbeats in attack configurations **8313** and **8314** are followed by practical behaviours when power systems are recovered from a true short-circuit fault.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-GOOSE/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
