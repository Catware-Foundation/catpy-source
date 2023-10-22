
#
# -*- coding: utf-8 -*-
#
# Catware Development. 2016-2020
#
# CatOS Boot
#

print('Идёт запуск CatOS...')

print(">>> Загрузка окружения системы...")
file = open("catenv.py", encoding="utf-8")
catenv = file.read()
file.close()
exec(catenv)
catenv = ""
OkMsg("Успешно")

#
# Modules
#

import os
procmsg("Загрузка shutil")
import shutil
succ()
procmsg("Загрузка subprocess")
import subprocess
succ()
procmsg("Загрузка wikipedia")
import wikipedia
succ()
procmsg("Загрузка runpy")
import runpy
succ()
procmsg("Загрузка numpy")
import numpy as np
succ()
procmsg("Загрузка wget")
import wget
succ()
procmsg("Загрузка PIL")
from PIL import Image, ImageDraw, ImageFont
succ()
procmsg("Загрузка random")
import random as randd
from random import random
succ()
procmsg("Загрузка requests")
import requests
succ()
procmsg("Загрузка vk_api")
import vk_api
from vk_api import VkApi
from vk_api import VkUpload
succ()
procmsg("Загрузка time")
import time
succ()
procmsg("Загрузка vk_api [дополнительные библиотеки]")
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
succ()
procmsg("Настройка библиотек")
session = requests.Session()
wikipedia.set_lang("ru")
succ()
procmsg("Загрузка urllib")
import urllib.request
import urllib.parse
succ()
procmsg("Загрузка sys")
import sys
succ()
procmsg("Загрузка threading")
from threading import Thread
succ()

procmsg("Загрузка конфигурации [base]")
exec(ReadFF("configs/base.py"))
succ()

if os.name == 'nt':
    osname = 'Windows NT'
if os.name == 'posix':
    osname = 'GNU/Linux'
if os.name == 'mac':
    osname = 'MacOS'
if os.name == 'os2':
    osname = 'OS/2 Warp'
if os.name == 'ce':
    osname = 'Windows CE'
if os.name == 'java':
    osname = 'Java'
InfoMsg('Detected OS: ' + osname)
try:
    os.mkdir('exf')
    os.mkdir('users')
    os.mkdir('chats')
except Exception:
    pass

authors = []
commands = []
ids = []
descs = []
modes = []
depends = []

vk_session = VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, gid)
vk = vk_session.get_api()
keyboard = VkKeyboard(one_time=False)
uptime = str(time.ctime())
uptime_time = time.time()

print('* Финальная подготовка.')
writeTo(admins, "admins.txt")

time.sleep(2)
CallSystem2('clear')
Select = input(ReadFF('loader.txt'))

if Select == '1':
    print('''
CatShell v0.0.0

Type "help" to get started
''')
    while True:
        cmd = input(">")
        wrds = cmd.split(' ')
        command = wrds[0]
        parameters = " ".join(wrds[1:])
        writeTo(parameters, 'exf/parameters.txt')
        try:
            Run('exf/' + command + '.py')
        except Exception as e:
            if command + '.py' not in os.listdir('exf'):
                print('/' + 'exf/' + command + '.py: command not found')
            else:
                print(e)
if Select == '2':
    while True:
        try:
            mta('Запускаю ядро...')
            exec(ReadFF("core.py"))
            mta('Ядро упало :(')
        except Exception as e:
            FailMsg('Kernel panic: ' + str(e))
        authors = []
        commands = []
        ids = []
        descs = []
        modes = []
        depends = []

if Select == '3':
    CallSystem2('clear')
    print('''
Python3 Catware Shell
''')
    while True:
        exec(input('>>>'))

if Select == '4':
    CallSystem2('clear')
    print('''MAI Information

Botname: ''' + botname + '''
Botversion: ''' + version + '''
CatOS version: ''' + core)
    input('\nPress any key to power off...')
    exit()
if Select == '5':
    exit()
