import os
for currentdir, dirnames, filenames in os.walk('.'):
    print(filenames)