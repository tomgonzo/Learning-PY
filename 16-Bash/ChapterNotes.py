#Chapter 16 ChapterNotes! - Bash

#Bash is a command line interface - a program you type instructions into that
#the operating system executes. Bash is an implementation of CLI that comes
#with most Unix-like systems. CLI and Command-line are the same thing.

#The command-line is the "control center" for everything programmer do 
#that isn't writing code. 

#CLI, package managers, regular expressions, and version control are core
#tools in a programmer's arsenal. Professional programmers are expected to
#be proficient with them.

#In programming documentation, Whenever you see a dollar sign followed
# by a command, it means you need to type the command into the CLI.

#echo to bash is like print to Python. 


Recent Commands!
#See recently typed commands in bash by pressing up or down arrow. View a list
#with the command history.

Relative vs Absolute Paths
#An OS is made up of directories and files. A directory is another word for a
#folder on your computer. All directories and files have a path, an address
#where the directory or file exists in the OS.

#When using Bash, you are always in a directory. Use the command pwd, which stands
#for print working directory, to print the directory you are in.

#Your OS represents directories, and your directory location, with a tree. In 
#computer science, a tree is an important concept called a data structure.
#In a tree, there is a root at the top. Roots can have branches, which have 
#more branches, ad infinitum.

#When using bash, you are at a location on your operating system's tree. A path
#is a way of expressing that location. There are two ways to give the path of a file
#or directory on an Unix operating system: an absolute path and a relative path.

Absolute Paths
#An absolute path gives the location of a file or directory starting from root.
#It is made up of the name of directories in the tree, in order of their proximity
#to the tree's root, separated by forward slashes. first slash represents the root

Relative Paths
#Another way of specifying a location on your computer is a relative path. Instead
#of starting at the rot directory, a relative path starts with the current working
#directory. If the path does not begin with a forward slash, bash knows you're 
#working with a relative path. 


Navigating!
#Navigate directories by passing the command cd an absolute or relative path.
#Enter the cd command followed by the absolute path / to navigate the root dir.

$ cd /

#The list directory command, ls, prints the directories and folders in the current
#working directory. 

$ ls

#Create a new directory by passing a name to the mkdir command. Directory names 
#cannot have spaces in them.

$ mkdir folder_name

#Move back up one directory (level up in the tree) by passing two pertiods to cd

$ cd ..

#Delete a directory with the remove directory command, rmdir.

$ rmdir folder_name

Flags!
#Commands have a concept called flags that allow the issuer to change its behavior.
#Flags are options for commands that can have a value of either True or False.

#By defaults, all of a command's flags start set to False. If you add a flag, bash sets
#the value to True and the behavior changes. To set a flag, depending on the OS, use - or --
#For example, add --author to the ls command to set the author flag to true.

#On Unix, use one hyphen.
#On Linux, use two hyphens.

ls -author

#This command will print not only the directories and files, but also the creator.

Hidden Files!
#OS and programs store data in hidden files. Hidden files, by default, are not shown
#to users because changing them could affect the programs that depend on them.

#hidden files that with a period. View hidden files by adding the flag -a, which 
#stands for all, to the ls command. The command touch creates a new file.

touch .self-taught >> creates a new hidden file 

Pipes!
#In Unix-like OS, the vertical bar | is called a pipe. Use a pipe to pass the output
#of a command to another command as its input. For example, you can use the output
#of the ls command as the imput of the less command.

Environmental Variables!
#Env Vars are variables, stored in the PS, that prorams use to get data about the 
#environment they are running in such as the name of the computer the program is
#running on or the name of the OS user running the program. 

#Create a new environmental variables in bash with the syntax 

export variable_name=[variable_value]

#To reference an environmental variable in Bash, put $ in front of its name.

export x=100
echo $x

>> 100

#Environmental variables created like this only exist in the Bash window it was 
#created in. If you exit the window, and try printing it again, it won't work.

#Environmental Variables can be persisted by adding them to hidden files used by 
#Unix-like OS, located in the home directory, called .profile

#Environmental Variables will persist as long as they're in the .profile file.

Users!
#Operating Systems can have multiple users. A user is a person that uses the
#operating systems. Each user has a set of permissions. Print the name of the
#current OS user with the command whoami

whoami

#The user created when installing the OS is not the most powerful user. The 
#highest level user is called the root user. Every system has a ropt user that
#can create and delete other users. 

#Precede commands you need to issue as the root user with the command sudo
#Sudo (superuser do) allowed issuing commands as the root user without actually
#logging in as the root user.

#Never issue a command with sudo unless you are confident in your command.



