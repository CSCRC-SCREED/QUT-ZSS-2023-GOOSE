## Processed dataset
For each scenario/sub-scenario, the dataset contains the following three datasheets: 
1. **QUTZS_GOOSE.csv** extracts all GOOSE features of all GOOSE packets from the raw network traffic
2. **QUTZS_SV.csv** extracts all SV features of all SV packets from the raw network traffic
3. **QUTZS_final.xlsx** merges both GOOSE and SV features, and most importantly labels each row of features based on 32 types of behaviours. For every GOOSE packet (a row of GOOSE features), two SV packets (two rows of SV features, one with APPID "0x4001" and the other with APPID "0x4002") were appended, respectively. For each row of merged features, the packet arrival time of the appended SV packet is closest to the packet arrival time of the GOOSE packet.

> The code snippet for generating QUTZS_final.xlsx is provided in **merge.py**.

> **metadata.xlsx** describes the metadata of each scenario/sub-scenario, including the number of GOOSE packets, SV packets, and samples with particular labels.