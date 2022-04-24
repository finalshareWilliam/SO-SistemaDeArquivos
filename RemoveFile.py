import os

def RemoveFile(name):
    path = os.getcwd()
    totalpath = os.path.join(path,name)

    if os.path.exists(totalpath):
        os.remove(totalpath)

    else:
        print("ARCHIVE NOT FOUND")
