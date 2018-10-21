import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor

class Raspberry:
    '''
        Raspnerry PI Hardware managemant
        DS18B20 Temperature sensor
        5v Rele switch
    '''

    __init__(self):
        # Create sensor object
        temp_sensor = W1ThermSensor()

        # Setup GPIO
        rele = 21
        GPIO.setmode(GPIO.BCM)



    def getTemp(self):
        ''' Read temperature from sensor '''

        return temp_sensor.get_temperature()



    def switchSupplementaryHeating(self,status):
        ''' Switch 5v Rele status with 21 GPIO pin ''''

        if status:
            GPIO.setup(rele,GPIO.OUT)
        else:
            GPIO.setup(rele,GPIO.IN)