from flask import Flask
from app.MainLoop import MainLoop
from app.Settings import Settings

# Load flask app
app = Flask(__name__)

# Load project objects
loop = MainLoop()
settings = Settings()

# Load prject properties
suppl_heating = False
suppl_heating_status = False



from app import routes
