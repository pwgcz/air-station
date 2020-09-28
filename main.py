
import json
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from gpiozero import LED


def turn_off_led():
    led = LED('GPIO16')
    led.on()


def measurement():
    led = LED('GPIO16')
    i2c = busio.I2C(board.SCL, board.SDA)

    ads = ADS.ADS1115(i2c)
    chan0 = AnalogIn(ads, ADS.P0)

    led.off()
    time.sleep(.00028)
    raw_data = chan0.voltage
    led.on()

    data = raw_data * 500
    return data


def average_measurement():
    measure_list = []
    for i in range(10):
        measure_list.append(measurement())

    average = sum(measure_list) / len(measure_list)

    return f'{"%.4f" % average} ug/m3'


def main():
    turn_off_led()
    # url = 'http://localhost:8000/private-station'
    # headers = {'content-type': 'application/json'}
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
        print(measure_data)
        print(payload)
        print(json.dumps(payload))
        # r = requests.post(url, data=json.dumps(payload), headers=headers)
        time.sleep(3)


main()
