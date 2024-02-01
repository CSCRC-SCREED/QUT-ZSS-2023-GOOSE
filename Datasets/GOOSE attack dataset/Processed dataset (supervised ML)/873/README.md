## Scenario 873
In this scenario, the malicious program deletes the first 40 GOOSE packets containing tripping signals when a short-circuit fault happens. Such an attack will delay the predefined safety protection for almost 35 seconds. The scenario contains a total of ${\color{red}four}$ sub-scenarios and each sub-scenario has one particular attack target.

**QUTZS_GOOSE.csv extracts all GOOSE features of all GOOSE packets from the raw network traffic**

**QUTZS_SV.csv extracts all SV features of all SV packets from the raw network traffic**

**QUTZS_final.csv merges both GOOSE and SV features based on packet receive timestamp, and most importantly labels each merged sample based on 55 types of behaviours<sup>*</sup>**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: delaying the safety protection when a short-circuit fault happens in Fault_FDR1
   - **b**: delaying the safety protection when a short-circuit fault happens in Fault_FDR2
   - **c**: delaying the safety protection when a short-circuit fault happens in Fault_FDR3
   - **d**: delaying the safety protection when a short-circuit fault happens in Fault_FDR4

> <sup>*</sup> Since the malicious program only deletes the legitimate GOOSE packets and the remaining GOOSE packets are non-malicious, so no sample is labelled as 871. However, from the 35-second heartbeat, it can be easily detected as an abnormal behaviour.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510" />
