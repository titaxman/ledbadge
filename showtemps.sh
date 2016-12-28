#!/bin/bash
set -e

speed=4
action=B

# Weather for Pasig City, Metro Manila, Philippines
URL='http://www.accuweather.com/en/ph/pasig/264876/weather-forecast/264876'
temp="$(wget -q -O- "$URL" \
| awk -F\' '/acm_RecentLocationsCarousel\.push/\
{print "Pasig City Current Temp: "$10"C Real Feel: "$12"C Condition: "$14 }' \
| head -1 )"

/usr/bin/python ./message.py "$temp" $speed $action
