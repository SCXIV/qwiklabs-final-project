#!/usr/bin/env python3

import os
import requests
from pathlib import Path

fruits = {}
keys = ["name", "weight", "description", "image_name"]
index = 0
directory = "./supplier-data/descriptions/"
image_directory = "./supplier-data/images/"

