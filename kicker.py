# TYPE : AUTO JS KICKER 2020.# PROGRAMMER : BOTCU ANGARALI .LINE: botcux1
from important import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from threading import Thread
from Naked.toolshed.shell import execute_js
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
botcu = LINE("you mid here")
botcuProfile = botcu.getProfile()
botcuSettings = botcu.getSettings()
botcuPoll = OEPoll(botcu)
botcuMID = botcu.getProfile().mid
oepoll = OEPoll(botcu)
loop = asyncio.get_event_loop()
async def botcuBot(op):
        if op.type == 13:
            if botcu.getProfile().mid in op.param3:
                xyz = botcu.getCompactGroup(op.param1)
                contact = botcu.getContact(op.param2)
                botcu.acceptGroupInvitation(op.param1)
                mems = [c.mid for c in xyz.members]
                targk = []
                for x in mems:
                    if x not in [op.param2,botcu.profile.mid]:targk.append(x)
                    xbot = 'dual.js gid={} token={}'.format(op.param1, botcu.authToken)
                    for x in targk:xbot += ' uik={}'.format(x)
                    execute_js(xbot)
def run():
    while True:
            ops = botcuPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(botcuBot(op))
                   #clientBot(op)
                   botcuPoll.setRevision(op.revision)
if __name__ == "__main__":
    run()
