## Source codes explanation 
* interface.cfg: configuration file for the interface between Simulink and OpenPLC
* simlink.cpp: the interface program connecting Simulink and goose_subscriber
* run.sh: shell executables file for running all necessary programs under benign behaviours
* multirun.sh: shell executables file for running all necessary programs under multiple malicious behaviours
* src/Benign/goose_publisher_*.c: API of GOOSE publisher based on libiec61850 for benign behaviours
* src/Benign/sv_subscriber_example.c: API of SV subscriber based on libiec61850 for benign behaviours
* src/Malicious/goose_publisher_*.c: API of GOOSE publisher based on libiec61850 for Malicious behaviours
* src/Malicious/sv_subscriber_example.c: API of SV subscriber based on libiec61850 for Malicious behaviours

## Executable files explanation
* simlink: executable file of "simlink.cpp"
* bin/goose_publisher_\*: executable file of "goose_publisher_\*.c"
* bin/sv_subscriber: executable file of "sv_subscriber_example.c"

## System logs
* TripRecord/*.csv: CB status records and SV measurement records in this IED.
