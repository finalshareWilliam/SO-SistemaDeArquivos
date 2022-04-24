from typing import Text
from AppendFile import*
from ChangeDir import*
from CopyFile import*
from CreateFile import*
from DeleteDir import*
from MakeDir import*
from ReadFile import*
from RemoveFile import*
from RenameFileDir import*
from UpdateInode import*
from SizeDir import*
from CreateInode import*

import re

def Treatment (input):

    command = input.split()

    if (len(command) < 2):
        return ()
    if (command[0] == 'SHUTDOWN'):
        return(True)

    if (command[0] == 'touch'):
        CreateFile(command[1])
        CreateInodeFile(command[1])
        SizeDir(command[1])

    if (command[0] == 'rm'):
        RemoveFile(command[1])

    if (command[0] == 'echo'):
        text = re.findall(r'"([^"]*)"', input)
        AppendFile(command[-1], text[0])
        UpdateInodeFile(command[-1])

    if (command[0] == 'cat'):
        ReadFile(command[1])

    if (command[0] == 'cp'):
        if (len(command) == 3):
            CopyFile(command[1], command[2])

    if (command[0] == 'mv'):
        if (len(command) == 3):
            RenameFileDir(command[1], command[2])

    if (command[0] == 'mkdir'):
        MakeDir(command[1])

    if (command[0] == 'rmdir'):
        DeleteDir(command[1])

    if (command[0] == 'cd'):
        ChangeDir(command[1])

    if (command[0] == '.'):
        ChangeDir(command[1])
        
    if (command[0] == '..'):
        ChangeDir(command[1])