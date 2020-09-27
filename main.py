import requests
import time
import json


def main():
    url = 'http://localhost:8000/private-station'
    headers = {'content-type': 'application/json'}
    while True:
        payload = {'some': 'data'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        time.sleep(3600)


if __name__ == '__main__':
    main()
