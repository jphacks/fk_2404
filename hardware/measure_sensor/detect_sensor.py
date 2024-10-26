# coding: utf-8

import spidev
import RPi.GPIO as GPIO
import time

# 閾値の設定（今回は音再生部分は使わないので不要）
threshold = 500

# GPIOの初期設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# SPIの設定
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000
spi.bits_per_word = 8

dummy = 0xff
start = 0x47
sgl = 0x20
ch0 = 0x00
msbf = 0x08

# センサー値を取得する関数
def measure(ch):
    ad = spi.xfer2([(start + sgl + ch + msbf), dummy])
    val = ((ad[0] & 0x03) << 8) + ad[1]
    return val

# メインループ
try:
    while True:
        time.sleep(1)  # 1秒間隔でデータを取得

        GPIO.output(22, True)
        time.sleep(0.003)

        ch0_val = measure(ch0)
        Val = 1023 - ch0_val
        time.sleep(0.002)
        GPIO.output(22, False)
        
        GPIO.output(17, True)
        time.sleep(0.008)
        GPIO.output(17, False)

        print(f"電圧値: {Val}")

except KeyboardInterrupt:
    pass

# リソースを解放
spi.close()
GPIO.cleanup()
