import bart_status
import bart_realTimeDepartures
import constants

from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():

    # TODO : pass in parameter from URL
    station = 'MLBR'

    message = bart_status.getStatus(station)

    errorMessageCondition = (constants.NOT_A_VALID_STATION is message)

    if (station != '' and (not errorMessageCondition)):
        message += bart_realTimeDepartures.getRealTimeDepartures(station)

    return message
