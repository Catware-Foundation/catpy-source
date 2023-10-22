#!/usr/local/bin/python3.9
import os
fileslist = os.listdir(".")
for x in fileslist:
    print("Блять: " + x + ", сайз: " + str(len(x)))
