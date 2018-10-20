import time
from threading import Thread

class MainLoop:
    '''
        Lurch main managemant loop
        This class starts a thread that checks and manage the hardware every 30 seconds
    '''

    def __init__(self, settings, raspberry):
        self.running = False
        self.loop = None

        self.settings = settings
        self.raspberry = raspberry

    def __main_loop(self):
        while self.running:
            current_temp = self.raspberry.getTemp()

            if current_temp <= self.settings.thresholdMIN and self.settings.suppl_heating :
                self.raspberry.switchSupplementaryHeating(True)
                self.settings.suppl_heating_status = True
            else :
                self.raspberry.switchSupplementaryHeating(False)
                self.settings.suppl_heating_status = False

            time.sleep(30)


    def updateSettings(self,settings):
        self.settings = settings

    def updateRaspberry(self, raspberry):
        self.raspberry = raspberry

    def start(self):
        self.running = True
        self.loop = Thread(target=self.__main_loop)
        self.loop.start()

    def stop(self):
        self.running = False
        self.loop = None