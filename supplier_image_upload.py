#!/usr/bin/env python3

import requests
import os

url = "http://CHANGENAMETOIPXXXXX/upload" #PLACEHOLDER FOR LAB IP
directory = "./supplier-data/images/"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if f.endswith(".jpeg"):
        with open(f, 'rb') as opened_file:
            r = requests.post(url, files = {'file': opened_file})