import os
import shutil


path="C:\\Users\\nasir\\"

downloads_path= "C:\\Users\\nasir\\Downloads\\"

files = os.listdir(downloads_path)

for file in files:
    try:
        if ".jpg" in file or ".jpeg" in file or ".png" in file:
            shutil.move(f"{downloads_path}{file}", f"{path}OneDrive\\Pictures") 
        elif ".pdf" in file or ".docx" in file or ".doc" in file:
            shutil.move(f"{downloads_path}{file}", f"{path}OneDrive\\Documents") 
        elif ".iso" in file: 
            shutil.move(f"{downloads_path}{file}", f"{path}OneDrive\\IsoFiles")    
        elif ".exe" in file:
            shutil.move(f"{downloads_path}{file}", f"{path}OneDrive\\myPrograms")
                           
    except shutil.Error:
        print(f"Error!\n shutil error: {file} already exists")
      