#!/bin/bash
import json

def read_code(filename):
    city_ = {}
    with open(filename, 'r') as f:
        temp = json.loads(f.read())
        for city in temp:
            if 'city_code' in city:
                key = city['city_name']
                value = city['city_code']
                city_[key] = value

    sorted(city_.keys())
    return city_