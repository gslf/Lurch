import json
from os import path

class Settings:
    ''' 
        Lurch app settings managemant
        This class use JSON file to read/write setting properties
    '''

    def __init__(self):
        # Init properties
        self._thresholdMAX = None
        self._thresholdMIN = None
        self._json_path = 'settings.data'

        # Read json
        if(path.isfile(self._json_path)):
            with open(self._json_path) as json_file:  
                data = json.load(json_file)

            # Set saved properties 
            self.thresholdMAX = data['thresholdMAX']
            self.thresholdMIN = data['thresholdMIN']
        else:
            # Set default properties 
            self.thresholdMAX = 40
            self.thresholdMIN = 60

    @property
    def thresholdMAX(self):
        ''' Maximum temperature for supplementary heating '''
        return self._thresholdMAX

    @thresholdMAX.setter
    def thresholdMAX(self, value):
        self._thresholdMAX = value
        self.__save()


    @property
    def thresholdMIN(self):
        ''' Minimum temperature for supplementary heating '''
        return self._thresholdMIN

    @thresholdMIN.setter
    def thresholdMIN(self, value):
        self._thresholdMIN = value
        self.__save()

    def __save(self):
        ''' Write settings in settings.data file as JSON '''

        data = {
            'thresholdMIN' : self.thresholdMIN,
            'thresholdMAX' : self.thresholdMAX
        }

        with open(self._json_path, 'w') as outfile:  
            json.dump(data, outfile)