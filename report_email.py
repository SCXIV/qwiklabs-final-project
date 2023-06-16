#!/usr/bin/env python3

import os
import datetime
import reports
import emails

date_time = datetime.date.today().strftime("%B %d, %Y")
date_string = "Processed Update on " + date_time
names = []
weights = []
directory = "./suppliet-data/descriptions/"

for filename in os.listdir(directory):
    with open(directory + filename) as f:
        for text in f:
            trimmed_text = text.strip()
            if len(text) <= 10 and len(text) > 0  and "lb" not in text:
                fruit_name = "name: " + text
                names.append(fruit_name)
            if lbs in text:
                fruit_weight = "weight: " + text
                weights.append(fruit_weight)