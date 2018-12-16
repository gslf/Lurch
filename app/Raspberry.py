import logging
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor

class Raspberry:
    '''Raspberry PI Hardware managemant
    
    Involved hardware:
        - DS18B20 Temperature sensor
        - 5v Rele switch
    '''

    def __init__(self):
        '''Raspberry class constructor with a basic setup'''
        # Create sensor object
        self.temp_sensor = W1ThermSensor()

        # Setup GPIO
        self.rele = 21
        GPIO.setmode(GPIO.BCM)



    def getTemp(self):
        ''' A function that read temperature from sensor '''
        return self.temp_sensor.get_temperature()



    def switchSupplementaryHeating(self,status):
        ''' A function that turn on/off the supplementary heating rele

        Involved hardware:
            Switch 5v Rele status on 21 GPIO pin 
        
        Parameters
        ----------
        status : Boolean
            Requested status of supplementaru heating
        '''

        if status:
            logging.info("Supplementary Heating ON")
            GPIO.setup(self.rele,GPIO.OUT)
        else:
            logging.info("Supplementary Heating OFF")
            GPIO.setup(self.rele,GPIO.IN)
