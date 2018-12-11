from flask import render_template, request
from app import app, settings, raspberry, loop

@app.route('/',methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    # Fomr managemant
    form_data = request.form 
    if(form_data):
        # Read settings from form
        settings.thresholdMIN = int(form_data['threshold_min'])
        settings.suppl_heating = True if form_data['status'] == 'enabled' else False
    
    # Update settings
    current_temp = raspberry.getTemp()
    thresholdMIN = settings.thresholdMIN

    # Populate view
    shs = 'on' if settings.suppl_heating_status else 'off'
    sh = 'on' if settings.suppl_heating else 'off'
    sh_enabled = 'checked' if settings.suppl_heating else ''
    sh_disabled = 'checked' if not settings.suppl_heating else ''

    # Run main loop
    if settings.suppl_heating :
        loop.start()
    else :
        loop.stop()

    # Load template
    return render_template('index.html', temp = int(current_temp), shs = shs, heating_threshold_MIN = thresholdMIN, sh = sh, sh_enabled = sh_enabled, sh_disabled = sh_disabled)
