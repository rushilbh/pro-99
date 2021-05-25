import os,time,sys
import shutil
import os.path
from os import path
directory=input("please provide directory path:-")
pathToDelete='/Users/rushil/Documents/Test folder/' + directory
r=os.listdir(pathToDelete)
now=time.time()
for value in r:
     print(path.join(pathToDelete, value))
     print("Current file modified time is:-"+str(os.stat(path.join(pathToDelete, value)).st_mtime))
     n=str(now)
     print("Current system time in seconds is:-"+n)
     if((path.exists(path.join(pathToDelete, value)))):
         if os.stat(path.join(pathToDelete, value)).st_mtime < now - 7 * 86400:
           if path.isfile(value):
             os.remove(path.join(pathToDelete, value))
