#!/bin/bash

# set the STRING variable
STRING="Hello World!"
# print the contents of the variable on screen
echo $STRING

read -r -p 'Commit message: ' desc  # prompt user for commit message
git status
git add .                           # track all files
git add -u                          # track deletes
git commit -m "$desc"               # commit with message
git push origin master              # push to origin

python hello.py

function create() {
    cd ~/Desktop/
}