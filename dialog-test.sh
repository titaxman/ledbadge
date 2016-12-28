#!/bin/bash
set -e
clear
message=$(dialog --backtitle "Python-based mini LED Badge Uploader" \
--max-input 250 \
--title "Enter Your Message!" \
--inputbox "Maximum Entry of 250 characters" 8 60 3>&1 1>&2 2>&3)
clear
action=$(dialog --backtitle "Python-based mini LED Badge Uploader" \
--title "Select Your Action!" \
--radiolist "Your [SPACE] or Mouse-Click to select Speed." 12 50 5 \
A "Hold" off \
B "Rotate" on \
C "Snow" off \
D "Flash" off \
E "Hold Frame" off 3>&1 1>&2 2>&3)
clear
speed=$(dialog --backtitle "Python-based mini LED Badge Uploader" \
--title "Select Your Speed!" \
--radiolist "Your [SPACE] or Mouse-Click to select Speed." 12 50 5 \
1 "Slowest" off \
2 "Slower" off \
3 "Moderate" off \
4 "Faster" off \
5 "Fastest" on 3>&1 1>&2 2>&3)
clear
/usr/bin/python ./message.py "$message" $speed $action
