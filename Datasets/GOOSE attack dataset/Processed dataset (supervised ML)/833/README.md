## Scenario 833
In this scenario, the malicious program injects counterfeit GOOSE packets when a short-circuit fault happens. Such an attack will mislead circuit breakers with fake closing signals to disable safety protection. The scenario contains a total of ${\color{red}16}$ sub-scenarios, which are combinations of ${\color{red}four}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS_GOOSE.csv extracts all GOOSE features of all GOOSE packets from the raw network traffic**

**QUTZS_SV.csv extracts all SV features of all SV packets from the raw network traffic**

**QUTZS_final.csv merges both GOOSE and SV features based on packet recieve timestamp, and most importantly labels each merged sample based on 55 types of behaviours**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: disrupting the safety protection when a short-circuit fault happens in Fault_FDR1
   - **b**: disrupting the safety protection when a short-circuit fault happens in Fault_FDR2
   - **c**: disrupting the safety protection when a short-circuit fault happens in Fault_FDR3
   - **d**: disrupting the safety protection when a short-circuit fault happens in Fault_FDR4
2. **${\color{red}Four}$ attack configurations**:
   - **8331**: injecting packets with a fixed heartbeat of 500ms when a short-circuit fault happens
   - **8332**: injecting only 40 packets with a fixed heartbeat of 500ms when a short-circuit fault happens
   - **8333**: injecting packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms when a short-circuit fault happens
   - **8334**: injecting only 30 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms when a short-circuit fault happens

> <sup>*</sup> The dynamic heartbeats in attack configurations **8333** and **8334** are followed by practical behaviours when power systems are recovered from a true short-circuit fault.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510" />
