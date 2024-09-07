import machine  # type: ignore
import time

# LED Pin(緑色)
green_led = machine.Pin(14, machine.Pin.OUT)
# LED Pin(黄色)
yellow_led = machine.Pin(13, machine.Pin.OUT)
# LED Pin(青色)
blue_led = machine.Pin(12, machine.Pin.OUT)
# LED Pin(赤色)
red_led = machine.Pin(11, machine.Pin.OUT)

# Slide Switch Pin
sw = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    # swが押されたらLEDを点灯
    if sw.value() == 0:
        green_led.value(1)
        yellow_led.value(1)
        blue_led.value(1)
        red_led.value(1)
    # swが離されたらLEDを消灯
    else:
        green_led.value(0)
        yellow_led.value(0)
        blue_led.value(0)
        red_led.value(0)
    time.sleep(0.1)
