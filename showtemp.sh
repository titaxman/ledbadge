#!/bin/bash
set -e
# Weather for Pasig City, Metro Manila, Philippines
URL='http://www.accuweather.com/en/ph/pasig/264876/weather-forecast/264876'
temp="$(wget -q -O- "$URL" \
| awk -F\' '/acm_RecentLocationsCarousel\.push/{print $10 }' | head -1 )"
/usr/bin/python ./post.py "CT:"$temp"C"

