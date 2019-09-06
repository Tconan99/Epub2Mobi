#!/usr/local/bin/python3

import os
import subprocess
import time

toolPath = '/Users/tconan/A.Document/book/epub2mobi/KindleGen_Mac_i386_v2_9/kindlegen'

filePath = '/Users/tconan/A.Document/book/'
files = os.listdir(filePath)

epubFiles = list(filter(lambda file: file.endswith('.epub'), files))

total = len(epubFiles)
index = 1

filterFiles = []
for file in epubFiles:
    epubName = file
    mobiName = epubName.replace('.epub', '.mobi')
    if file.endswith('.epub') and not os.path.exists(filePath + mobiName):
        filterFiles.append(file)

total = len(filterFiles)
index = 1

logfile = open('logfile', 'a+')
logfile.write('\n')
logfile.write('\n')
logfile.write('---------------------------------------------------------')
logfile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

for file in filterFiles:
    print(str(index) + '/' + str(total))
    epubName = file
    mobiName = epubName.replace('.epub', '.mobi')
    cmd = toolPath + ' "' + filePath + epubName + '"'
    print(filePath + epubName)
    subprocess.call(cmd, shell=True, stdout=logfile)
    index += 1
    if not os.path.exists(filePath + mobiName):
        print('转化失败')
    # break
    
logfile.close()
print("end")