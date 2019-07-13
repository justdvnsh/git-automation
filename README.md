## Git Automation Script

This is an automation script which automates my git tasks like creating a folder for the project then , making the repo on github , intializing the readme files and init files . then pushing the code over .

The script.py has all the automations done which - 
- Opens up chrome 
- fills in the username and password
- creates a new repo
- writes a repo title
- creates the repository

The main script is the create script , which is a shell script , which actually -
- makes the dir
- initializes git init
- initializes readme file
- runs the python script
- and finally pushes it all over

The git-deploy script is for the later on tasks, i.e. when the project has made some progress and I dont want to run those boring commands over and over again. So this script -
- checks the git status
- adds the files of the current dir
- commits , with the commit message taken as a user prompt
- pushes it all over

---

## Usage 

You are free to use this tool anytime you like . Just pull issues in the issues section if you feel something can be added or something is not working . 

This will help me and other developers using this script .

---

#### Thank You !