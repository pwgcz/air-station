import requests
import json
import dust_sensor
import gps
import time


def main():
    dust_sensor.turn_off_led()
    url = 'http://localhost:8000/private-station'
    headers = {'content-type': 'application/json'}
    print('za')
    while True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        measure_data = dust_sensor.average_measurement()
        # geg_lon, geg_lan = gps.location()
        print('okok')
        payload = {
            "stationName": "Private Station",
            "values": {
                "params": "PM2.5",
                "value": measure_data,
                'time': current_time
            },
            # "gegrLat": geg_lon,
            # "gegrLon": geg_lon,
        }
        print(payload)
        print(json.dumps(payload))
        # r = requests.post(url, data=json.dumps(payload), headers=headers)


main()
