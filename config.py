from configparser import ConfigParser
import os

QUIZ_TABLE = "quiz"
# is path for id_deployer


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

def config_serverai(filename='database.ini', section='serverai'):
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
