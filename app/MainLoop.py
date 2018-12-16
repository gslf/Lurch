import time
from threading import Thread

class MainLoop:
    '''
        Lurch main managemant loop
        This class starts a thread that checks and manage the hardware every 30 seconds
    '''

    def __init__(self, settings, raspberry):
        '''
        MainLoop class contructor
        
        Parameters
        ----------

        settings : Settings 
            App settings manager

        raspberry : Raspberry 
            Hardware manager

        '''

        self.running = False
        self.loop = None

        self.settings = settings
        self.raspberry = raspberry

    def __main_loop(self):

        while self.running:
            # Get current temperature
            current_temp = self.raspberry.getTemp()

            # Manage supplementary heating
            if current_temp <= self.settings.thresholdMIN and self.settings.suppl_heating :
                self.raspberry.switchSupplementaryHeating(True)
                self.settings.suppl_heating_status = True
            else :
                self.raspberry.switchSupplementaryHeating(False)
                self.settings.suppl_heating_status = False
            
            # Repeat main loop after 30 seconds
            time.sleep(30)


    def updateSettings(self,settings):
        '''Update app settings object

        Parameters
        ----------
        settings : Settings
            New settings object
        '''
        self.settings = settings

    def updateRaspberry(self, raspberry):
        '''Update hardware manager object

        Parameters
        ----------
        raspberry : Raspberry
            New raspberry object
        '''
        self.raspberry = raspberry

    def start(self):
        '''Start the main loop in a Thread'''
        self.running = True
        self.loop = Thread(target=self.__main_loop)
        self.loop.start()

    def stop(self):
        '''Stop main loop Thread'''
        self.raspberry.switchSupplementaryHeating(False)
        self.settings.suppl_heating_status = False
        self.running = False
        self.loop = None
