import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor

class Raspberry:
    '''
        Raspnerry PI Hardware managemant
        DS18B20 Temperature sensor
        5v Rele switch
    '''

    def __init__(self):
        # Create sensor object
        self.temp_sensor = W1ThermSensor()

        # Setup GPIO
        self.rele = 21
        GPIO.setmode(GPIO.BCM)



    def getTemp(self):
        ''' Read temperature from sensor '''

        return self.temp_sensor.get_temperature()



    def switchSupplementaryHeating(self,status):
        ''' Switch 5v Rele status with 21 GPIO pin '''

        if status:
            print("Supplementary Heating ON")
            GPIO.setup(self.rele,GPIO.OUT)
        else:
            print("Supplementary Heating OFF")
            GPIO.setup(self.rele,GPIO.IN)
