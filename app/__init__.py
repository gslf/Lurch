from flask import Flask
from MainLoop import MainLoop

app = Flask(__name__)
loop = MainLoop()

from app import routes
