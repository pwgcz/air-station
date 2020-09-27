import serial

port = "/dev/ttyS0"


def decode(coord):
    v = coord.split(".")
    head = v[0]
    tail = v[1]
    deg = head[0:-2]
    minim = head[-2:]

    return deg + minim + "." + tail


def parseGPS(data):
    print(data[0:6])
    data.decode()
    if data[0:6] == "$GPGGA":
        print(str(data))
        print(type(data))
        s = data.split(",")

        if s[7] == '0':
            print("no satelite data available")
            return None
        time = s[1][0:2] + ":" + s[1][2:4] + ":" + s[1][4:6]
        lat = decode(s[2])
        dir_lat = s[3]
        lon = decode(s[4])
        dir_lon = s[5]
        print(f'Lat:{lat}({dir_lat})  Lon:{lon}({dir_lon}) time: {time}')


ser = serial.Serial(port, baudrate=9600, timeout=0.5)
while True:
    data = ser.readline()
    parseGPS(data)