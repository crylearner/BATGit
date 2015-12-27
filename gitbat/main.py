'''
Created on 2012-6-30

@author: lenovo
'''

from gitbat.CommandComposer import createCommandFile
import optparse
import os
import sys


def main(REPO_FILE_NAME, CMD_FILE_NAME, ROOT_PATH=None):
    curr_path = os.path.dirname(sys.argv[0])
    if ROOT_PATH:   root_path = ROOT_PATH
    else: root_path = curr_path
    
    p = optparse.OptionParser()
    p.add_option("-c", "--command", action="store", type="string", dest="command")
    p.add_option("-e", "--execute", action="store_true", dest="execute", default=False)
    (opt, arg) = p.parse_args()
    gitCommand = opt.command
    toExecute = opt.execute
    print("git command:" + gitCommand)
    print("execute:" + str(opt.execute))
    print("root path:" + root_path)
    print("\n")
    
    if (not gitCommand) or gitCommand == '':
        print("no git command")
        return
    
    #create
    repoFilePath = os.path.join(curr_path, REPO_FILE_NAME)
    cmdFilePath = os.path.join(curr_path, CMD_FILE_NAME)
    createCommandFile(repoFilePath, gitCommand, cmdFilePath)
    
    #execute 
    if root_path != '':
        os.system("cd " + root_path)
            
    if toExecute:
        os.system("sh " + CMD_FILE_NAME)
                     
def test():
    CMD_FILE_NAME = r"gitbat.sh"
    REPO_FILE_NAME = r"repourl.txt"
    main(REPO_FILE_NAME, CMD_FILE_NAME)

#test()
#if __name__ == '__main__':
#    main()