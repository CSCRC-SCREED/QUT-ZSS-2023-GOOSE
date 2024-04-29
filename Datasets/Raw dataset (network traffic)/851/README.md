## Scenario 851
In this scenario, the malicious program injects counterfeit GOOSE packets when a short-circuit fault happens. Such an attack will mislead other irrelevant circuit breakers with fake opening signals to deteriorate the impacts of the short-circuit fault. The scenario contains a total of ${\color{red}16}$ sub-scenarios, which are combinations of ${\color{red}four}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: disrupting the power supply through Transformer 2 when a short-circuit fault happens in Fault_66bus1
   - **b**: disrupting the power supply through Transformer 2 when a short-circuit fault happens in Fault_XFMR1
   - **c**: disrupting the power supply through Transformer 1 when a short-circuit fault happens in Fault_66bus2
   - **d**: disrupting the power supply through Transformer 1 when a short-circuit fault happens in Fault_XFMR2
2. **${\color{red}Four}$ attack configurations**:
   - **8511**: when a short-circuit fault happens, injecting packets with a fixed heartbeat of 500ms until the associated circuit breakers start to reset (the fault is eliminated and the systems recover)
   - **8512**: when a short-circuit fault happens, injecting only 40 packets with a fixed heartbeat of 500ms
   - **8513**: when a short-circuit fault happens, injecting packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms until the associated circuit breakers start to reset (the fault is eliminated and the systems recover)
   - **8514**: when a short-circuit fault happens, injecting only 30 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms

> <sup>*</sup> The dynamic heartbeats in attack configurations **8513** and **8514** are followed by practical behaviours when a true short-circuit fault occurs.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-GOOSE/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
