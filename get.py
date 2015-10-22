import Tkinter
import tkFileDialog
import tkMessageBox
import os
import os.path
import re
import shutil

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

class MainWidget:
    def __init__(self):
        self._mainFrame = Tkinter.Tk()
        self._subFrame = Tkinter.Frame(self._mainFrame)
        self._createWidgets()

    def _createWidgets(self):
        self._sdCardPathLabel = Tkinter.Label(
            self._subFrame, text="SD card Location: ")
        self._sdCardPathLabel.grid(column=0, row=0)
        self._sdCardPathButton = Tkinter.Button(
                self._subFrame, text="Select",
                command=self._sdCardPathButtonOnClick)
        self._sdCardPathEntry = Tkinter.Entry(self._subFrame)
        self._sdCardPathEntry.grid(column=1, row=0)
        self._sdCardPathButton.grid(column=2, row=0)
        self._destPathLabel = Tkinter.Label(
                self._subFrame, text="Output path: ")
        self._destPathLabel.grid(column=0, row=1)
        self._destPathEntry = Tkinter.Entry(self._subFrame)
        self._destPathEntry.grid(column=1, row=1)
        self._destPathButton = Tkinter.Button(
                self._subFrame, text="Select",
                command=self._destPathButtonOnClick)
        self._destPathButton.grid(column=2, row=1);
        self._startButton = Tkinter.Button(
                self._mainFrame, text="Start",
                command=self._startButtonOnClick)
        self._subFrame.pack(side=Tkinter.TOP)
        self._startButton.pack(side=Tkinter.BOTTOM)
    def show(self):
        self._mainFrame.mainloop()
    def _sdCardPathButtonOnClick(self):
        sdCardPath = tkFileDialog.askdirectory(initialdir='/')
        length = len(self._sdCardPathEntry.get())
        if(length > 0):
            self._sdCardPathEntry.delete(0, length)
        self._sdCardPathEntry.insert(0, sdCardPath)
    def _destPathButtonOnClick(self):
        destPath = tkFileDialog.askdirectory(initialdir='/')
        length = len(self._destPathEntry.get())
        print length
        if(length > 0):
            self._destPathEntry.delete(0, length)
        self._destPathEntry.insert(0, destPath)
    def _startButtonOnClick(self):
        self._startButton
        self._sdCardPath = self._sdCardPathEntry.get()
        self._destPath = self._destPathEntry.get()
        if(os.path.exists(self._sdCardPath) == False):
            tkMessageBox.showerror('error', 'SD card path not exists!')
            return
        if(os.path.exists(self._destPath) == False):
            tkMessageBox.showerror('error', 'Dest path not exists!')
            return
        self._startButton['state'] = Tkinter.DISABLED
        dirFinder = WeChatGifDirFinder(self._sdCardPath)
        dirList = dirFinder.findGifDir()
        gifGetter = GetWeChatGif()
        for adir in dirList:
            dirName = adir.split('/')[-1]
            destDir2 = self._destPath + '/' + dirName
            os.mkdir(destDir2)
            gifGetter.setSourceAndDest(adir + '/emoji', destDir2)
            gifGetter.get()
        self._startButton['state'] = Tkinter.ACTIVE

main = MainWidget()
main.show()
