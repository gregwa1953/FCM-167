#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     weather-api-test1.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #167
# Written by G.D. Walters
# Copyright (c) 2021 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
# Assumption - Python 3.7.4 or better
# ======================================================

import requests
import json

degree_sign = "\N{DEGREE SIGN}"
address = "http://api.weatherapi.com/v1/"
JsonCurrentsQuery = "forecast.json?"
key = "key=Your API Key Here"
location = "&q=78748"
extras = "&days=3&aqi=&alerts=yes"
link = f"{address}{JsonCurrentsQuery}{key}{location}{extras}"

session = requests.Session()
response = session.get(link).json()

datatime = response["current"]["last_updated"]

temp = response["current"]["temp_f"]
feelslike = response["current"]["feelslike_f"]
wind = response["current"]["wind_mph"]
pressuremb = response["current"]["pressure_mb"]
pressurein = response["current"]["pressure_in"]
conditions = response["current"]["condition"]["text"]
winddir = response["current"]["wind_dir"]
windgust = response["current"]["gust_mph"]
winddegree = response["current"]["wind_degree"]

print(f"Time: {datatime}")
print(f"Conditions: {conditions}")
print(f"Temp: {temp}")
print(f"Wind: {wind} Gusts: {windgust} From: {winddir} ({winddegree}{degree_sign})")
print(f"Feels like: {feelslike}")
print(f"Pressure:")
print(f"    {pressuremb }mb")
print(f"    {pressurein} in")

print("")
print("-------------------")
print("   3 Day Forecast")
print("")
forecastday = response["forecast"]["forecastday"]

for cntr in forecastday:
    condition = cntr["day"]["condition"]["text"]
    high = cntr["day"]["maxtemp_f"]
    low = cntr["day"]["mintemp_f"]
    probRain = cntr["day"]["daily_chance_of_rain"]
    probSnow = cntr["day"]["daily_chance_of_snow"]
    moonphase = cntr["astro"]["moon_phase"]
    illumination = cntr["astro"]["moon_illumination"]
    print(cntr["date"])
    # print(cntr["day"])
    print(f"Conditions: {condition}")
    print(f"Forecasted High: {high}")
    print(f"Forecasted Low: {low}")
    print(f"Chance of rain: {probRain}%")
    print(f"Chance of snow: {probSnow}%")
    print(f"Phase of Moon: {moonphase}")
    print(f"Moon Illumination: {illumination}")
    print("")

if "alerts" in response:
    if response["alerts"]["alert"] != []:
        print("Alert has been issued!")
        alert = response["alerts"]
        print(alert)
    else:
        print("No alerts at this time.")