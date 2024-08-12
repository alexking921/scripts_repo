#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import sys
import os


### MODULES...###
# 1. Sys Module: 
# 2. Os Module: (operating sys stuff + folder manipulations)
# 3. Subprocess Module:
# 4. Math Module:
# 5. Random Module:
# 6. Date Time Module:
# 7. JSON Module:
# ... ??? 

## DONT FORGET TO USE PROPER EXCEPTION HANDLING!! ## 



print("HELLOworld!!")
print(sys.version)
print(sys.argv)




print(os.getcwd)
# os.chdir("/Users/alexking") # change directory to given path
# os.mkdir("/Users/alexking/tempDeleteMeFolder") # create dir at the given path location
# os.rmdir("/Users/alexking/tempDeleteMeFolder") # create dir at the given path location
# os.remove("/Users/alexking/THE_FILE_I_WANT_TO_DELETE") # delete a FILE...
print(os.path.exists("/Users/alexking/tempDeleteMeFolder")) # return TRUE/FALSE if given path exists

