#!/usr/bin/env python

__author__ = 'LeanneBenson'

import requests
import time
import turtle

iss_api = 'http://api.open-notify.org'

def astronaut_info():
    r = requests.get(iss_api + '/astros.json')
    r.raise_for_status()
    return r.json()['people']

def iss_location():
    r = requests.get(iss_api + '/iss-now.json')
    r.raise_for_status()
    position = r.json()['iss_position']
    latitude = float(position['latitude'])
    longitude = float(position['longitude'])

    return latitude, longitude


    
def main():
    pass


if __name__ == '__main__':
    main()
