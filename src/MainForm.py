# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Make Video Segments", pos = wx.DefaultPosition, size = wx.Size( 522,422 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Input File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.InputFilePath = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( -1,-1 ), wx.FLP_DEFAULT_STYLE )
		gSizer1.Add( self.InputFilePath, 0, wx.ALL|wx.EXPAND, 10 )


		bSizer.Add( gSizer1, 0, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )


		bSizer2.Add( ( 0, 15), 1, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 1, 2, 0, 0 )

		gSizer5 = wx.GridSizer( 3, 1, 0, 0 )

		self.SegmentLengthLabel = wx.StaticText( self, wx.ID_ANY, u"Segment Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SegmentLengthLabel.Wrap( -1 )

		gSizer5.Add( self.SegmentLengthLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.FadeInCheck = wx.CheckBox( self, wx.ID_ANY, u"Fade In", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		gSizer5.Add( self.FadeInCheck, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.FadeOutCheck = wx.CheckBox( self, wx.ID_ANY, u"Fade Out", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		gSizer5.Add( self.FadeOutCheck, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer4.Add( gSizer5, 1, wx.EXPAND, 5 )

		fgSizer = wx.FlexGridSizer( 3, 3, 0, 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.SegmentLengthSlider = wx.Slider( self, wx.ID_ANY, 20, 1, 100, wx.DefaultPosition, wx.Size( 130,-1 ), wx.SL_HORIZONTAL )
		fgSizer.Add( self.SegmentLengthSlider, 0, wx.ALL, 5 )

		self.SegmentLength = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 9000, 20 )
		fgSizer.Add( self.SegmentLength, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.FadeInSlider = wx.Slider( self, wx.ID_ANY, 1, 1, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		self.FadeInSlider.Enable( False )

		fgSizer.Add( self.FadeInSlider, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )

		self.FadeInDuration = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 1 )
		self.FadeInDuration.Enable( False )

		fgSizer.Add( self.FadeInDuration, 0, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		self.m_staticText41.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer.Add( self.m_staticText41, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

		self.FadeOutSlider = wx.Slider( self, wx.ID_ANY, 1, 1, 10, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		self.FadeOutSlider.Enable( False )

		fgSizer.Add( self.FadeOutSlider, 0, wx.ALL|wx.EXPAND, 5 )

		self.FadeOutDuration = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 1 )
		self.FadeOutDuration.Enable( False )

		fgSizer.Add( self.FadeOutDuration, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer.Add( self.m_staticText42, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )


		gSizer4.Add( fgSizer, 0, wx.EXPAND, 5 )


		bSizer2.Add( gSizer4, 0, 0, 5 )


		bSizer.Add( bSizer2, 0, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Output Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.OutputDir = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.DIRP_DEFAULT_STYLE )
		gSizer2.Add( self.OutputDir, 0, wx.EXPAND|wx.ALL, 10 )


		bSizer.Add( gSizer2, 0, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"START", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.m_button1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		gSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.ProgressBar = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.ProgressBar.SetValue( 0 )
		gSizer3.Add( self.ProgressBar, 0, wx.ALL|wx.EXPAND, 10 )


		bSizer.Add( gSizer3, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer )
		self.Layout()
		self.OutputText = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.InputFilePath.Bind( wx.EVT_FILEPICKER_CHANGED, self.set_input_file )
		self.FadeInCheck.Bind( wx.EVT_CHECKBOX, self.fade_in_checked )
		self.FadeOutCheck.Bind( wx.EVT_CHECKBOX, self.fade_out_checked )
		self.SegmentLengthSlider.Bind( wx.EVT_SCROLL, self.on_segment_length_slider )
		self.SegmentLength.Bind( wx.EVT_SPINCTRL, self.on_segment_length )
		self.FadeInSlider.Bind( wx.EVT_SCROLL_CHANGED, self.on_fade_in_slider )
		self.FadeInDuration.Bind( wx.EVT_SPINCTRL, self.on_fade_in_duration )
		self.FadeOutSlider.Bind( wx.EVT_SCROLL_CHANGED, self.on_fade_out_slider )
		self.FadeOutDuration.Bind( wx.EVT_SPINCTRL, self.on_fade_out_duration )
		self.OutputDir.Bind( wx.EVT_DIRPICKER_CHANGED, self.set_output_dir )
		self.m_button1.Bind( wx.EVT_BUTTON, self.on_submit_click )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def set_input_file( self, event ):
		event.Skip()

	def fade_in_checked( self, event ):
		event.Skip()

	def fade_out_checked( self, event ):
		event.Skip()

	def on_segment_length_slider( self, event ):
		event.Skip()

	def on_segment_length( self, event ):
		event.Skip()

	def on_fade_in_slider( self, event ):
		event.Skip()

	def on_fade_in_duration( self, event ):
		event.Skip()

	def on_fade_out_slider( self, event ):
		event.Skip()

	def on_fade_out_duration( self, event ):
		event.Skip()

	def set_output_dir( self, event ):
		event.Skip()

	def on_submit_click( self, event ):
		event.Skip()


