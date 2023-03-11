import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Hello World")
        # self.Show()
        panel = wx.Panel(self)
        mySizer = wx.BoxSizer(wx.VERTICAL)
        # absolute positioning of text_ctrl
        # self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        self.text_ctrl = wx.TextCtrl(panel)
        mySizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label="Press Me")
        my_btn.Bind(wx.EVT_BUTTON, self.onPress)
        mySizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(mySizer)
        self.Show()

    def onPress(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
            return
        print(f'You typed: "{value}"')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()