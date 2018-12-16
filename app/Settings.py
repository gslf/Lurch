import json
from os import path

class Settings:
    ''' 
        Lurch app settings managemant
        This class use JSON file to read/write setting properties
    '''

    def __init__(self):
        '''Settings class contructor with basic configuration
        
        Settings file = settings.data
        Default supplementary heating threshold = 60
        '''
        # Init properties
        self._thresholdMIN = None
        self._suppl_heating = None
        self._suppl_heating_status = None

        self._json_path = 'settings.data'

        # Read json
        if(path.isfile(self._json_path)):
            with open(self._json_path) as json_file:  
                data = json.load(json_file)

            # Set saved properties 
            self.thresholdMIN = data['thresholdMIN']
            self.suppl_heating = data['suppl_heating']
            self.suppl_heating_status = data['suppl_heating_status']
        else:
            # Set default properties 
            self.thresholdMIN = 60
            self.suppl_heating = False
            self.suppl_heating_status = False


    @property
    def thresholdMIN(self):
        ''' Get supplementary heating threshold '''
        return self._thresholdMIN

    @thresholdMIN.setter
    def thresholdMIN(self, value):
        '''Set supplementary heating threshold
        
        Parameters
        ----------
        value : Boolean
            Supplementary heating threshold
        '''
        self._thresholdMIN = value
        self.__save()


    @property
    def suppl_heating(self):
        '''Get supplementary heating status setting '''
        return self._suppl_heating

    @suppl_heating.setter
    def suppl_heating(self, value):
        '''Set supplementary heating current setting 
        
        Parameters
        ----------
        value : Boolean
            Supplementary heating current setting
        '''
        self._suppl_heating = value
        self.__save()

    @property
    def suppl_heating_status(self):
        '''Get supplementary heating current status '''
        return self._suppl_heating_status

    @suppl_heating_status.setter
    def suppl_heating_status(self, value):
        '''Set supplementary heating current status
        
        Parameters
        ----------
        value : Boolean
            Supplementary heating current status
        '''
        self._suppl_heating_status = value
        self.__save()



    def __save(self):
        '''Write settings in settings.data file as JSON '''

        data = {
            'thresholdMIN' : self.thresholdMIN,
            'suppl_heating' : self.suppl_heating,
            'suppl_heating_status' : self.suppl_heating_status
        }

        with open(self._json_path, 'w') as outfile:  
            json.dump(data, outfile)
