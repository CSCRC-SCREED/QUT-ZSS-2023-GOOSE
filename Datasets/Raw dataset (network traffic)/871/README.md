## Scenario 871
In this scenario, the malicious program deletes the first 40 GOOSE packets containing tripping signals when a short-circuit fault happens. Such an attack will delay the predefined safety protection for almost 35 seconds. The scenario contains a total of ${\color{red}four}$ sub-scenarios and each sub-scenario has one particular attack target.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: delaying the safety protection when a short-circuit fault happens in Fault_66bus1
   - **b**: delaying the safety protection when a short-circuit fault happens in Fault_XFMR1
   - **c**: delaying the safety protection when a short-circuit fault happens in Fault_66bus2
   - **d**: delaying the safety protection when a short-circuit fault happens in Fault_XFMR2

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-GOOSE/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
