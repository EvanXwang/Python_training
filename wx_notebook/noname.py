# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"記事本", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.text = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer3.Add( self.text, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem11 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"建立檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem11 )

		self.m_menuItem12 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"開啟檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem12 )

		self.m_menuItem13 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"儲存檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem13 )

		self.m_menuItem14 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"關閉程式", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem14 )

		self.m_menubar1.Append( self.m_menu1, u"檔案" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem15 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"作者介紹", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem15 )

		self.m_menubar1.Append( self.m_menu2, u"關於" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.newfile, id = self.m_menuItem11.GetId() )
		self.Bind( wx.EVT_MENU, self.openfile, id = self.m_menuItem12.GetId() )
		self.Bind( wx.EVT_MENU, self.savefile, id = self.m_menuItem13.GetId() )
		self.Bind( wx.EVT_MENU, self.closefile, id = self.m_menuItem14.GetId() )
		self.Bind( wx.EVT_MENU, self.coder, id = self.m_menuItem15.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def newfile( self, event ):
		event.Skip()

	def openfile( self, event ):
		event.Skip()

	def savefile( self, event ):
		event.Skip()

	def closefile( self, event ):
		event.Skip()

	def coder( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"關於作者", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"作者:王祥鈞\n信箱:wangxevan@gmail.com\n網站:http://teaching.bo-yuan.net/", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer8.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.message )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def message( self, event ):
		event.Skip()


