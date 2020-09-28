import requests
import json
import dust_sensor
import gps


def main():
    dust_sensor.turn_off_led()
    url = 'http://localhost:8000/private-station'
    headers = {'content-type': 'application/json'}
    measure_data = dust_sensor.average_measurement()
    print(measure_data)
    while True:

        measure_data = dust_sensor.average_measurement()
        # geg_lon, geg_lan = gps.location()

        payload = {
            "stationName": "Private Station",
            "values": {
                "params": "PM2.5",
                "value": measure_data,
            },
            # "gegrLat": geg_lon,
            # "gegrLon": geg_lon,
        }
        print(measure_data)
        print(payload)
        print(json.dumps(payload))
        # r = requests.post(url, data=json.dumps(payload), headers=headers)


main()
