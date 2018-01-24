#Chapter 19 - Version Control ChapterNotes

#Writing software is a team sport - when working with others you all 
#need to be able to change the codebase and keep those changes synced.

#Version control helps collaborate on projects with other programmers.

#Git and SVN are two popular version control systems. 
#Let's play with Git and GitHub!

### Repositories! ###
#A repository is a data structure created by a version control system.
#A data structure is a way of organizing and storing information:
#Lists and dictionaries are examples of data structures. 

#Typically when working on a project managed by Git, there will be 
#multiple repositories, one for each person working on it.

#Everybody has a repository on their computer called a local repository,
#this tracks all the changes they've made to the project.

#There is also a central repository, hosted on a site like GitHub, that
#all local repositories communicate with to stay in sync. 

### Git! ###

#Use an URL to download a repo to the computer with the git clone command.

git clone [repo_URL]

### Pushing and Pulling
#Pushing - updating the central repo with changes from the local repo
#Pulling - updating local repo with changes from central repo

#To see the URL of the repo you're pushing to and pulling from:
git remote -v

### Pushing Example ###

# Changes are pushed from local to central in three steps.

#Use this command to show the current state of the project in relation
#to the central repository:

git status

#First, stage the files. Tell Git which files you want to push. 
#The filename will show green when the file is staged.

git add [filename]

#Git status can then be used to confirm the file is staged. You could
#unstage the file using:

git reset [filename]

#then confirm the file was unstaged with:

git status

#Once the files are staged, commit the files:
#Create a commit, then add a message to help remember the changes made.

git commit -m [message]

#Once commited, you're ready for the final step.
#Push changes to the central repo using:

git push origin master

#The command line will ask for username and password, then push changes.

### Pulling Example ###

#In this example, we'll update the local repo by pulling changes from central.
#Update the local repo with changes from the central repo with:

git pull origin master

#This will cause Git to apply changes from central to local repo.


### Reverting Versions ###

#Git saves the project each time a file is commited. It also allows reverting
#to any previous commit, essentially "rewinding" the project.

#Each commit has a commit number: a unique sequence used to identify it.
#View project history of commits with the command:

git log

#You can switch your project to another commit by passing a commit number
#to the command:

git checkout [commit number]

### diff! ###

#You can show differences between a file in local vs central using:

git diff [filename]






