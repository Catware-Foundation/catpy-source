need_install = True
install = [
"vk_api",
"requests",
"wikipedia",
"wget",
"google_trans_new",
"lyricsgenius",
"SpeechRecognition",
"pyaspeller",
"gTTS",
"yandex_music"
]
modules = [
"import vk_api",
"import vk_api as api2",
"from vk_api import VkUpload, VkApi",
"from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType",
"from vk_api.keyboard import VkKeyboard, VkKeyboardColor",
"import requests",
"from requests import get, post, Session",
"import wikipedia",
"import wget",
"from google_trans_new import google_translator",
"from lyricsgenius import Genius",
"import speech_recognition as speech_recog",
"from yandex_music.client import Client"
]
script = """
session = requests.Session()
wikipedia.set_lang("ru")
vk_api.VkApi.RPS_DELAY = 1/20 # Для пользовательских ключей значение 1/3
translator = google_translator()
genius = Genius("UbhRZjKz4jS5XzdjxCVHr1t-BE9KqSxne0ogbzzCZr57eMubSPznK1L9-OlXILjs")
genius.response_format = 'plain'
"""
