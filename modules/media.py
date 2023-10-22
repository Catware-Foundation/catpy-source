need_install = True
install = [
"webcolors",
"geopy",
"astral",
"zalgo_text",
"bs4",
"feedparser",
"qrcode",
"gTTS",
"pyaspeller",
"pydub",
"html2text",
"markovify",
"numpy",
"pytesseract",
"pillow",
"lxml",
"cachetools"
]
modules = [
"import webcolors",
"import geopy",
"from geopy import distance",
"import astral",
"from astral import moon as astr_moon",
"from zalgo_text.zalgo import zalgo",
"from bs4 import BeautifulSoup",
"from feedparser import parse",
"import qrcode",
"from gtts import gTTS",
"from pyaspeller import Word, YandexSpeller",
"from pydub import AudioSegment",
"import html2text",
"import markovify",
"import numpy as np",
"import pytesseract",
"from PIL import Image, ImageDraw, ImageFont, ImageFilter"
]
script = """
zalgofy = zalgo().zalgofy
del zalgo
speller = YandexSpeller()
"""
