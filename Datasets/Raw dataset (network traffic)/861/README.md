## Scenario 861
In this scenario, the malicious program subscribes to all types of SV messages illegitimately and publishes tripping signals even when a short-circuit fault happens in an irrelevant location. Such an attack will mislead other irrelevant circuit breakers with opening signals to deteriorate the impacts of the short-circuit fault. The scenario contains a total of ${\color{red}eight}$ sub-scenarios, which are combinations of ${\color{red}four}$ attack targets and ${\color{red}two}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: disrupting the power supply through Transformer 1 when a short-circuit fault happens in Fault_66bus2
   - **b**: disrupting the power supply through Transformer 1 when a short-circuit fault happens in Fault_XFMR2
   - **c**: disrupting the power supply through Transformer 2 when a short-circuit fault happens in Fault_66bus1
   - **d**: disrupting the power supply through Transformer 2 when a short-circuit fault happens in Fault_XFMR1
2. **${\color{red}Two}$ attack configurations**:
   - **8611**: when a short-circuit fault happens, an irrelevant IED (compromised with malicious program) publishes packets containing tripping signals until the fault is eliminated and the systems recover
   - **8612**: when a short-circuit fault happens, an irrelevant IED (compromised with malicious program) publishes the first 30 packets containing tripping signals, and the rest packets containing non-tripping signals

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023/blob/main/PrimaryPlant.jpg" alt="" width="800" height="510" />
