## Scenario 871
In this scenario, the malicious program deletes the first 40 GOOSE packets containing tripping signals when a short-circuit fault happens. Such an attack will delay the predefined safety protection for almost 35 seconds. The scenario contains a total of ${\color{red}four}$ sub-scenarios and each sub-scenario has one particular attack target.

**QUTZS_GOOSE.csv extracts all GOOSE features of all GOOSE packets from the raw network traffic**

**QUTZS_SV.csv extracts all SV features of all SV packets from the raw network traffic**

**QUTZS_final.csv merges both GOOSE and SV features based on packet recieve timestamp, and most importantly labels each merged sample based on 55 types of behaviours<sup>*</sup>**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: delaying the safety protection when a short-circuit fault happens in Fault_66bus1
   - **b**: delaying the safety protection when a short-circuit fault happens in Fault_XFMR1
   - **c**: delaying the safety protection when a short-circuit fault happens in Fault_66bus2
   - **d**: delaying the safety protection when a short-circuit fault happens in Fault_XFMR2

> <sup>*</sup> Since malicious program only deletes the legitimate GOOSE packets and the remain GOOSE packets are non-malicious, so no sample is labelled as 871. However, from the 35-second heartbeat, it can be easily detected as abnormal behaviour.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510" />
