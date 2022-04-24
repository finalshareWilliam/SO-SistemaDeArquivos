import os
def ChangeDir(name):
    path = os.getcwd()
    root = 'root'
    last = path.split('\\')

    try:
        if(len(name) >= 2):
            if(name[0] == '.' and name[1] == '.' and len(name)<3 and last[-1] != root):
                os.chdir(name)
            elif(name[0] != '.' and name[1] != '.'):
                os.chdir(name)
            else:
                raise Exception("SOURCE")

        elif(name[0] == '.'):
            print(path)
        else:
            os.chdir(name)

    except Exception as e:
        print("ERROR 404:" % e)
    except OSError:
        print("ARCHIVE NOT FOUND")

    else:
        print("ARCHIVE FOUND")