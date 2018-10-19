from flask import render_template, request
from raspberryManagemant import getTemp
from app import app

@app.route('/',methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
   
    # Read current temperature
    current_temp = getTemp()

    form_data = request.form 
    if(form_data):
        
        # Read form data
        #TODO form_data['threshold_min']

        # Save form data
        #TODO
    else:
        # Read saved settings
        #TODO

    # Run main loop

    return render_template('index.html', title='Home')
