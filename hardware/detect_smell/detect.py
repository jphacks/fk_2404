import spidev
import RPi.GPIO as GPIO
import time
import datetime

from post_data import post_data
GPIO.setwarnings(False)

"""
処理フロー
1. 距離センサーが一定以下の値になる
2. それをトリガーに、臭いセンサーが値を取得開始
3. X 1分間計測(250回)→配列
4. X 標準関数を用いて読み込み、最大値の取得
5. X 基準値(測定開始から1秒後の値) - 最大値 = diff
6. X 正規化
7. X 値に応じてラベル(A-D)までを決定
8. X post_data関数を呼び出し、dataに情報をまとめて辞書型で送信
"""

# 1. 距離センサー

# 2. 臭いセンサー実装部

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # heater
GPIO.setup(22, GPIO.OUT)  # VCC

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000
spi.bits_per_word = 8

dummy = 0xff
start = 0x47
sgl = 0x20
ch0 = 0x00
msbf = 0x08
smell_val = []

def getTime():
    return datetime.datetime.now()

def measure(ch):
    ad = spi.xfer2([(start + sgl + ch + msbf), dummy])
    val = ((ad[0] & 0x03) << 8) + ad[1]
    return val

# 評価を決定する関数
def get_grade(score):
    if score <= 15:
        return "D"
    elif score <= 25:
        return "C"
    elif score <= 35:
        return "B"
    elif score <= 40:
        return "A"
    elif score <= 45:
        return "AA"
    else:
        return "AAA"

try:
    dt_begin = getTime()  # Capture the start time
    for i in range(250):
        time.sleep(0.237)

        GPIO.output(22, True)
        time.sleep(0.003)

        ch0_val: float = measure(ch0)
        Val = 1023.0 - ch0_val
        time.sleep(0.002)
        GPIO.output(22, False)

        GPIO.output(17, True)
        time.sleep(0.008)
        GPIO.output(17, False)

        print(Val)
        smell_val.append(Val)

except KeyboardInterrupt:
    pass

spi.close()

dt_end = getTime()  # Capture the end time
base_val = smell_val[0]
min_val = min(smell_val)

score = (base_val - min_val)
grade = get_grade(score)

# Post data with dt_begin, dt_end, and grade
data = ({
    "start_time": dt_begin.strftime("%Y-%m-%d %H:%M:%S"),
    "end_time": dt_end.strftime("%Y-%m-%d %H:%M:%S"),
    "label": "九州産業大学15号館2Fトイレ40",
    "grade": grade,
})

post_data(data)