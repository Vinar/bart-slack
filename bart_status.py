import requests
import json
import pytz
import bartStations
import constants

from datetime import datetime
from pytz import timezone


def getStatus(station):

    # API callout prep
    API_ENDPOINT = constants.BART_API_ENDPOINT + constants.COMMAND_STATUS + '.aspx'
    params = {'cmd': constants.COMMAND_STATUS,
              constants.RESPONSE_FORMAT: 'y', 'key': 'QBZ4-Z5SG-QRBY-YIDD'}
    if (station != ''):

        # Verify if its a valid station in BART system
        validStation = bartStations.validate(station)

        if (not validStation):
            message = constants.NOT_A_VALID_STATION
            return message
        else:
            params.update({'orig': str(station)})

    # API callout
    response = requests.get(API_ENDPOINT, params=params)

    # displayMessage = "Welcome to Bart-Slack app !!"
    # displayMessage += "\n\n******************"
    # displayMessage += "\n\n******************"
    # displayMessage += "\n\nReruest URL : " + str(response.url)
    # displayMessage += "\n\nStatus : " + str(response.status_code)

    json_response = json.loads(response.text)
    # TODO : Include type in advisory messages. The "type" element will either be DELAY or EMERGENCY
    # bartStatusMessageType = json_response['root']['bsa'][0]['type'] + " : "
    bartStatusMessageDescription = json_response['root'][constants.COMMAND_STATUS][0][constants.STATUS_TAG]['#cdata-section']

    # Formatting date in Pacific Time Zone
    date_format = '%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    pacificDateTime = date.strftime(date_format)

    displayMessage = "Current Status "

    if station != '':
        displayMessage += "for " + station + " station "

    displayMessage += "as of " + pacificDateTime + " is " + str(bartStatusMessageDescription)

    return displayMessage
