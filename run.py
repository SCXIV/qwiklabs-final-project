#!/usr/bin/env python3

import os
import requests
from pathlib import Path

fruits_list = {}
keys = ["name", "weight", "description", "image_name"]
index = 0
directory = "./supplier-data/descriptions/"
image_directory = "./supplier-data/images/"

for filename in os.listdir(directory):
    with open(directory + filename) as f:
        for info in f:
            text = info.strip()
            if "lbs" in info:
                # May not work in lab(?)
                trimmed_line = Path(info).stem
                converted_weight = int(trimmed_line)
                fruits_list["weight"] = converted_weight
                index += 1
            else:
                try:
                    fruits_list[keys[index]] = text
                    index += 1
                except:
                    fruits_list[keys[2]] = text
        
        index = 0
        split_filename = filename.split(".")
        name = split_filename[0] + ".jpeg"

        for img in os.listdir(image_directory):
            if img == name:
                fruits_list["image_name"] = name
        
        response = requests.post("http://ENTERIPHERE/fruits/", json = fruits_list)
        fruits_list.clear()
