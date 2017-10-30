import os
import requests
import json
import time

from flask import Flask


app = Flask(__name__)


@app.route('/')
def status():

    API_ENDPOINT = 'http://api.bart.gov/api/bsa.aspx'
    params = {'cmd': 'bsa', 'json': 'y', 'key': 'QBZ4-Z5SG-QRBY-YIDD'}
    response = requests.get(API_ENDPOINT, params=params)

    # displayMessage = "Welcome to Bart-Slack app !!"
    # displayMessage += "\n\n******************"
    # displayMessage += "\n\n******************"
    # displayMessage += "\n\nReruest URL : " + str(response.url)
    # displayMessage += "\n\nStatus : " + str(response.status_code)

    json_response = json.loads(response.text)
    bartMessage = json_response['root']['bsa'][0]['description']['#cdata-section']
    currentDateTime = time.strftime('%Y-%m-%d %H:%M:%S')
    displayMessage = "Current Status as of " + currentDateTime + "  ==>  " + str(bartMessage)

    return displayMessage
