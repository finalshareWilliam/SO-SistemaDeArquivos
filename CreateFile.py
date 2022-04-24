import os
def CreateFile(name):
    path = os.getcwd()
    totalpath = os.path.join(path,name)

    if os.path.exists(totalpath):
        print ("EXISTING ARCHIVE")

    else:
        f=open(totalpath, "x")
        print ("ARCHIVE CREATE")
        f.close
        