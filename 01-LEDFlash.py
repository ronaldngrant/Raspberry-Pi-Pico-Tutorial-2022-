from machine import Pin				# import the pin library to connect other devices
import utime						# import sleep/pause functionality

led = Pin(25, Pin.OUT)				# make pin 25 be the led pin

#led.toggle()						# turn on or turn off the led

while True:
    led.low()						# turns led off
    utime.sleep(0.3)				# sleep for 0.3 seconds
    led.high()						# turn the led on
    utime.sleep(0.3)				# sleep for 0.3 seconds

