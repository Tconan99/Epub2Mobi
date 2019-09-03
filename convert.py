#!/usr/local/bin/python3

import os
import subprocess

toolPath = '/Users/tconan/A.Document/book/epub2mobi/KindleGen_Mac_i386_v2_9/kindlegen'

filePath = '/Users/tconan/A.Document/book/'
files = os.listdir(filePath)

epubFiles = list(filter(lambda file: file.endswith('.epub'), files))

total = len(epubFiles)
index = 1

for file in epubFiles:
    print(str(index) + '/' + str(total))

    epubName = file
    mobiName = epubName.replace('.epub', 'mobi')

    if os.path.exists(mobiName):
        continue

    cmd = toolPath + ' "' + filePath + epubName + '"'
    print(cmd)
    subprocess.call(cmd, shell=True)
    index += 1
    # break
    
print("end")