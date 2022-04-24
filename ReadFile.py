import os

def ReadFile(name):
    path = os.getcwd()
    totalpath = os.path.join(path,name)

    if os.path.exists(totalpath):
        f=open(totalpath, "r")
        print(f.read())
        f.close

    else:
        print("ARCHIVE NOT FOUND")
