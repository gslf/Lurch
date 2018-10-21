# :#/ Lurch
### Solar water heating managemant via Raspberry PI 3


## How To Use Lurch
Lurch is almost ready for use out-of-the-box. To use it simply wire the hardware, install the required libraries and then start the Flask webserver.

1. Wire the hardware (instruction below)
1. Install required library with this commands:
    1. _sudo pip3 install w1thermsensor_
    1. _sudo pip3 install flask_
1. Download & Unzip the source code in a folder
1. Open the folder in a terminal
1. Start the Flask webserver with this commands:
    1. export FLASK_APP=lurch.py
    1. sudo flask run
1. Open a browser at 127.0.0.1:5000
1. __Enjoy Lurch!__


## Hardware requirements
* Raspberry PI 3
* Temperature sensor DS18B20 
* Single 5V Rele module jqc-3ff
* Heating Element 220V 1500W

## Hardware scheme
* ToDo . . .

## Software requirements
* Click==7.0
* Flask==1.0.2
* itsdangerous==0.24
* Jinja2==2.10
* MarkupSafe==1.0
* pkg-resources==0.0.0
* w1thermsensor==1.1.2
* Werkzeug==0.14.1








Powered by [:#/promezio](https://promezio.it).
