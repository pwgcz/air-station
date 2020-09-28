import serial

port = "/dev/ttyS0"


def decimal_format(coordinate):
    raw_data = coordinate.split('.')
    degree = raw_data[0][0:-2]
    minutes = raw_data[0][-2:] + raw_data[1]
    decimal_minutes = str(float('.' + minutes) * 100 / 6).replace('.', '')
    if degree.startswith('0'):
        degree = degree.replace('0', '', 1)
    return degree + '.' + decimal_minutes


def parse_gps(serial_data: bytes):
    decoded_data = serial_data.decode()
    if decoded_data[0:6] == "$GPGGA":
        s = decoded_data.split(",")

        if s[7] == '0':
            # cant reach data
            return None
        raw_lat = s[2]
        raq_lon = s[4]
        geg_lat = decimal_format(raw_lat)
        geg_lon = decimal_format(raq_lon)
        print(geg_lon, geg_lat)
        return geg_lon, geg_lat


while True:
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    serial_response = ser.readline()
    parse_gps(serial_response)
