from vk_api import VkApi
import json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from sys import exc_info
import traceback
import random as randd

beta_text = """Благодарим за интерес к программе бета-тестирования catpy!
Привилегии бета-тестировщика catpy позволяют использовать и тестировать некоторые команды и функционал до официального появления в catpy. За успешные баг-репорты (отчёты об багах) вам будут начисляться очки, которые будут поднимать вас в рейтинге. Самые успешные тестировщики будут получать призы :)

Обращаем ваше внимание, что для вступления в программу бета-тестирования catpy вам потребуется наличие действующей подписки на @catpy (catpy) длительностью не менее 3 месяцев и наличие заявки на вступление в данную группу. Вступая в программу, вы соглашаетесь с правом Администрации catpy закрыть вам доступ к бета-тестированию за отсутствие активности или по иным причинам, соглашаетесь с добровольностью участия в программе бета-тестирования, а также обязуетесь принимать участие в бета-тестировании и своевременно сообщать Администрации о багах.

Остались вопросы по программе бета-тестирования catpy? Обратитесь к учредителю программы @theagrik (Ивану Загайнову) за всеми необходимыми разъяснениями.

Нажимая кнопку "Вступить в программу", вы подтверждаете ознакомление с данным сообщением. После нажатия на кнопку ваш аккаунт будет проверен на соответствие условиям вступления в программу бета-тестирования."""

Ff = open("catenv.py", 'r', encoding='UTF-8')
exec(Ff.read())
Ff.close()
del Ff
outputd = False

VkApi.RPS_DELAY = 1/20

catpy = VkApi(token="токен от кетпая").get_api()
beta = VkApi(token="токен от группы кетпай бета тестерс")
haxinge = VkApi(token="токен от какой то там юзерки").get_api()
longpoll = VkBotLongPoll(beta, 203746151) # вроде тут какой то gid вроде от группы кетпай бета тестерс

vk = beta.get_api()

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                event.object = event.object["message"]
                user_id = event.object['from_id']
                peer_id = event.object['from_id']
                text = event.object["text"]
                
                if text == "Начать":
                    message(beta_text, keyboard='{"one_time":false,"inline":false,"buttons":[[{"color":"positive","action":{"type":"text","payload":null,"label":"Вступить в программу"}}]]}')
                    
                if text == "Вступить в программу":
                    message("Начинаю проверку вашего аккаунта, подождите...")
                    accept = True
                    issues = ""
                    
                    
                    
    except:
        exc_type, exc_value, exc_tb = exc_info()
        print("\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
