# Connect a remote connection to local git repo
```cmd
git init
git add .
git commit -m "First commit"
git remote add origin remote repository https://github.com/user/repo.git
git remote -v
git push origin master
```

# These are the most used git commands available

## Basic cmd Commands
```cmd
> ls 
    - to show the content in the directory 
> dir 
    - to show the content in the directory 
> pwd 
    - to know the current directory
> mkdir folder_name 
    - to make a new folder
> mkdir folder1/folder2/folder3
    - to create folder with children
> cd folder_name 
    - to change directory to folder name
> cd ..
    - to go back one directory
> cd ../..
    - to go back two directories
> cd ~
    - to go back home
> cd \ - to go back to drive E.g. C:\
> cat start.txt
    - to read the content of a file
> echo "Test Git Quick Start demo" >>  start.txt 
    - to create a file
> ren 
    - to rename a file or folder
> rmdir folder_path -r -force
    - to remove the entire folder
    even when it has files in it
    no prompt, no warnings
> rm file_name
    - to remove a file
> rm file_name -r -force
    - to recursively force remove a file
> rmdir .git -r -force
    - to remove the repository
```
## Basic bash-only Commands
```bash
> ls -al
    - to show all files including .git files
> rm -rf folder_name
    - to remove the entire folder 
    even when it has files in it
    no prompt, no warnings
> rm -rf .git
    - to remove the repository
```

## Basic git Commands
```cmd
> git 
    - to show the available commands
> git version 
    - to show the current version of git
> git config --global user.name "Abe > Lincoln" 
    - to configure the name of the user
> git config --global user.email > "mrabe@host.com" 
    - to configure the email of the user
> git config --global --list 
    - to describe the configuration of the user
> git clone git-https-url 
    - to clone a repository host in the cloud
> git remote add origin git-htpps-url
    - to link a remote repository to a local repository
> git remote -v
    - to verify the remote url
> git push -u origin master
    - to have Branch 'master' set up to track remote 
    branch 'master' from 'origin'
> git init
    - to start a new repository from inside
    the project's folder
> git init new-project 
    - to start a new folder and project 
> git rm itemname
    - to remove a folder or file  tracked by git
> git rm -f itemname
    - to force remove a folder or file staged by git
> git rm --cached <file>
    - to remove tracked files
> git rm -r --cached <folder>
    - to remove tracked folders and files
> git config --global alias.aliasname "long git command"
> git config --global alias.hist "log --all --graph -- decorate --oneline"
    - to  show summary of commit by using just alias
> notepad.exe .gitconfig
    - to open the configuration file in notepad
```

## Tracking Changes Commands
```cmd
> git log
    - to show the whole history of commands
    (use q to get out)
> git --abbrev-commit
    - to shorten the commit id 
> git log --oneline --graph --decorate  
    - summary of all commits
> git log commitid...commitid
    - to slice the commits to show
> git log --since="n days ago" 
    - to slice by the range of days
    (n is the number of days)
> git log -- filename
    - to show the history of an specific file
> git log --follow -- itemname
    - to see the trail of renames etc.
> git show commitid
    - to see the specific changes made in the commit
> git status
    - to check the status of the branch
> git add file.txt
    - to transfer the file to the staging area
> git add .
    - to recursively add all files to the 
    staging area
> git add -all
    - to add all changes to a file or folders into staging
> git mv filename.txt newfilename.txt
    - to move or rename a file and have 
    only one process in staging
> git commit -m "Adding start text file"
    - to transfer the file to the .git folder 
    (repository)
> git commit -am "Adding and commit"
    - to transfer the file directly to the .git folder
    (it will only work for tracke files)
> git ls-files
    - to know which file are being tracked
    (tracked=uploaded to the remote repository)
> git reset HEAD file.txt
    - unstages the stated file
> git reset HEAD .
    - unstages all staged files
> git checkout file.txt
    - to discard any changes made to the file
> git restore file.txt
    - to discard any changes made to the file
> git restore . --staged
    - to discard all changes on stage
> git restore file.txt --staged
    - to discard any changes made to a file
> git push origin master
    - to push the repository the the cloned 
    cloud source
> git pull origin master
    - to pull from the remote repository to local
> git pull --rebase origin master
    - to rebase on top of the local repository from remote
> git fetch origin master
    - to simply update references between local and remote
> notepad.exe .gitignore
    - to create the exclussion file
    *.csv will ignore all csv files
    *.txt will ignore all txt files
    etc.
```

## Setting Merge and Diff Tool
First, we need to install p4merge (Helix Visual Merge Tool)
1. Check only Helix Visual Merge Tool on the installation gui
1. Look for the Perforce path -default C:\Program Files\Perforce\p4merge.exe
1. Add it to the system environment variable path
1. Use > p4merge in the cmd to test configuration
1. Follow the below instruction in cmd to configure p4merge with git

```cmd
> git config --global merge.tool p4merge
> git config --global mergetool.p4merge.path "C:\Program Files\Perforce\p4merge.exe"
> git config --global mergetool.prompt false
> notepad.exe .gitconfig
> git config --global diff.tool p4merge
> git config --global difftool.p4merge.path "C:\Program Files\Perforce\p4merge.exe"
> git config --global difftool.prompt false
```

```cmd
> git difftool
    - to show differences from working to stage using the visual tool
> git difftool HEAD
    - to show differences from working to head using the visual tool
> git diff
    - to show differences from working to stage
> git diff HEAD
    - to show differences from working to head
```
<<<<<<< HEAD

## Branching and Mergin Commands
```cmd
> git branch -a
> git branch --all
    - to show all available branches including origin master
> git branch mynewbranch
    - to create a new branch
> git checkout mynewbranch
    - to change to another branch
> git checkout -b mynewbranch
    - to create and change to the new branch
> git branch mynewbranch newbranch
    - to change the name of the branch
> git branch -d delbranch
    - to delete a branch (not from same branch)
> git diff master anyotherbranch
    - to compare staged commits with the master before mergin
> git merge anyotherbranch
    - to merge any other branch to the active branch
> git merge anyotherbranch --no-ff
    _ to merge with not fast forward
```

## Rebasing
```cmd
> git rebase master
    - to rebase from master to newbranch
> git rebase newbranch
    - to rebase from newbranch to master
> git rebase --abort
    - to abort the rebase when conflicting
```

## Mergin Terminology
Fast Forward Branch - it happes when there is no commits on the master branch and any other branch is merged in continuation from the time the other brach was separated from the master.
=======
>>>>>>> c75ef2fe3add431009a6aa917f52fb9d115f1b0e
