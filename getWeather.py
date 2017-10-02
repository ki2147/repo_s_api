# -*- coding: utf-8 -*-
"""
This script will fetch the maximum and minimum temperature over the next 5 days for a city
By default it will fetch the data for New York, NY in fahrenheit
Defaults can be overridden by the -c and -u options (or --city and --units)
e.g. python getWeather.py --city seattle,wa --units metric
"""

import requests
import getopt
import sys

def main(argv):
    #Default values for query parameters
    units='imperial'
    city='newyork,ny'
    url_endpoint='http://api.openweathermap.org/data/2.5/forecast?appid=b417f7c6df42e7ab06ebf19ec691dc13'
    
    #If city and units options are passed, the default values are overwritten
    opts, args = getopt.getopt(argv, "c:u:", ["city=", "units="])
    for opt, arg in opts:
          if opt in ('-c', '--city'):
              city=arg
          elif opt in ('-u', '--units'):
              units=arg
    
    paramDict = {'q': city, 'units': units}
    
    def getResponse(url, paramDict):
        response = requests.get(url, params=paramDict)
        assert response.status_code == 200
        parsed_json = response.json();
        return parsed_json
    
    parsed_json = getResponse(url_endpoint, paramDict)
    
    #Parse the response to construct arrays for maximum and minimum temperature for each data point
    maxArray = [ x['main']['temp_max'] for x in parsed_json['list'] ]
    minArray = [ x['main']['temp_min'] for x in parsed_json['list'] ]
    
    print('Max temp over the next 5 days in', city, 'is', max(maxArray))
    print('Min temp over the next 5 days in', city, 'is', min(minArray))


if __name__ == "__main__":
   main(sys.argv[1:])
   