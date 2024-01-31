## Scenario 831
In this scenario, the malicious program injects counterfeit GOOSE packets when a short-circuit fault happens. Such an attack will mislead circuit breakers with fake closing signals to disable safety protection. The scenario contains a total of ${\color{red}16}$ sub-scenarios, which are combinations of ${\color{red}four}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: disrupting the safety protection when a short-circuit fault happens in Fault_66bus1
   - **b**: disrupting the safety protection when a short-circuit fault happens in Fault_XFMR1
   - **c**: disrupting the safety protection when a short-circuit fault happens in Fault_66bus2
   - **d**: disrupting the safety protection when a short-circuit fault happens in Fault_XFMR2
2. **${\color{red}Four}$ attack configurations**:
   - **8311**: injecting packets with a fixed heartbeat of 500ms when a short-circuit fault happened
   - **8312**: injecting only 40 packets with a fixed heartbeat of 500ms when a short-circuit fault happened
   - **8313**: injecting packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms when a short-circuit fault happened
   - **8314**: injecting only 30 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms when a short-circuit fault happened

> <sup>*</sup> The dynamic heartbeats in attack configurations **8313** and **8314** are followed by practical behaviours when power systems are recovered from a true short-circuit fault.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510" />
