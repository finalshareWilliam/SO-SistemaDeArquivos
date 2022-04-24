from Filesize import Filesize
import os

def CreateInodeFile(name):
    path = os.getcwd()
    print(path)
    print(name)
    totalpath = os.path.join(path,name)
    name = 'INODE' + name # + 'txt'
    totalpath2 = os.path.join(path,name)

    if os.path.exists(totalpath2):
        print ("INODE EXISTS")

    else:
        f = open(totalpath2, 'w')
        print ("INODE CREATE")
        blocks = (int(Filesize(totalpath)/4096)) + \
            (Filesize(totalpath) % 4096 > 0)
        
        print("ARCHIVE SIZE " + str (Filesize(totalpath)))
        print("BUSY BLOCKS " + str(blocks))
        f.writelines ([(totalpath + '\n'), (str(blocks) + '\n')])
        f.write(str(os.stat(totalpath)) + '\n')
        f.close
