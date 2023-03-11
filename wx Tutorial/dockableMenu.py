import wx

class MenuFrame(wx.Frame):
    def __init__(self, parent, id, title):
        super().__init__(parent, id, title)
        
        menubar = wx.MenuBar(wx.MB_DOCKABLE)

        file = wx.Menu()
        edit = wx.Menu()
        view = wx.Menu()
        insr = wx.Menu()
        form = wx.Menu()
        tool = wx.Menu() 
        cushelp = wx.Menu()

        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(view, '&View')
        menubar.Append(insr, '&Insert')
        menubar.Append(form, '&Format')
        menubar.Append(tool, '&Tool')
        menubar.Append(cushelp, '&Help')

        self.SetMenuBar(menubar)
        self.Center()
        self.Show()

app = wx.App()
MenuFrame(None, -1, 'Dockable Menubar')
app.MainLoop()



