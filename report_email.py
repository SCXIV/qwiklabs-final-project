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