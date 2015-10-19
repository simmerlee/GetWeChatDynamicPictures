from WeChatGifDirFinder import*
from GetWeChatGif import*
import os

destDir = 'E:/asdf'

dirFinder = WeChatGifDirFinder('G:/')
dirList = dirFinder.findGifDir()
gifGetter = GetWeChatGif()

adir = dirList[0]
dirName = adir.split('/')[-1]
os.mkdir(destDir + '/' + dirName)
gifGetter.setSourceAndDest(adir + '/emoji', dirName)
gifGetter.get()

