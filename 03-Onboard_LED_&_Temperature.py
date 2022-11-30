import machine								# import machine to make use of pins
import utime								# import to allow python to sleep
from machine import Pin						# import the pin library to connect other devices

led = Pin(25, Pin.OUT)						# make pin 25 be the led pin, output pin

tempsensor = machine.ADC(4)					# set sensor to pin 4 analogue to digital
conversion_factor = 3.3 / (65535)			# divide the 3.3v by 16-bits
 
while True:													# while loop to run forever
    reading = tempsensor.read_u16() * conversion_factor 	# read value from sensor 16-bits
    # print("Reading:",reading)
    temperature = 27 - (reading - 0.706)/0.001721			# convert value read to normal celcius
    print("Temperature:",temperature)						# show the value
    utime.sleep(0.5)										# pause for 0.5 seconds
    
    if temperature > 24.0:									# check if temp is greater than 24
        print("Temperature is greater than 24.")			# print message to screen
        led.high()											# turn the internal LED on
        utime.sleep(0.5)									# sleep for 0.5 seconds
    elif temperature < 24.0:								# check if the temp is less than 24
        print("Temperature is less than 24.")				# print message to screen
        led.low()											# turn the LED off
        utime.sleep(0.5)									# sleep for 0.5 seconds
    else:													# catch any other weird conditions
        print("There must have been an error.")				# print message to screen