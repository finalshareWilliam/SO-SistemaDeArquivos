import os

def RenameFileDir(name,target):
    path = os.getcwd()
    totalpath = os.path.join(path,name)
    totalpath2 = os.path.join(path,target)

    try:
        os.rename(totalpath, totalpath2)
    except OSError:
        print("FOLDER RENAMING ERROR" % totalpath)
    
    else:
        print("FOLDER RENAME SUCCESSFUL")

        