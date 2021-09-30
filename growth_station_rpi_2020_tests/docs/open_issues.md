# Open Issues

This list shows the open issues that we are facing.

## Time coordination

The RPi does not have the ability of keeping track of time when it is off. For this reason, we will have to account for the issue by either connecting it some type of NTP server, or giving each RPi its own clock.

In a single-node installation that does not have an Internet connection, we may have to adjust for the issue by building a real-time clock, similar to what is here: [Adding a Real Time Clock to Raspberry Pi](https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/overview).

In case the installation contains multiple nodes collected by a Farmer, then the Farmer can just run the NTP server and coordinate the timing. In the case of a larger system with the Farmer coordinating the time, we can either rely on the Farmer having a real-time clock, or connectivity to the Internet.

[Use a Pi as an NTP server](https://www.raspberrypi.org/forums/viewtopic.php?t=188673)

## Installation and Deployment

Crete scripts that automate the setup of the Growth Stations as well as the Farmer.

## TODO

Temperatures in C or F
