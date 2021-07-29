import os
import json
from utils import Installer


def list():
    with open("vpks.json") as js:
        db = json.load(js)
    form = "------VPK Name: {0}------\nMod: {1}\n\n"
    for column, keys in db["vpks"].items():
        print(form.format(column, keys["mod"]))


def runtime():
    commands = {

    }
    while 1:



if not ".dir" in os.listdir():
    Installer.find_titanfall_2()
else:
    with open(".dir") as d:
        tf = d.read()
    tf = tf.strip()
    os.chdir(tf)