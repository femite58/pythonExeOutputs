import wx

class LeftPanel(wx.Panel):
    def __init__(self, parent, id):
        super().__init__(parent, id, style=wx.BORDER_SUNKEN)
        self.text = parent.GetParent().rightPanel.text 

        button1 = wx.Button(self, -1, '+', (10, 10))
        button2 = wx.Button(self, -1, '-', (10, 60))

        self.Bind(wx.EVT_BUTTON, self.onPlus, id=button1.GetId())
        self.Bind(wx.EVT_BUTTON, self.onMinus, id=button2.GetId())

    def onPlus(self, e):
        value = int(self.text.GetLabel())
        value += 1
        self.text.SetLabel(str(value))
    
    def onMinus(self, e):
        value = int(self.text.GetLabel())
        value -= 1
        self.text.SetLabel(str(value))

class RightPanel(wx.Panel):
    def __init__(self, parent, id):
        super().__init__(parent, id, style=wx.BORDER_SUNKEN)
        self.text = wx.StaticText(self, -1, '0', (40, 60))

class Communicate(wx.Frame):
    def __init__(self, parent, id, title):
        super().__init__(parent, id, title, size=(280, 200))
        panel = wx.Panel(self, -1)
        self.rightPanel = RightPanel(panel, -1)

        leftPanel = LeftPanel(panel, -1)

        hbox = wx.BoxSizer()
        hbox.Add(leftPanel, 1, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.rightPanel, 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(hbox)
        self.Center()
        self.Show()

app = wx.App()
Communicate(None, -1, 'Widget Communication')
app.MainLoop()
