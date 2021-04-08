import os
import glob
import shutil
import time

temp = 'C:/Windows/Temp/*'
percent_temp = 'C:/Users/your pc name here/AppData/Local/Temp/*'
prefetch = 'C:/Windows/Prefetch/*'

all_paths = [temp, percent_temp, prefetch]

for path in all_paths:
    file_paths = glob.glob(path, recursive=True)
    for file_path in file_paths:
        try:
            if os.path.exists(file_path):
                # shutil.rmtree(file_path)
                os.remove(file_path)
        except Exception as e:
            pass

os.system('cmd /c "tree"')
print('=====Done=====')
time.sleep(1)
