## Scenario 862
In this scenario, the malicious program subscribes to all types of SV messages illegitimately and publishes tripping signals even when a short-circuit fault happens in an irrelevant location. Such an attack will mislead other irrelevant circuit breakers with opening signals to deteriorate the impacts of the short-circuit fault. The scenario contains a total of ${\color{red}four}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}two}$ attack configurations.

> In this scenario, there is an approximately 30-second DMZ period. The DMZ here represents a buffer between the 1st attack cycle and the 2nd attack cycle. The data within the DMZ period is valid and shows a type of fault-free behaviours that systems were recovered from a real/fabricated fault. Therefore, data within the DMZ period was labelled as **0**.

**QUTZS_GOOSE.csv extracts all GOOSE features of all GOOSE packets from the raw network traffic**

**QUTZS_SV.csv extracts all SV features of all SV packets from the raw network traffic**

**QUTZS_final.xlsx merges both GOOSE and SV features based on packet arrival timestamp, and most importantly labels each merged sample based on 32 types of behaviours**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: disrupting the power supply through CB3_22KV when a short-circuit fault happens in Fault_22bus1
   - **b**: disrupting the power supply through CB1_22KV when a short-circuit fault happens in Fault_22bus2
2. **${\color{red}Two}$ attack configurations**:
   - **8621**: when a short-circuit fault happens, an irrelevant IED (compromised with malicious program) publishes packets containing tripping signals until the fault is eliminated and the systems recover
   - **8622**: when a short-circuit fault happens, an irrelevant IED (compromised with malicious program) publishes the first 30 packets containing tripping signals, and the rest packets containing non-tripping signals

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-GOOSE/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
