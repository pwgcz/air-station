import serial

port = "/dev/ttyS0"


def decimal_format(coordinate):
    raw_data = coordinate.split('.')
    degree = raw_data[0][0:-2]
    minutes = raw_data[0][-2:] + raw_data[1]
    decimal_minutes = str(float(minutes) * 10 / 6)
    return degree + '.' + decimal_minutes


def parse_gps(data):
    decoded_data = data.decode()
    if decoded_data[0:6] == "$GPGGA":
        s = decoded_data.split(",")

        if s[7] == '0':
            print("no satelite data available")
            return None
        raw_time = s[1]
        hour = slice(0, 2)
        minutes = slice(2, 4)
        seconds = slice(4, 6)
        time = raw_time[hour] + ":" + raw_time[minutes] + ":" + raw_time[seconds]
        raw_lat = s[2]
        raq_lon = s[4]
        direction_lat = s[3]
        direction_lon = s[5]
        geg_lat = decimal_format(raw_lat)
        geg_lon = decimal_format(raq_lon)
        print(f'Lat:{geg_lat}--({direction_lat})  Lon:{direction_lon}--({geg_lon}) time:{time} ')


ser = serial.Serial(port, baudrate=9600, timeout=0.5)
while True:
    data = ser.readline()
    parse_gps(data)
