from machine import Pin				# import the pin library to connect other devices
import utime						# import time librarry to sleep

GreenLED = Pin(16, Pin.OUT)			# make pin 25 be the led pin, output pin
RedLED = Pin(17, Pin.OUT)			# make pin 25 be the led pin, output pin

GreenLED.toggle()					# turn green led on
RedLED.toggle()						# turn red led on