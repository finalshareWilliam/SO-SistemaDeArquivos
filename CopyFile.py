import os
import shutil

def CopyFile(name,target):
    path = os.getcwd()
    totalpath = os.path.join(path,name)
    totalpath2 = os.path.join(path,target)

    try:
        shutil.copy(totalpath, totalpath2)
    except IOError as error:
        print("ERROR IN COPYING FILE" % error)

    else:
        print("FILE COPIED SUCCESSFULLY")
