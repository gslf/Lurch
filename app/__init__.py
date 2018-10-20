from flask import Flask
from app.MainLoop import MainLoop
from app.Settings import Settings
from app.Raspberry import Raspberry

# Load flask app
app = Flask(__name__)

# Load project objects
settings = Settings()
raspberry = Raspberry()
loop = MainLoop(settings,raspberry)


from app import routes
