import config
import stt
from fuzzywuzzy import fuzz
from commands import *


print(f"{config.NAME} онлайн...")


def respond(voice: str):
    print(voice)
    if voice.startswith(config.ALIAS) or config.CMD_LIST:
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.CMD_LIST.keys():
            tts.tts_speak("Так?")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.ALIAS:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


stt.stt_listen(respond)