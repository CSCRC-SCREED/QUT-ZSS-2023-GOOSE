## Scenario 853
In this scenario, the malicious program injects counterfeit GOOSE packets when a short-circuit fault happens. Such an attack will mislead other irrelevant circuit breakers with fake opening signals to deteriorate the impacts of the short-circuit fault. The scenario contains a total of ${\color{red}16}$ sub-scenarios, which are combinations of ${\color{red}four}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: disrupting the power supply through Feeder2 when a short-circuit fault happens in Fault_FDR1
   - **b**: disrupting the power supply through Feeder1 when a short-circuit fault happens in Fault_FDR2
   - **c**: disrupting the power supply through Feeder4 when a short-circuit fault happens in Fault_FDR3
   - **d**: disrupting the power supply through Feeder3 when a short-circuit fault happens in Fault_FDR4
2. **${\color{red}Four}$ attack configurations**:
   - **8531**: when a short-circuit fault happens, injecting packets with a fixed heartbeat of 500ms until the associated circuit breakers start to reset (the fault is eliminated and the systems recover)
   - **8532**: when a short-circuit fault happens, injecting only 40 packets with a fixed heartbeat of 500ms
   - **8533**: when a short-circuit fault happens, injecting packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms until the associated circuit breakers start to reset (the fault is eliminated and the systems recover)
   - **8534**: when a short-circuit fault happens, injecting only 30 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms

> <sup>*</sup> The dynamic heartbeats in attack configurations **8533** and **8534** are followed by practical behaviours when a true short-circuit fault occurs.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510" />
