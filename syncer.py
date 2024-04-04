import sys
from math import floor, ceil
import os
import shutil   # For file operations
import subprocess   # to run external commands as processes
import csv
import methods as m
import getpass

directories = []
new_directory = []
command = ''
username = getpass.getuser()

m.welcome()
directories = m.CheckDirFile()

while command != 'exit':
    try:
        command = input(username+"@syncer~: ")
    except EOFError:
        print("Syncer program exited by ctrl+d.")
        break
    except KeyboardInterrupt:
        print("Syncer program exited by ctrl+c.")
        break
    if command == 'add':
        new_directory = m.addDirectory()
        directories = m.UpdateDirectories(directories, new_directory)
        m.UpdateDirFile(directories)
    elif command == 'rm':
        directories = m.remDirectory(directories)
        m.UpdateDirFile(directories)
    elif command == 'sync -a':
        print("Syncing all directories with rsync...")
        m.SyncAll(directories)
    elif command == 'sync':
        m.List(directories)
        n=int(input("Please specify the desired directories:"))-1
        m.Sync(directories, n)
    elif command == 'list':
        m.List(directories)
    elif command =='help':
        m.help()  
    elif command =='exit':
        break
    else:
        print("Command unknown.")



    #with open('directories', 'w') as f:
    #   for l in range(len(directories)):
    #      f.write(directories[l])

    #with open('directories', 'r') as f:
    #   print(f.read())