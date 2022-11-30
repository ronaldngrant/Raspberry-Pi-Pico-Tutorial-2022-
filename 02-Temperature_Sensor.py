import machine								# import machine to make use of pins
import utime								# import to allow python to sleep
 
tempsensor = machine.ADC(4)					# set sensor to pin 4 analogue to digital
conversion_factor = 3.3 / (65535)			# divide the 3.3v by 16-bits
 
while True:													# while loop to run forever
    reading = tempsensor.read_u16() * conversion_factor 	# read value from sensor 16-bits
    print("Reading:",reading)
    temperature = 27 - (reading - 0.706)/0.001721			# convert value read to normal celcius
    print("Temperature:",temperature)						# show the value
    utime.sleep(0.5)										# pause for 0.5 seconds
    
    
# 27 degrees Celsius delivers a voltage of 0.706V
# convert the temp we get to volts
# fahrenheit_degrees = celsius_degrees * 9 / 5 + 32
# this is not my code, i found it online and edited it.