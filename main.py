import os
import shutil


path="C:\\Users\\nasir\\"

downloads_path= "C:\\Users\\nasir\\Downloads\\"

files = os.listdir(downloads_path)

for file in files:
    if ".jpg" in file or ".png" in file:
        shutil.move(f"{downloads_path}{file}", f"{path}Pictures") 
