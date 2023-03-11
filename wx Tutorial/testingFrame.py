import wx
import time

class MyFrame(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, -1, 'Testing Frame', size=(400, 300), style=wx.NO_BORDER | wx.RESIZE_BORDER)
        vbox = wx.BoxSizer(wx.VERTICAL)
        topHbox = wx.FlexGridSizer(1, 4, 0, 0)
        mainSizer = wx.FlexGridSizer(2, 1, 0, 0)
        
        
        self.customHeader = wx.Panel(self, -1, pos=(-10, -10))
        self.customHeader.SetBackgroundColour(wx.Colour(94, 76, 157))
        
        staticText = wx.StaticText(self.customHeader, -1, 'JW Library')
        staticText.SetForegroundColour(wx.Colour(255, 255, 255))
        staticText.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, ''))
        topHbox.Add(staticText, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 10)

        self.miniMizeBtn = self.bitmapSizer('icon/minimizeIcon_white.png')
        self.miniMizeBtn.Bind(wx.EVT_BUTTON, self.onMinimize)
        self.miniMizeBtn.Bind(wx.EVT_ENTER_WINDOW, self.onMinimizeOver)
        self.miniMizeBtn.Bind(wx.EVT_LEAVE_WINDOW, self.onMinimizeOut)
        self.maximizeBtn = self.bitmapSizer('icon/maximizeIcon_white.png')
        self.maximizeBtn.Bind(wx.EVT_BUTTON, self.onMaximize)
        self.maximizeBtn.Bind(wx.EVT_ENTER_WINDOW, self.onMaximizeOver)
        self.maximizeBtn.Bind(wx.EVT_LEAVE_WINDOW, self.onMaximizeOut)
        self.closeBtn = self.bitmapSizer('icon/closeIcon_white.png')
        self.closeBtn.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOver)
        self.closeBtn.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseOut)
        self.closeBtn.Bind(wx.EVT_BUTTON, self.onClick)

        topHbox.Add(self.miniMizeBtn, 0)
        topHbox.Add(self.maximizeBtn, 0)
        topHbox.Add(self.closeBtn, 0)

        topHbox.AddGrowableRow(0)
        topHbox.AddGrowableCol(0)
        
        self.customHeader.SetSizer(topHbox)

        mainSizer.Add(self.customHeader, 1, wx.EXPAND, 0)
        mainSizer.AddGrowableRow(1)
        mainSizer.AddGrowableCol(0)
        # bodyVbox = wx.BoxSizer(wx.VERTICAL)
        self.bodyContainer = wx.Panel(self, -1)
        self.bodyContainer.SetBackgroundColour('#ffffff')
        mainSizer.Add(self.bodyContainer, 1, wx.EXPAND, 0)

        bodySizer = wx.FlexGridSizer(1, 2, 0, 0)
        
        self.toolBox = wx.Panel(self.bodyContainer, -1)
        self.toolBox.SetBackgroundColour('#000000')
        self.mainBody = wx.Panel(self.bodyContainer, -1)
        


        toolVSizer = wx.FlexGridSizer(2, 1, 0, 0)

        image = wx.Bitmap('icon/menuIcon_white.png', wx.BITMAP_TYPE_ANY).ConvertToImage()
        image = image.Scale(20, 15, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(image)
        self.toggleMenu = wx.Button(self.toolBox, -1, size=(50, 40), style=wx.BORDER_NONE | wx.BU_NOTEXT)
        self.toggleMenu.SetBitmap(bitmap)
        self.toggleMenu.SetBackgroundColour('#5e4c9d')
        toolVSizer.Add(self.toggleMenu, 0)
        self.animatingTool = wx.Panel(self.toolBox, -1)
        self.animatingTool.SetBackgroundColour('#3e3f42')
        toolVSizer.Add(self.animatingTool, 1, wx.EXPAND, 0)
        toolVSizer.AddGrowableRow(1)
        toolVSizer.AddGrowableCol(0)
        
        toolVSizer2 = wx.FlexGridSizer(8, 1, 0, 0)
        self.home = self.toolBtn('icon/homeIcon_white.png', 20, 20)
        self.bible = self.toolBtn('icon/bibleIcon_white.png', 25, 15)
        self.publ = self.toolBtn('icon/resizeIcon_white.png', 18, 18)
        self.media = self.toolBtn('icon/mediaIcon_white.png', 23, 18)
        self.meeting = self.toolBtn('icon/meetingIcon_white.png', 23, 20)
        self.treasure = self.toolBtn('icon/treasureIcon_white.png', 20, 20)
        extendedRow = wx.Panel(self.animatingTool, -1, size=(-1, 200))
        # emptyBtn = wx.Button(extendedRow, -1, size=(20, 20), style=wx.BORDER_NONE | wx.BU_NOTEXT)
        self.settings = self.toolBtn('icon/settingsIcon_white.png', 20, 20)
        toolVSizer2.Add(self.home, 0)
        toolVSizer2.Add(self.bible, 0)
        toolVSizer2.Add(self.publ, 0)
        toolVSizer2.Add(self.media, 0)
        toolVSizer2.Add(self.meeting, 0)
        toolVSizer2.Add(self.treasure, 0)
        toolVSizer2.Add(extendedRow, 1, wx.EXPAND, 0)
        toolVSizer2.Add(self.settings, 0)
        toolVSizer2.AddGrowableRow(6)
        toolVSizer2.AddGrowableCol(0)

        
        self.animatingTool.SetSizer(toolVSizer2)

        self.toolBox.SetSizer(toolVSizer)


        
        bodySizer.Add(self.toolBox, 0)
        bodySizer.Add(self.mainBody, 1, wx.EXPAND, 0)
        bodySizer.AddGrowableCol(1)
        bodySizer.AddGrowableRow(0)
        self.bodyContainer.SetSizer(bodySizer)
        
        vbox.Add(mainSizer, 1, wx.EXPAND, 0)
        self.SetSizer(vbox)
        
        self.Layout()
        self.Center()
        self.Show()

    def toolBtn(self, imagePath, w, h):
        image = wx.Bitmap(imagePath, wx.BITMAP_TYPE_ANY).ConvertToImage()
        image = image.Scale(w, h, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(image)
        toolBtn = wx.Button(self.animatingTool, -1, size=(50, 50), style=wx.BORDER_NONE | wx.BU_NOTEXT)
        toolBtn.SetBitmap(bitmap)
        toolBtn.SetBackgroundColour('#4a4a4d')
        return toolBtn



    
    def onMotion(self, e):
        print(e.GetPosition())
        x, y = e.GetPosition()
        sx, sy = self.GetSize()
        if e.Dragging() and (x == (sx - 2) or x == (sx -1) or x == sx):
            self.SetSize(sx+(sx - x), sy)
    
    def onMouseOver(self, e):
        e.GetEventObject().SetBackgroundColour('Red')
        e.Skip()

    def onMouseOut(self, e):
        e.GetEventObject().SetBackgroundColour('#5e4c9d')
        e.Skip()

    def onClick(self, e):
        self.Close()

    def onMinimize(self, e):
        self.Iconize(True)

    def onMinimizeOver(self, e):
        self.miniMizeBtn.SetBitmap(self.getBitmap('icon/minimizeIcon.png'))
        self.miniMizeBtn.SetBackgroundColour('#dfdfdf')
    
    def onMinimizeOut(self, e):
        self.miniMizeBtn.SetBitmap(self.getBitmap('icon/minimizeIcon_white.png'))
        self.miniMizeBtn.SetBackgroundColour('#5e4c9d')

    def onMaximize(self, e):
        self.Maximize(not self.IsMaximized())

    def onMaximizeOver(self, e):
        if not self.IsMaximized():
            self.maximizeBtn.SetBitmap(self.getBitmap('icon/maximizeIcon.png'))
        else:
            self.maximizeBtn.SetBitmap(self.getBitmap('icon/resizeIcon.png'))
        self.maximizeBtn.SetBackgroundColour('#dfdfdf')
        e.Skip()

    def onMaximizeOut(self, e):
        if not self.IsMaximized():
            self.maximizeBtn.SetBitmap(self.getBitmap('icon/maximizeIcon_white.png'))
        else:
            self.maximizeBtn.SetBitmap(self.getBitmap('icon/resizeIcon_white.png'))
        self.maximizeBtn.SetBackgroundColour('#5e4c9d')
        e.Skip()

    def bitmapSizer(self, imgPath):
        image = wx.Bitmap(imgPath, wx.BITMAP_TYPE_ANY).ConvertToImage()
        image = image.Scale(10, 10, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(image)
        iconBtn = wx.Button(self.customHeader, -1, size=(40, 30), style=wx.BORDER_NONE | wx.BU_NOTEXT)
        iconBtn.SetBitmap(bitmap)
        iconBtn.SetBackgroundColour(wx.Colour(94, 76, 157))
        return iconBtn
    
    def getBitmap(self, imgPath):
        image = wx.Bitmap(imgPath, wx.BITMAP_TYPE_ANY).ConvertToImage()
        image = image.Scale(10, 10, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(image)
        return bitmap

app = wx.App()
wx.Log.EnableLogging(False)
frame = MyFrame(None)
app.SetTopWindow(frame)
app.MainLoop()