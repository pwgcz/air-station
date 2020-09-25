import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from gpiozero import LED


def measure():
    led =LED('GPIO16')
    led.on()
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    chan0 = AnalogIn(ads, ADS.P0)

    led.off()
    time.slleep(.00028)
    raw_data = chan0.voltage
    led.on()

    data = raw_data*500
    return f'{"%.2f" % data} ug/m3'

