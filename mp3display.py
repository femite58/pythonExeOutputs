import eyed3
import glob
import wx

class Mp3Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.rowObjDict = {}

        self.listCtrl = wx.ListCtrl(
            self, size=(-1, 100), 
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.listCtrl.InsertColumn(0, 'Artist', width=140)
        self.listCtrl.InsertColumn(1, 'Album', width=140)
        self.listCtrl.InsertColumn(2, 'Title', width=200)
        mainSizer.Add(self.listCtrl, 0, wx.ALL | wx.EXPAND, 5)
        editButton = wx.Button(self, label='Edit')
        editButton.Bind(wx.EVT_BUTTON, self.onEdit)
        mainSizer.Add(editButton, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(mainSizer)
    
    def onEdit(self, event):
        print('in onEdit')
        selection = self.listCtrl.GetFocusedItem()
        if selection >= 0:
            mp3 = self.rowObjDict[selection]
            dlg = EditDialog(mp3)
            dlg.ShowModal()
            self.updateMp3Listing(self.currentFolderPath)
            dlg.Destroy()
    
    def updateMp3Listing(self, folderPath):
        print(folderPath)
        self.currentFolderPath = folderPath
        self.listCtrl.ClearAll()
        self.listCtrl.InsertColumn(0, 'Artist', width=140)
        self.listCtrl.InsertColumn(1, 'Album', width=140)
        self.listCtrl.InsertColumn(2, 'Title', width=200)
        self.listCtrl.InsertColumn(3, 'Year', width=200)
        mp3s = glob.glob(folderPath + '/*.mp3')
        mp3Objects = []
        index = 0
        for mp3 in mp3s:
            mp3Object = eyed3.load(mp3)
            try:
                self.listCtrl.InsertItem(index, mp3Object.tag.artist)
            except:
                self.listCtrl.InsertItem(index, '')
            try:
                self.listCtrl.SetItem(index, 1, mp3Object.tag.album)
            except:
                self.listCtrl.SetItem(index, 1, '')
            try:
                self.listCtrl.SetItem(index, 2, mp3Object.tag.title)
            except:
                self.listCtrl.SetItem(index, 2, '')
            mp3Objects.append(mp3Object)
            self.rowObjDict[index] = mp3Object
            index += 1


class EditDialog(wx.Dialog):
    def __init__(self, mp3):
        title = f'Editing "{mp3.tag.title}"'
        super().__init__(parent=None, title=title)
        self.mp3 = mp3
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.artist = wx.TextCtrl(self, value=self.mp3.tag.artist)
        self.addWidgets('Artist', self.artist)
        self.album = wx.TextCtrl(self, value=self.mp3.tag.album)
        self.addWidgets('Album', self.album)
        self.title = wx.TextCtrl(self, value=self.mp3.tag.title)
        self.addWidgets('Title', self.title)
        btnSizer = wx.BoxSizer()
        saveBtn = wx.Button(self, label='Save')
        saveBtn.Bind(wx.EVT_BUTTON, self.onSave)
        btnSizer.Add(saveBtn, 0, wx.ALL, 5)
        btnSizer.Add(wx.Button(self, id=wx.ID_CANCEL), 0, wx.ALL, 5)
        self.mainSizer.Add(btnSizer, 0, wx.CENTER)
        self.SetSizer(self.mainSizer)
    
    def addWidgets(self, labelTxt, textCtrl):
        rowSizer = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, label=labelTxt, size=(50, -1))
        rowSizer.Add(label, 0, wx.ALL, 5)
        rowSizer.Add(textCtrl)
        self.mainSizer.Add(rowSizer, 0, wx.EXPAND)
    
    def onSave(self, event):
        self.mp3.tag.artist = self.artist.GetValue()
        self.mp3.tag.album = self.album.GetValue()
        self.mp3.tag.title = self.title.GetValue()
        self.mp3.tag.save()
        self.Close()


class Mp3Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Mp3 Tag Editor")
        self.panel = Mp3Panel(self)
        self.createMenu()
        self.Show()
    
    def createMenu(self):
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        openFolderMenuItem = fileMenu.Append(wx.ID_ANY, 'Open Folder', 'Open a folder with MP3s')
        menuBar.Append(fileMenu, '&File')
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.onOpenFolder,
            source=openFolderMenuItem
        )
        self.SetMenuBar(menuBar)
    
    def onOpenFolder(self, event):
        title = "Choose a directory:"
        dlg = wx.DirDialog(self, title, style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.panel.updateMp3Listing(dlg.GetPath())
        dlg.Destroy()

if __name__ == '__main__':
    app = wx.App()
    frame = Mp3Frame()
    app.MainLoop()