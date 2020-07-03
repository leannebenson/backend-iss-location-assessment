#!/usr/bin/env python

__author__ = 'LeanneBenson'

import requests
import time
import turtle

iss_api = 'http://api.open-notify.org'
world_img = 'map.gif'
iss_img = 'iss.gif'

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

def iss_map(latitude, longitude):
    map = turtle.Screen()
    map.setup(720, 360)
    map.bgpic(world_img)
    map.setworldcoordinates(-180, -90, 180, 90)
    map.register_shape(iss_img)
    iss = turtle.Turtle()
    iss.shape(iss_img)
    iss.setheading(90)
    iss.penup()
    iss.goto(latitude, longitude)
    return map

def iss_risetime(latitude, longitude):
    params = {'lat': latitude, 'lon': longitude}
    r = requests.get(iss_api + '/iss-pass.json', params=params)
    r.raise_for_status()
    
    passover = r.json()['response'][1]['risetime']
    return time.ctime(passover)

def main():
    astro_info = astronaut_info()
    print('Number of astronauts on ISS: {}'.format(len(astro_info)))
    for astro in astro_info:
        print(' - {} in {}'.format(astro['name'], astro['craft']))

    latitude, longitude = iss_location()
    print('Real-time ISS Co-Ordinates: latitude={:.02f} longitude={:.02f}'.format(latitude, longitude)')
    
    map = None
    try:
        map = iss_map(latitude, longitude)
        indiana_latitude = 39.791000
        indiana_longitude = -86.148003
        location_pin = turtle.Turtle()
        location_pin.penup()
        location_pin.color('yellow')
        location_pin.goto(indiana_latitude, indiana_longitude)
        location_pin.dot(5)
        

    pass


if __name__ == '__main__':
    main()
