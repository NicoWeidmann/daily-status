# Daily Status for Adafruit Thermal Printer

This is a Python script that prints a daily status report on your Adafruit Thermal Printer.

![GIF couldn't be loaded :(](.github/printer_vid.gif)

## Description

For a previous project I bought the [Adafruit Thermal Printer](https://learn.adafruit.com/mini-thermal-receipt-printer).
I also had an old Raspberry Pi 1 lying around and so I thought: why not combine the two and build a fun project that
prints a daily status report with the events of the day, a weather report and some other more or less useful information.

The script consists of separated [modules](modules/), each of which prints a separate part of the report. With
this design, it is easy to add new modules to the report. As of now, the following modules exist:

* **Calendar**:  
This module connects to a user's google calendar and prints the upcoming events for the day of interest. A descrition
on how to set up the module can be found [here](modules/calendar).

* **Greeter**:  
Prints a greeting with the user's name. Also prints the day and date the report is generated for.

* **Weather**:  
Prints a weather report for the day of interest (with min. and max. temperatures and precipitation probability). The
data is obtained from the [darksky.net](https://darksky.net/dev) API.

* **News**:  
Prints some trending headlines. The default version prints the 3 top headlines in Germany. The data is obtained from
the [newsapi.org](https://newsapi.org) API.

* **Postillon**:  
This module prints pun headlines made by [Der Postillon](http://www.der-postillon.com), a satiric german news site (quite
similar to [The Onion](https://www.theonion.com)).

## Usage

To use this script, simply clone the repository. The Adafruit printer library is included in this repository as a
git submodule, you might have to download it by executing the following commands in the root directory of this repository:
```
git submodule init
git submodule update
```
Make sure the submodule (at `lib/printer`) is checked out at the latest commit (`master` branch).

Before you can run the script, copy the file `config_example.py` and save it as `config.py`. This file contains some
settings you might want to adjust (every option is documented by comments in the file, simply have a look around).

Install the dependencies (listed in the provided Pipfile, pipenv can be used to install the dependencies).

Instructions on how to set up the hardware (i.e. how to connect printer and Raspberry Pi) can be found in this [Adafruit
Tutorial](https://learn.adafruit.com/pi-thermal-printer/case-2#step-28). However, only the GND and RX pins have to be
connected (some sources say that connecting the TX pin could damage the RasPi).

*If something doesn't work as intended, feel free to open a new Issue or fix the problem
yourself and open a PR ;)*

## Requirements

* Raspberry Pi 1 (might also work with later models, although additional configuration might be necessary due to issues
with the serial port caused by the bluetooth module on the Model 3)
* [Adafruit Thermal Printer](https://learn.adafruit.com/mini-thermal-receipt-printer) (other Adafruit printer kits could
also be used)
* Python 3.6 installed on the Raspberry Pi (pip or pipenv for easy installation of the required libraries)


* for the Calendar module: a Google API console project and, of course, a Google account. See [here](modules/calendar) for
further instructions.
* for the Weather module: a [darksky.net](https://darksky.net/dev) API key (free for developers).
* for the News module: a [newsapi.org](https://newsapi.org) API (free as well)
