## Scenario 811
In this scenario, the malicious program injects counterfeit GOOSE packets every one minutes during normal operation. Such attack will mislead circuit breakers with fake opening signals to disrupt power supply. The scenario contains a total of eight sub-scenarios, which are divided into:
1. **Two attack targets**: Transformer 1 and Transformer 2
2. **Four attack configurations**: A) injecting 40 packets with a fixed heartbeat of 500ms; B) injecting 40 packets with a fixed heartbeat of 250ms; C) inject 15 packets with dynamic heartbeats<sub>\*</sub> of 1, 4, 16, 64, 256, 1000, 1000, 1000ms, ...; and D) inject 10 packets with dynamic heartbeats of 1, 4, 16, 64, 256, 1000, 1000, 1000ms, ...

> \*: the dynamic heartbeats in attack configurations C and D are followed by the practical behaviours when a true short-circuit situation occurs.

** QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose **