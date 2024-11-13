from configparser import ConfigParser
from PySide6.QtCore import QSize
import os

QUIZ_TABLE = "quiz"

ARDUINO_USE = "yes"
ARDUINO_PORT = "/dev/ttyACM0"
ARDUINO_BAUD = 9600

# standard image if no album image is found
image_image = "standard.jpg"
small_image = QSize(200, 200)
big_image = QSize(400, 400)
image_path = "/home/benny/Dokumente/musikquiz_local/musikquiz/static/cover/"


# player
pressedBuzzerColor = "rgb(0, 191, 209)"
blockedBuzzerColor = "rgb(255, 0, 0)"
playerColor = "rgb(255, 255, 255)"
roundTopColor = "rgb(0, 100, 000)"
roundPlayoffColor = "rgb(255, 255, 0)"

# color vars
background_color = "#333436"
main_color = "#00c300"
active_button_color = "black"
question_color = "#dcdcdc"
question_bg_color = "#333436"

# toggle colors
ToggleBgColor = "#000000"
ToggleCircleColor = "#F5F5DC"
ToggleActiveColor = "#00FF00"

# window size vars
hwindowsize = 1400
vwindowsize = 900

def config(filename='database.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    dbx = {}
    if section in parser:
        for key in parser[section]:
            dbx[key] = parser[section][key]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))
    return dbx
