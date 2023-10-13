import os
import pymysql
import json
path = './CAB_ZBBB_VATPRC/All/ASRs'
grpath = './CAB_ZBBB_VATPRC/Gr_TWR'
twrpath = './CAB_ZBBB_VATPRC/Tower'
dirs = os.listdir( path )
def FindAirport(ICAO):
    # TODO: Find Airport Elevation
def startgr():
    for file in dirs:
        if "TWR" in file:
            airport = file.split('_')[0]
            alt = FindAirport(airport)
            if alt != None:
                gr = f'''DisplayTypeName:Ground Radar display
DisplayTypeNeedRadarContent:0
DisplayTypeGeoReferenced:1
PLUGIN:TopSky plugin:NoDraw:1
PLUGIN:Ground Radar plugin:GroundMode:{airport}
PLUGIN:Ground Radar plugin:AirportElevation:{alt}
PLUGIN:Ground Radar plugin:AirportRadius:3
'''
                with open(f'{path}/{file}', 'r') as f:
                    asr = f.read()
                with open(f'{path}/GR_{airport}.asr', 'w') as f:
                    f.write(f"{asr}{gr}")
                with open(f'{twrpath}/{airport}_TWR.prf', 'r') as f:
                    prfdata = f.read()
                with open(f'{grpath}/GR_{airport}.prf', 'w') as f:
                    f.write(prfdata.replace(f"{airport}_TWR.asr",f"GR_{airport}.asr"))
def grparking():
    disc = os.listdir( grpath )
    with open("stands.json","r") as f:
        data = f.read()
        data = json.loads(data)
    for flie in disc:
        ICAO = flie.replace(".prf","").replace("GR_","")
        try:
            parsed_data = data[ICAO]
            for key, value in parsed_data.items():
                print("机位名字:", key)
                print(parsed_data[key])
                with open("GR_STAND.txt","a") as f:
                    f.write(f"STAND:{ICAO}:{key}:{parsed_data[key][0]}:{parsed_data[key][1]}:36\n")
        except:
            pass
if __name__ == '__main__':
    startgr()
    # grparking()




