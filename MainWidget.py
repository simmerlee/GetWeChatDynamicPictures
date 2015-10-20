import Tkinter

class MainWidget:
    def __init__(self):
        self._mainFrame = Tkinter.Tk()
        self._subFrame = Tkinter.Frame(self._mainFrame)
        self._createWidgets()
        print 'fuck'

    def _createWidgets(self):
        self._sdCardPathLabel = Tkinter.Label(
            self._subFrame, text="Please select SD card Location ")
        self._sdCardPathLabel.grid(column=0, row=0)
        self._sdCardPathButton = Tkinter.Button(
                self._subFrame, text="Select")
        self._sdCardPathButton.grid(column=1, row=0)
        self._destPathLabel = Tkinter.Label(
                self._subFrame, text="Please select output path ")
        self._destPathLabel.grid(column=0, row=1);
        self._destPathButton = Tkinter.Button(
                self._subFrame, text="Select")
        self._destPathButton.grid(column=1, row=1);
        self._startButton = Tkinter.Button(
                self._mainFrame, text="Start")
        self._subFrame.pack(side=Tkinter.TOP)
        self._startButton.pack(side=Tkinter.BOTTOM)

    def show(self):
        self._mainFrame.mainloop()

main = MainWidget()
main.show()
