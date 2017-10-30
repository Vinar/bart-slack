import requests
import json
import pytz
import bartStations
import constants

from datetime import datetime
from pytz import timezone


def getRealTimeDepartures(station):

    # Verify if its a valid station in BART system
    validStation = bartStations.validate(station)

    if (not validStation):
        statusMessage = constants.NOT_A_VALID_STATION

    if (station == ''):
        statusMessage = constants.NO_STATION

    if (validStation and station != ''):
        # API callout prep
        API_ENDPOINT = constants.BART_API_ENDPOINT + 'etd.aspx'
        params = {'cmd': 'etd', 'json': 'y', 'key': 'QBZ4-Z5SG-QRBY-YIDD', 'orig': str(station)}

        # API callout
        response = requests.get(API_ENDPOINT, params=params)

        json_response = json.loads(response.text)

        # Formatting date in Pacific Time Zone
        date_format = '%m/%d/%Y %H:%M:%S %Z'
        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Pacific'))
        pacificDateTime = date.strftime(date_format)

        statusMessage = " Departure times from " + station + \
            " station as of " + pacificDateTime + " is as follows " + response.text

    return statusMessage
