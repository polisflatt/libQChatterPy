import requests
import os

import libqchatterpy.constants 

constants = libqchatterpy.constants


def getMotd():
    return requests.post("{ip}/Server/motd.php".format(ip = constants.SERVER_IP_DNS)).text


def executeServerCommand(command):
    return requests.post("{ip}/Command/issue_command.php".format(ip = constants.SERVER_IP_DNS), {"command": command}).text
