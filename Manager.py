import os
import sys
import json
import hashlib
import traceback
from utils import Installer


def update_vpkfile():
    fio = open("vpks.json")
    jso = json.load(fio)
    pvpks = [filename for filename in os.listdir(tf+f"{os.path.sep}vpk")]
    vvpks = [vpk for vpk in jso["vpks"].keys()]
    for name in pvpks:
        if name in vvpks:
            pass
        else:
            filestream = open(tf+os.path.sep+"vpk"+os.path.sep+name, "rb")
            md5 = hashlib.md5(filestream.read())
            md5sum = md5.hexdigest()
            jso[name] = {
                "md5": md5sum,
                "Mod": "Basic"
            }
    fio.close()
    wio = open("vpks.json", "w")



def list():
    with open("vpks.json") as js:
        db = json.load(js)
    form = "------VPK Name: {0}------\nMod: {1}\n\n"
    for column, keys in db["vpks"].items():
        print(form.format(column, keys["Mod"]))


def exit():
    sys.exit(0)





def runtime():
    commands = {
        "list": list,
        "exit": exit
    }
    while 1:
        command = input("Input a command: ")
        try:
            func = commands[command]
            func()
        except KeyError as e:
            tb = traceback.format_exception(type(e), e, e.__traceback__)
            print("\n".join(tb))


for _ in range(2):
    if ".dir" not in os.listdir():
        Installer.find_titanfall_2()
    else:
        with open(".dir") as d:
            tf = d.read()
        tf = tf.strip()
        runtime()
        break