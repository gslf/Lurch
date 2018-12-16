#
# :#/ promezio
# Lurch is an open source solar water heating managemant system
#

from app import app

def startWebserver():
    '''
    This function start a Flask webserver 
    '''
    app.run(host="0.0.0.0")



if __name__ == "__main__":
    # Run webserver when this file is called by command line
    startWebserver()
