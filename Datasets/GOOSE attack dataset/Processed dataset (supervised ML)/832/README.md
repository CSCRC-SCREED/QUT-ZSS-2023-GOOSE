## Scenario 832
In this scenario, the malicious program injects counterfeit GOOSE packets when a short-circuit fault happens. Such an attack will mislead circuit breakers with fake closing signals to disable safety protection. The scenario contains a total of ${\color{red}eight}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}four}$ attack configurations.

> In this scenario, there is an approximately 30-second DMZ period. The DMZ here represents a buffer between the 1st attack cycle and the 2nd attack cycle. The data within the DMZ period is valid and shows a type of fault-free behaviours that systems were recovered from a real/fabricated fault. Therefore, data within the DMZ period was labelled as **0**.

**QUTZS_GOOSE.csv extracts all GOOSE features of all GOOSE packets from the raw network traffic**

**QUTZS_SV.csv extracts all SV features of all SV packets from the raw network traffic**

**QUTZS_final.xlsx merges both GOOSE and SV features based on packet recieve timestamp, and most importantly labels each merged sample based on 32 types of behaviours**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: disrupting the safety protection when a short-circuit fault happens in Fault_22bus1
   - **b**: disrupting the safety protection when a short-circuit fault happens in Fault_22bus2
2. **${\color{red}Four}$ attack configurations**:
   - **8321**: injecting packets with a fixed heartbeat of 500ms when a short-circuit fault happens
   - **8322**: injecting only 40 packets with a fixed heartbeat of 500ms when a short-circuit fault happens
   - **8323**: injecting packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms when a short-circuit fault happens
   - **8324**: injecting only 30 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms when a short-circuit fault happens

> <sup>*</sup> The dynamic heartbeats in attack configurations **8323** and **8324** are followed by practical behaviours when power systems are recovered from a true short-circuit fault.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510" />
