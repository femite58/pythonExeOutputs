import wx

class MenuExample(wx.Frame):
    def __init__(self, parent, id, title):
        super().__init__(parent, id, title, size=(250, 150))
        menubar = wx.MenuBar()
        file = wx.Menu()
        cusquit = wx.MenuItem(file, 1, '&Quit\tCtrl+Q')
        cusquit.SetBitmap(wx.Bitmap('icon/exiticon.png'))
        file.Append(cusquit)
        
        self.Bind(wx.EVT_MENU, self.onQuit, id=1)

        menubar.Append(file, '&File')

        self.SetMenuBar(menubar)

        self.Center()
        self.Show(True)

    def onQuit(self, event):
        self.Close()
    
app = wx.App()
MenuExample(None, -1, '')
app.MainLoop()
