import machine								# import machine to make use of pins
import utime								# import to allow python to sleep
from machine import Pin

GreenLED = Pin(16, Pin.OUT)					# make pin 16 be the green led pin, output pin
RedLED = Pin(17, Pin.OUT)					# make pin 17 be the red led pin, output pin

tempsensor = machine.ADC(4)					# set sensor to pin 4 analogue to digital
conversion_factor = 3.3 / (65535)			# divide the 3.3v by 16-bits
 
while True:													# while loop to run forever
    reading = tempsensor.read_u16() * conversion_factor 	# read value from sensor 16-bits
    # print("Reading:",reading)
    temperature = 27 - (reading - 0.706)/0.001721			# convert value read to normal celcius
    print("Temperature:",temperature)						# show the value
    utime.sleep(0.5)										# pause for 0.5 seconds
    
    if temperature >=23:									# check temp is above or equal to 23
        print("Green LED")									# print message to shell
        GreenLED.high()										# turn the green led on
        RedLED.low()										# turn the red led off
        
    elif temperature<23:									# check temp is below 23
        print("Red LED")									# print message to shell
        RedLED.high()										# turn red led on
        GreenLED.low()										# turn green led off
        
    else:													# catch anything els ei have not thought of
        print("No LED. Error.")
    

