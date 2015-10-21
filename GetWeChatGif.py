import os
import os.path
import re
import shutil

class GetWeChatGif:
    _sourcePath = ''
    _destPath = ''
    _count = 0
    
    def setSourceAndDest(self, sourcePath, destPath):
        self._sourcePath = sourcePath
        self._destPath = destPath
    def get(self):
        self._go(self._sourcePath)
    def _go(self, dirName):
        files = os.listdir(dirName)
        fileMap = {}
        for afile in files:
            fullPath = dirName + '/' + afile;
            if(os.path.isdir(fullPath)):
                self._makeDestDir(fullPath)
                self._go(fullPath )
            else:
                key = self._getFileNamePrefix(afile)
                if(fileMap.has_key(key) != True):
                    fileMap[key] = []
                fileMap[key].append(afile)
        for key in fileMap.keys():
            destFileName = dirName + '/' + fileMap[key][0];
            destFileName = destFileName.replace(self._sourcePath, self._destPath)
            fileListSize = len(fileMap[key])
            if(fileListSize == 1):
                destFileName += '.jpg'
            elif(fileListSize > 1):
                destFileName += '.gif'
            else:
                continue
            if(os.path.exists(dirName + '/' + key)):
                shutil.copyfile(dirName + '/' + key, destFileName)
            self._count += 1
    def _makeDestDir(self, sourceFullPath):
        halfPath = sourceFullPath[len(self._sourcePath):]
        fullPath = self._destPath + halfPath
        os.mkdir(fullPath)
    def _getFileNamePrefix(self, fileName):
        ret = re.match('[0-9,a-f]+', fileName);
        return ret.group()
    
    
