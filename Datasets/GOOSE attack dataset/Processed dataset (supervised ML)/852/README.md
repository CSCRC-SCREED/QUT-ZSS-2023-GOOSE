## Scenario 852
In this scenario, the malicious program injects counterfeit GOOSE packets when a short-circuit fault happens. Such an attack will mislead other irrelevant circuit breakers with fake opening signals to deteriorate the impacts of the short-circuit fault. The scenario contains a total of ${\color{red}eight}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS_GOOSE.csv extracts all GOOSE features of all GOOSE packets from the raw network traffic**

**QUTZS_SV.csv extracts all SV features of all SV packets from the raw network traffic**

**QUTZS_final.csv merges both GOOSE and SV features based on packet recieve timestamp, and most importantly labels each merged sample based on 32 types of behaviours**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: disrupting the power supply through CB3-22KV when a short-circuit fault happens in Fault_22bus1
   - **b**: disrupting the power supply through CB1-22KV when a short-circuit fault happens in Fault_22bus2
2. **${\color{red}Four}$ attack configurations**:
   - **8521**: when a short-circuit fault happens, injecting packets with a fixed heartbeat of 500ms until the associated circuit breakers start to reset (the fault is eliminated and the systems recover)
   - **8522**: when a short-circuit fault happens, injecting only 40 packets with a fixed heartbeat of 500ms
   - **8523**: when a short-circuit fault happens, injecting packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms until the associated circuit breakers start to reset (the fault is eliminated and the systems recover)
   - **8524**: when a short-circuit fault happens, injecting only 30 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms

> <sup>*</sup> The dynamic heartbeats in attack configurations **8523** and **8524** are followed by practical behaviours when a true short-circuit fault occurs.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510" />
