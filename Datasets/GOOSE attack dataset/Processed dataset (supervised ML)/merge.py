import pandas as pd

GOOSEcsv = pd.read_csv('QUTZS_GOOSE.csv')
SVcsv = pd.read_csv('QUTZS_SV.csv')
SV4001 = SVcsv[SVcsv['APPID'] == '0x4001']
SV4002 = SVcsv[SVcsv['APPID'] == '0x4002']

temp = pd.merge_asof(GOOSEcsv, SV4001, on='pkt arrive time', suffixes=('_goose','_sv1'), direction='nearest')
final = pd.merge_asof(temp, SV4002, on='pkt arrive time', suffixes=('_sv1','_sv2'), direction='nearest')
final = final.rename(columns={"MACsrc": "MACsrc_sv2", "MACdst": "MACdst_sv2", "APPID": "APPID_sv2"})
final.to_excel("QUTZS_final.xlsx")
