import RPi.GPIO as GPIO
import requests
from typing import Final


def post_data(x):
    
    # デバイス固有のラベル。理想的なのはデバイスIDから場所を参照する
    label :Final[str] = "九州産業大学15号館2F40"

    # デバイスIDをMacアドレスから取得する
    try: 
        response = requests.post('http://localhost:3000/api/data', json=x)

    except KeyboardInterrupt:
        print("Cleanup")
        GPIO.cleanup()