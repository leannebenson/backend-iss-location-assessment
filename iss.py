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
    iss.goto(longitude, latitude)
    return map


def main():
    pass


if __name__ == '__main__':
    main()
