'''
Created on 2012-6-29

@author: yaoyufei
'''
import re
Host="(https://android.googlesource.com/|https://android.googlesource.com/a/m/)"
RepoUrlPattern = re.compile(r'(.*)'+ Host + r'(.+)')
class RepoUrlParser(object):
    '''
    parse host and repo path from the url. 
    e.g. given a url like "git clone https://android.googlesource.com/platform/packages/apps/Browser"
    then getRepoPath() return platform/packages/apps/Browser
         getWebsite() return  https://android.googlesource.com/
    '''


    def __init__(self, repoUrl):
        '''
        Constructor
        @param repoUrl: url of repository  
        '''
        m = RepoUrlPattern.match(repoUrl)
        if not m:
            print("Unknown RepositoryURL: " + repoUrl + '\n')
            self.isvalid = False
            self.website = None
            self.repoPath = None
        else:
            #print("a valid repo url")
            self.isvalid = True
            self.website = m.group(2)
            self.repoPath = m.group(3)
            self.repoPath = self.__removeCRAtTail(self.repoPath)
    
   
    def isValid(self): 
        '''
        return if is a valid repository url
        '''
        return self.isvalid        
            
    
    def getRepoPath(self):
        '''
        get path of repository    
        '''    
        return self.repoPath
    
    
    def getWebsite(self):
        '''
        get www source server of repository    
        '''    
        return self.website
 
 
    def __removeCRAtTail(self, path):
        if path.endswith('\n'):
            #remove '\n' at tail
            return path[:-1]
        else:
            return path
        
def test():
    url = r"git clone https://android.googlesource.com/platform/packages/apps/Browser"
    repourl = RepoUrlParser(url)
    print(repourl.getRepoPath())
    print(repourl.getWebsite())


if __name__ == "__main__":
    test()
    
            