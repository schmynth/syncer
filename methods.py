import os
import subprocess

#test comment test branch

FileExists=False
index = 1

def welcome():
    welcome = """   Welcome to the syncer! 
    This program can sync directories.
    To add a directory to directories file, type "add".
    To read a directories file, type "read".
    To sync all directories in directories file, type "sync -a".
    To display help message, type "help".
    Checking if directories file exists..."""
    print(welcome)
    
def help():
    help = """  This software syncs directories specified in a file called "directories".
    You can create this file yourself and specify directories with the syntax 'index source destination' seperated by tab.
    Alternatively this program can create the file.
    
    Command:    Explanation:    
    
    add         Add a directory to directories file.
    rm          Removes a directory from the directories file.
    read        Read a directories file.
    sync -a     Sync all directories specified in directories file.
    help        Show this help message."""
    print(help)
    
def CheckDirFile():
    global FileExists
    if os.path.isfile('directories'):       #checks if directories file exists. If so, adding contents to directories list in program memory.
        print("directories file detected")
        #global FileExists
        directories = []
        FileExists = True
        with open('directories', 'r') as file:
            for line in file:
                items = line.rstrip('\r\n').split('\t')   #strip new-line characters and split on column delimiter
                items = [item.strip() for item in items]
                directories.append(items)
        global index
        for directory in directories:
            directory[0]=index
            index += 1
        return directories
    else:
        print("No directories file found. File will be created.")
        directories = []
        #global FileExists
        FileExists = True
        return directories
        
def UpdateDirFile(directories):
    with open('directories', 'w') as file:
        for item in directories:
            file.write(str(item[0])+'\t'+item[1]+'\t'+item[2]+'\n')

def UpdateDirectories(directories, new_directory):
    directories.append(new_directory)
    return directories
                
def List(directories):
    if FileExists == True:
        print("Listing all directories in directories file:")
        for directory in directories:
            print("Source directory No.",directory[0], ":", directory[1], "destination directory No.", directory[0], ":", directory[2])
    else:
        print("No directories file found.")    
           
def addDirectory():
    global index
    source = input("Input your source directory:")
    if os.path.isdir(source):
        print("Source directory", source, "added.")
    else:
        create='empty'
        while create!='y' and create!='n':
            print("The directory you entered does not exist on this system. Do you want to create it? y/n")
            create=input()
            if create == 'y':
                os.mkdir(source)
                print("Source directory", source, "created and added to directories file.")
            elif create == 'n':
                print("Creation of directory cancelled.")
            else:
                print("Wrong input. y/n:")            
    dest = input("Input your destination directory:")
    if os.path.isdir(dest):
        print("Destination directory", dest, "added.")
    else:
        print("The directory you entered does not exist. Do you want to create it? y/n")
        create=input()
        if create == 'y':
            os.mkdir(dest)
            print("Destination directory", dest, "created and added to directories file.")
    new_directory = [index, source, dest]
    index += 1
    return new_directory    

def remDirectory(directories):
    List(directories)
    n = int(input("Which directory do you want to remove from directories file? Directories on disk will be left unchanged."))
    del(directories[n-1])
    return directories
    
def SyncAll(directories):
    for item in directories:
        print("Syncing", item[1], "to", item[2], "with rsync", '\n')
        try:
            subprocess.run(['rsync', '-va', item[1], item[2]])
        except FileNotFoundError:
            print("rsync not found. rsync has to be installed to use this syncer.")
            break
        
def Sync(directories, n):
    print("Syncing", directories[n][1], "to", directories[n][2], "with rsync", '\n')
    #try:
    subprocess.run(['rsync', '-va', directories[n][1], directories[n][2]]) 
    #except
    
      
# # todo:
# # actual syncing