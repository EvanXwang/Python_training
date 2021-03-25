import wx
import wx.xrc
import noname
import wx.richtext
import codecs

class funtion(noname.MyFrame1):

    def newfile( self, event ):
        self.text.Clear()   #清除畫面

    def openfile( self, event ):

        file = wx.FileSelector(     #將檔案路徑存成file
            '請選擇檔案', 
             wildcard='全部|*.*',
             flags=wx.FD_OPEN       
        )
        with open(file, 'rb') as f:  #讀取檔案內容
            content =f.read()       #將內容存成 content
        self.text.SetValue(content)  #將內容存至text
        
        
    def savefile( self, event ):
        content = self.text.GetValue() # 取得text內容
        with open('text.txt', 'w') as f: 
            f.write(content)          # 將內容寫入於text.txt

    
    def closefile( self, event ):
        wx.Exit()                      #關閉視窗

    def coder( self, event ):
        win1.Show()
 

class funtion1(noname.MyDialog1):
    def message( self, event ):
        pass


app = wx.App()  #建立應用
win = funtion(None)  # 主框架檔名.框架名稱
win1 = funtion1(None)
win.Show()   #顯示視窗框
app.MainLoop() #讓視窗持續顯示