## Scenario 832
In this scenario, the malicious program injects counterfeit GOOSE packets when a short-circuit fault happens. Such an attack will mislead circuit breakers with fake closing signals to disable safety protection. The scenario contains a total of ${\color{red}eight}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: disrupting the safety protection when a short-circuit fault happens in Fault_22bus1
   - **b**: disrupting the safety protection when a short-circuit fault happens in Fault_22bus2
2. **${\color{red}Four}$ attack configurations**:
   - **8321**: injecting packets with a fixed heartbeat of 500ms when a short-circuit fault happens
   - **8322**: injecting only 40 packets with a fixed heartbeat of 500ms when a short-circuit fault happens
   - **8323**: injecting packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms when a short-circuit fault happens
   - **8324**: injecting only 30 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms when a short-circuit fault happens

> <sup>*</sup> The dynamic heartbeats in attack configurations **8323** and **8324** are followed by practical behaviours when power systems are recovered from a true short-circuit fault.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-GOOSE/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
