## Scenario 813
In this scenario, the malicious program injects counterfeit GOOSE packets every minute during normal operation. Such an attack will mislead circuit breakers with fake opening signals to disrupt the power supply. The scenario contains a total of ${\color{red}16}$ sub-scenarios, which are combinations of ${\color{red}four}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Four}$ attack targets**:
   - **a**: disrupting the power supply through Feeder1
   - **b**: disrupting the power supply through Feeder2
   - **c**: disrupting the power supply through Feeder3
   - **d**: disrupting the power supply through Feeder4
2. **${\color{red}Four}$ attack configurations**:
   - **8131**: injecting 40 packets with a fixed heartbeat of 500ms
   - **8132**: injecting 40 packets with a fixed heartbeat of 250ms
   - **8133**: injecting 15 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms
   - **8134**: injecting 10 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms

> <sup>*</sup> The dynamic heartbeats in attack configurations **8133** and **8134** are followed by practical behaviours when a true short-circuit situation occurs.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-GOOSE/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510"/>