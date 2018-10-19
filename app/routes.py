from flask import render_template, request
from app.raspberryManagemant import getTemp
from app import app, settings, suppl_heating, suppl_heating_status

@app.route('/',methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
   
    # Read settings/data and populate view
    current_temp = getTemp()
    thresholdMIN = settings.thresholdMIN
    thresholdMAX = settings.thresholdMAX

    shs = 'on' if suppl_heating_status else 'off'
    sh = 'on' if suppl_heating else 'off'

    # From managemant
    form_data = request.form 
    if(form_data):
        # Save form data
        settings.thresholdMIN = form_data['threshold_min']
        settings.thresholdMAX = form_data['threshold_max']
    else:
        # Read saved settings
        #TODO
        pass

    # Run main loop
    #TODO

    # Load template
    return render_template('index.html', temp = current_temp, shs = shs, heating_threshold_MAX = thresholdMAX, heating_threshold_MIN = thresholdMIN, sh = sh)