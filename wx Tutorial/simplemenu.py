import wx

class SimpleMenu(wx.Frame): 
    def __init__(self, parent, id, title):
        super().__init__(parent, id, title, size=(250, 150))
        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(-1, 'Quit', 'Quit application')
        menubar.Append(file, '&File')
        self.SetMenuBar(menubar)
        self.Center()
        self.Show()

app = wx.App()
SimpleMenu(None, -1, 'Simple Menu')
app.MainLoop()