## Scenario 811
In this scenario, the malicious program injects counterfeit GOOSE packets every minute during normal operation. Such an attack will mislead circuit breakers with fake opening signals to disrupt the power supply. The scenario contains a total of ${\color{red}eight}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS_GOOSE.csv extracts all GOOSE features of all GOOSE packets from the raw network traffic**

**QUTZS_SV.csv extracts all SV features of all SV packets from the raw network traffic**

**QUTZS_final.xlsx merges both GOOSE and SV features based on packet arrival timestamp, and most importantly labels each merged sample based on 32 types of behaviours**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: disrupting the power supply around Three-Phase Transformer 1 
   - **b**: disrupting the power supply around Three-Phase Transformer 2
2. **${\color{red}Four}$ attack configurations**:
   - **8111**: injecting 40 packets with a fixed heartbeat of 500ms
   - **8112**: injecting 40 packets with a fixed heartbeat of 250ms
   - **8113**: injecting 15 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms
   - **8114**: injecting 10 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms

> <sup>*</sup> The dynamic heartbeats in attack configurations **8113** and **8114** are followed by practical behaviours when a true short-circuit situation occurs.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-GOOSE/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />