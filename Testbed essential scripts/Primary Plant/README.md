## Source codes explanation 
* MATLAB-Simulink/Testbed_v3.slx: Simulink model (source codes) of the primary plant
* interface.cfg: configuration file for interface between Simulink and OpenPLC
* simlink.cpp: the interface program connecting Simulink and goose_subscriber
* run.sh: shell executables file for running all necessary programs under benign behaviours
* multirun.sh: shell executables file for running all necessary programs under multiple malicious behaviours
* src/Benign/goose_subscriber_*.c: API of GOOSE subscriber based on libiec61850 for benign behaviours
* src/Benign/sv?_publisher.c: API of SV publisher based on libiec61850 for benign behaviours
* src/Malicious/goose_subscriber_*.c: API of GOOSE subscriber based on libiec61850 for Malicious behaviours
* src/Malicious/sv?_publisher_*.c: API of SV publisher based on libiec61850 for Malicious behaviours

## Executable files explanaiton
* simlink: executable file of "simlink.cpp"
* bin/goose_subscriber_*: executable file of "goose_subscriber_*.c"
* bin/sv?_publisher_*: executable file of "sv?_publisher_*.c"

## System logs
* TripRecord/*.csv: CB status records and SV measurement records from different IEDs.