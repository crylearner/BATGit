'''
Created on 2012-6-29

@author: yaoyufei
'''
from gitbat.RepositoryUrlParser import RepoUrlParser
import os



def composeCommandForOneRepository(repoUrl, gitCommand):
    '''
    Compose shell command for one group
    @param repoUrl: RepoUrlParser object
    @param gitCommond: git command need to execute 
    '''
    # if possible, should check if is root path
    pass

    if gitCommand.startswith("git clone"):
        command = composeGitCloneCommand(repoUrl, gitCommand)
    else:
        command = composeGitCommand(repoUrl, gitCommand)            
    
    return command


def composeGitCommand(repoUrl, gitCommand):
    '''
    Compose shell command for one group
    @param repoUrl: RepoUrlParser object
    @param gitCommond: git command need to execute. 
    these command are all executed in the repository path.
    '''
    command = ''
    pathToExcuteCmd = repoUrl.getRepoPath()    
    # entry path to execute git command
    if pathToExcuteCmd != '':
        command += "echo " + "cd " + pathToExcuteCmd+ '\n'
        command += "cd " + pathToExcuteCmd+ '\n'
    # do git command
    command += "echo " + gitCommand + '\n'
    command += gitCommand + '\n'    
    # quit to root 
    if pathToExcuteCmd != '':
        #command += "echo " + "cd -" + '\n'
        command += "cd -" + '\n'
    
    return command    


def composeGitCloneCommand(repoUrl, gitCommand):
    '''
    for git clone, it is different with other git command.
    @param repoUrl: RepoUrlParser object
    @param gitCommand: git command. if git command does not starts with "git clone"
    then, it will return empty ''. Besides, it will always discard any infomation
    at the tail of "git clone"
    '''
    command = ''
    if not gitCommand.startswith("git clone"):
        print("warning: not git clone ")
        return command
    
    #for git clone, excute path should be up-level directory of repoPath
    pathToExcuteCmd = os.path.split(repoUrl.getRepoPath())[0]
    
    if pathToExcuteCmd != '':
        command += "echo " + "mkdir -p " + pathToExcuteCmd + '\n'
        command += "mkdir -p " + pathToExcuteCmd + '\n'
        command += "echo " + "cd " + pathToExcuteCmd+ '\n'
        command += "cd " + pathToExcuteCmd+ '\n'
    # do git command
    command += "echo " + gitCommand + " " + repoUrl.getWebsite() + repoUrl.getRepoPath() + '\n'
    command += gitCommand + " " + repoUrl.getWebsite() + repoUrl.getRepoPath() + '\n'
    # quit to root
    if pathToExcuteCmd != '':
        #command += "echo " + "cd -" + '\n'
        command += "cd -" + '\n'
        
    return command

 
def createCommandFile(repoURLFilePath, gitCommand, cmdFilePath):
    '''
    Create shell command file, which is composed by each repository
    @param repoURLFilePath: path of file include each repository url 
    @param gitCommond: git command to be execute
    @param cmdFilePath: path of shell command file which will be created 
    '''   
    repoURLFile = open(repoURLFilePath, 'r')
    cmdFile = open(cmdFilePath, 'w')
    
    for line in repoURLFile:
        repoUrl = RepoUrlParser(line)
        if not repoUrl.isValid():    continue
        command = composeCommandForOneRepository(repoUrl, gitCommand)
        cmdFile.write(command)
        cmdFile.write("\n")
    
    cmdFile.close()
    repoURLFile.close()



def test():
    url = r"git clone https://android.googlesource.com/platform/packages/apps/Browser"
    repourl = RepoUrlParser(url)
    command = composeCommandForOneRepository(repourl, "git clone")
    print(command)
    
    command = composeCommandForOneRepository(repourl, "git pull")
    print(command)
  
    
if __name__ == "__main__":
    test()