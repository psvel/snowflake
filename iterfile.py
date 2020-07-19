import os
import sys

rootdir =  sys.argv[1]

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(file)
