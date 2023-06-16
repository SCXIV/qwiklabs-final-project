#!/usr/bin/env python3

import os
from PIL import Image
from pathlib import Path

directory = "./supplier-data/images/"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if f.endswith('.jpg'):
        # The next two lines of code both removes the extension from the file name, then adds the new one
        trimmed_name = Path(f).stem
        revised_name = trimmed_name + ".jpeg"

        # Opens image file, then converts it to given format
        image = Image.open(f)
        image.resize((600, 400)).convert("RGB").save("{}{}".format(directory, revised_name), "JPEG")

        print("Successfully converted image file")
