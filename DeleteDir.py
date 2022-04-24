import os

def DeleteDir(name):
    path = os.getcwd()
    totalpath = os.path.join(path,name)
    
    try:
        os.rmdir(totalpath)
    
    except OSError:
        print ("FAILED TO DELETE FOLDER" % totalpath)

    else: 
        print ("FOLDER DELETED SUCCESSFULLY")