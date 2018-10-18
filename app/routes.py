from flask import render_template, request
from raspberryManagemant import getTemp
from settingsManagemant import readSettings, saveSettings
from app import app

@app.route('/',methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
   
    # Read current temperature
    current_temp = getTemp()

    form_data = request.form 
    if(form_data):
        print(form_data['threshold_min'])
        # Read form data
        settings = #TODO

        # Save form data
        saveSettings(settings)
    else:
         # Read saved settings
        settings = readSettings()

    # Run main loop

    return render_template('index.html', title='Home')
