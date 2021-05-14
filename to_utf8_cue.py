#This script find all the cue file under current folder and covert it to utf8 encoding
#make sure you have relative module installed
# Import the os module, for the os.walk function
import os
from chardet import detect

# Set the directory you want to start from
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
        if "cue" in fname:
            fullname = "{0}\{1}".format(dirName,fname)

            coding = ""
            with open(fullname, 'rb') as f:
                rawdata = f.read()
                coding = detect(rawdata)['encoding']
                if coding is None:
                    print("!!!!!Can not convert: {}", fullname)
                    continue
                if "2312" in coding:
                    coding = "gb18030"
            trgfile = "{0}\{1}.back".format(dirName,fname)
            srcfile = fullname
            with open(srcfile, 'r', encoding=coding) as f, open(trgfile, 'w', encoding='utf-8-sig') as e:
                text = f.read() # for small files, for big use chunks
                e.write(text)

            os.remove(fullname) # remove old encoding file
            os.rename(trgfile, srcfile) # rename new encoding
            print("Success {}".format(fullname))
            
 
