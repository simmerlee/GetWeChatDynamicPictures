import Tkinter
import tkFileDialog
import tkMessageBox
import os.path

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
            self._sdCardPathEntry.delete(0, length - 1)
        self._sdCardPathEntry.insert(0, sdCardPath)
    def _destPathButtonOnClick(self):
        destPath = tkFileDialog.askdirectory(initialdir='/')
        length = len(self._destPathEntry.get())
        if(length > 0):
            self._destPath.delete(0, length - 1)
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
        

main = MainWidget()
main.show()
