def validate(station):

    # TODO : Add all stations
    allBartStations = {'MLBR': 'Millbrae', 'CIVC': 'Civic Center / UN Plaza Station', '16TH': '16th St. Mission Station',
                       '24TH': '24th St. Mission Station', 'RICH': 'Richmond Station', 'DALY': 'Daly City Station', 'SFIA': 'San Francisco International Airport Station'}

    validStation = station in allBartStations

    return validStation
