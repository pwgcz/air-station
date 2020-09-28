import requests
import json
import time
from dust_sensor import average_measurement, turn_off_led


def main():
    turn_off_led()

    url = 'http://127.0.0.1:5000/private-station'
    headers = {'content-type': 'application/json'}
    measure_data = average_measurement()
    print(measure_data)

    while True:

        measure_data = average_measurement()
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
        print(json.dumps(payload))
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        time.sleep(3)


if __name__ == "__main__":
    main()
