# syncer
Sync directories with rsync and python

This is probably the most naive software you can find. It serves the purpose of familiarising myself with python and git/github.

This software syncs directories specified in a file called "directories".
You can create this file yourself and specify directories with the syntax 'index source destination' seperated by tab.
Alternatively this program can create the file.


    Command:    Explanation:    
    
    ´add´         Add a directory to directories file.
    ´rm´          Removes a directory from the directories file.
    read        Read a directories file.
    sync -a     Sync all directories specified in directories file.
    help        Show this help message.