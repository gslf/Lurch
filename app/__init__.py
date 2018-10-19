from flask import Flask
from MainLoop import MainLoop
from Settings import Settings

app = Flask(__name__)
loop = MainLoop()
settings = Settings()

from app import routes
