## Scenario 811
In this scenario, the malicious program injects counterfeit GOOSE packets every minute during normal operation. Such an attack will mislead circuit breakers with fake opening signals to disrupt the power supply. The scenario contains a total of eight sub-scenarios, which are divided into:
1. **Two attack targets**: Transformer 1 and Transformer 2
2. **Four attack configurations**:
   - A) injecting 40 packets with a fixed heartbeat of 500ms;
   - B) injecting 40 packets with a fixed heartbeat of 250ms;
   - C) inject 15 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms; and
   - D) inject 10 packets with dynamic heartbeats<sup>*</sup> of 1, 4, 16, 64, 256, 1000, 1000, ..., 1000ms.

> <sup>*</sup> The dynamic heartbeats in attack configurations C and D are followed by practical behaviours when a true short-circuit situation occurs.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose**
