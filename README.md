# mini LED Badge Uploader
## Instructions
<a href="http://www.tutorialspoint.com/python/index.htm">Python</a> is required for standard operation.
The `demo.py` program sends "Python" to the badge.<br>
The `input.py` program is console-based API for data entry.<br>
`python message.py "message" 5 B` = Sends "message" at the speed of 5 (1-5) and action B (A-E).<br>
The script `message.py` uses <a href="http://www.tutorialspoint.com/python/python_command_line_arguments.htm">Python Command Line Arguments</a>.<br>
Shell script `dialog-test.sh` is an example message entry script that uses <a href="http://linux.die.net/man/1/dialog">dialog</a>.<br>
Shell script `showtemp.sh` displays the temperature of <a href="http://en.wikipedia.org/wiki/Pasig">Pasig City</a>, <a href="http://en.wikipedia.org/wiki/Philippines">Philippines</a> on the LED board.
## Where to buy this USB LED Mini Board
A couple of years ago, I bought my unit for a store in <a href="http://en.wikipedia.org/wiki/SM_Megamall">SM Megamall</a> Cyberzone, however, the store I bought mine from, no longer sells these LED boards.<br><br>
When I did a Google Search, I found this URL: http://www.usbgeek.com/products/usb-led-mini-board
## Conclusion
Tested on my Blue Scrolling LED Mini Board (48 x 12 pixels)<br>
![Alt text](/KM_LED_Badge.png?raw=true "Kuya Marc USB LED Badge")<br>
Recent versions of Linux have a built-in driver for the PL2303 serial USB device, so no extra driver is necessary. Python code has been tested with 32-bit & 64-bit GNU/Linux, FreeBSD and Oracle Solaris operating systems.

