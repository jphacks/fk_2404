import RPi.GPIO as GPIO
import time
import datetime
import requests
import uuid
from typing import Final

# datatime, label, mac_addr, 
dt_now = datetime.datetime.now()
# デバイス固有のラベル。理想的なのはデバイスIDから場所を参照する
label :Final[str] = "九州産業大学15号館2F40"

# デバイスIDをMacアドレスから取得する
mac_addr = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
                    for ele in range(0, 8 * 6, 8)][::-1])

data = {
    'time':dt_now,
    'label': label,
    'mac_addr':mac_addr 
    }
print(data)

try:    
    response = requests.post('http://localhost:3000/', data)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()