import wx

ID_QUIT = 1

class SubmenuExample(wx.Frame):
    def __init__(self, parent, id, title):
        super().__init__(parent, id, title, size=(350, 250))

        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(-1, '&New')
        file.Append(-1, '&Open')
        file.Append(-1, '&Save')
        file.AppendSeparator()

        imp = wx.Menu()
        imp.Append(-1, 'Import newsfeed list...')
        imp.Append(-1, 'Import bookmarks...')
        imp.Append(-1, 'Import mail...')

        file.AppendMenu(-1, 'I&mport', imp)

        cusquit = wx.MenuItem(file, ID_QUIT, '&Quit\tCtrl+W')
        cusquit.SetBitmap(wx.Bitmap('icon/exiticon.png'))
        file.Append(cusquit)
        self.Bind(wx.EVT_MENU, self.onQuit, id=ID_QUIT)

        menubar.Append(file, '&File')

        self.SetMenuBar(menubar)

        self.Center()
        self.Show()

    def onQuit(self, e):
        self.Close()

app = wx.App()
SubmenuExample(None, -1, 'Submenu Example')
app.MainLoop()
