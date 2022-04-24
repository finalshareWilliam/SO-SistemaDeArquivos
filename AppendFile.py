import os
def AppendFile(name,content):
    path = os.getcwd()
    totalpath = os.path.join(path,name)

    if os.path.exists(totalpath):
        f=open(totalpath, "a")
        f.write(content)
        f.close
        print("CONCLUDED")
        
    else:
        print("NOT FOUND")