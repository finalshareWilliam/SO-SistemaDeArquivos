from Filesize import Filesize
import os

def UpdateInodeFile(name):
    path = os.getcwd()
    totalpath = os.path.join(path,name)
    name = 'INODE' + name # + 'TXT'
    totalpath2 = os.path.join(path,name)

    if os.path.exists(totalpath2):
        f = (open(totalpath2, "w"))
        blocks = (int(Filesize(totalpath)/4096)) + \
            (Filesize(totalpath) % 4096 > 0)

        f.writelines([(totalpath + '\n'), (str(blocks) + '\n')])
        f.write(str(os.stat(totalpath)) + '\n')
        print("INODE UPDATED")
        print("ARCHIVE SIZE " + str(Filesize(totalpath)))
        print("BUSY BLOCKS " + str(blocks))
        f.close

    else:
        print ("INODE NOT FOUND")
        
