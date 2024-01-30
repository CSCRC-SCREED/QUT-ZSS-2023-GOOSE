## Scenario 812
In this scenario, the malicious program injects counterfeit GOOSE packets every minute during normal operation. Such an attack will mislead circuit breakers with fake opening signals to disrupt the power supply. The scenario contains a total of eight sub-scenarios, which are combinations of **two attack targets** and **four attack configurations**.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose**

1. **Two attack targets**: 
   - **a**: disrupting the power supply through the CB1_22KV; and 
   - **b**: disrupting the power supply through the CB3_22KV
2. **Four attack configurations**:
   - **8121**: injecting 40 packets with a fixed heartbeat of 500ms;
   - **8122**: injecting 40 packets with a fixed heartbeat of 250ms;
   - **8123**: injecting 15 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms; and
   - **8124**: injecting 10 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms.

> <sup>*</sup> The dynamic heartbeats in attack configurations **8123** and **8124** are followed by practical behaviours when a true short-circuit situation occurs.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510" />