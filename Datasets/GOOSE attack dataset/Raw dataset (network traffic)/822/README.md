## Scenario 822
In this scenario, the malicious program modifies original GOOSE packets every minute during normal operation. Such an attack will mislead circuit breakers with fake opening signals to disrupt the power supply. The scenario contains a total of ${\color{red}four}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}two}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Two}$ attack targets**:
   - **a**: disrupting the power supply through the CB1_22KV
   - **b**: disrupting the power supply through the CB3_22KV
2. **${\color{red}Two}$ attack configurations**:
   - **8221**: altering only the allData field of 10 packets; heartbeat, stNum, and sqNum remain unchanged
   - **8222**: altering relevant fields of 10 packets, including dynamic heartbeats (1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms), stNum++, sqNum reset to 0<sup>*</sup>

> <sup>*</sup> The modifications of those three fields in attack configuration **8222** are followed by practical behaviours when a true short-circuit situation occurs.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510"/>