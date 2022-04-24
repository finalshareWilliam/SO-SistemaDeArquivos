import os

def SizeDir(path):
    path = os.getcwd()
    size = 0
    for filename in os.listdir(path):
        size += os.path.getsize(os.path.join(path, filename))
    print('DIRECTORY SIZE ' + str(size) + ' BYTES')
    return size