import os.path
import re

class WeChatGifDirFinder:
    _diskRootPath = ''
    def __init__(self, diskRootPath):
        self._diskRootPath = diskRootPath
    def findGifDir(self):
        path = self._diskRootPath + 'tencent/MicroMsg';
        if(os.path.exists(path) == False):
            return False
        ret = []
        files = os.listdir(path)
        for afile in files:
            if(re.match('^[0-9,a-f]{32}', afile) != None):
                ret.append(path + '/' + afile )
        return ret
            
        
