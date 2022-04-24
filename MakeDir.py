import os

def MakeDir(name):
    path = os.getcwd()
    totalpath = os.path.join(path,name)

    try:
        if(name=='root'):
            raise Exception ("INVALID NAME")

        else:
            os.mkdir(totalpath)
    
    except Exception as e:
        print("ERROR" % e)
    except OSError:
        print("ERROR CREATION FOLDER" % totalpath)
    
    else:
        print("FOLDER CREATED SUCESSFULLY")