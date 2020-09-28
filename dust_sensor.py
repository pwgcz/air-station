import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from gpiozero import LED

'''
Turn of infra led diode after reboot raspberry,
led is connected to transistor, to turn off 
need have high state on PIN16
'''


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
    print(f'{"%.4f" % average} ug/m3')
    return f'{"%.4f" % average} ug/m3'


turn_off_led()
average_measurement()
