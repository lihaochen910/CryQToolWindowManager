from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from QToolWindowManager import *

import sys
app = QApplication ( sys.argv )
app.setStyleSheet (
	open ( './QToolWindowManager/resources/CryEngineVStyleSheet.qss' ).read ()
)

class Test ( QMainWindow ):
	def __init__ ( self, *args ):
		super ( Test, self ).__init__ ( *args )

		self.setWindowTitle ( "Test Window" )
		self.setWindowIcon ( QIcon ( "./QToolWindowManager/resources/base_window.png" ) )
		self.setMinimumSize ( 640, 480 )

		toolConfig = {}
		toolConfig[ QTWM_AREA_DOCUMENT_MODE ] = False
		toolConfig[ QTWM_AREA_IMAGE_HANDLE ] = False
		toolConfig[ QTWM_AREA_SHOW_DRAG_HANDLE ] = False
		toolConfig[ QTWM_AREA_TABS_CLOSABLE ] = False
		toolConfig[ QTWM_AREA_EMPTY_SPACE_DRAG ] = False
		toolConfig[ QTWM_THUMBNAIL_TIMER_INTERVAL ] = 1000
		toolConfig[ QTWM_TOOLTIP_OFFSET ] = QPoint ( 1, 20 )
		toolConfig[ QTWM_AREA_TAB_ICONS ] = True
		toolConfig[ QTWM_RELEASE_POLICY ] = QTWMReleaseCachingPolicy.rcpWidget
		toolConfig[ QTWM_WRAPPERS_ARE_CHILDREN ] = False
		toolConfig[ QTWM_RAISE_DELAY ] = 750
		toolConfig[ QTWM_RETITLE_WRAPPER ] = True
		toolConfig[ QTWM_SINGLE_TAB_FRAME ] = True
		toolConfig[ QTWM_BRING_ALL_TO_FRONT ] = True
		toolConfig[ QTWM_DROPTARGET_COMBINE ] = "./QToolWindowManager/resources/base_window.png"
		toolConfig[ QTWM_DROPTARGET_TOP ] = "./QToolWindowManager/resources/dock_top.png"
		toolConfig[ QTWM_DROPTARGET_BOTTOM ] = "./QToolWindowManager/resources/dock_bottom.png"
		toolConfig[ QTWM_DROPTARGET_LEFT ] = "./QToolWindowManager/resources/dock_left.png"
		toolConfig[ QTWM_DROPTARGET_RIGHT ] = "./QToolWindowManager/resources/dock_right.png"
		toolConfig[ QTWM_DROPTARGET_SPLIT_LEFT ] = "./QToolWindowManager/resources/vsplit_left.png"
		toolConfig[ QTWM_DROPTARGET_SPLIT_RIGHT ] = "./QToolWindowManager/resources/vsplit_right.png"
		toolConfig[ QTWM_DROPTARGET_SPLIT_TOP ] = "./QToolWindowManager/resources/hsplit_top.png"
		toolConfig[ QTWM_DROPTARGET_SPLIT_BOTTOM ] = "./QToolWindowManager/resources/hsplit_bottom.png"
		toolConfig[ "sandboxMinimizeIcon" ] = QIcon ( "./QToolWindowManager/resources/window_minimize.ico" )
		toolConfig[ "sandboxMaximizeIcon" ] = QIcon ( "./QToolWindowManager/resources/window_maximize.ico" )
		toolConfig[ "sandboxRestoreIcon" ] = QIcon ( "./QToolWindowManager/resources/window_restore.ico" )
		toolConfig[ "sandboxWindowCloseIcon" ] = QIcon ( "./QToolWindowManager/resources/window_close.ico" )
		toolConfig[ QTWM_TAB_CLOSE_ICON ] = QIcon ( "./QToolWindowManager/resources/window_close.ico" )
		toolConfig[ QTWM_SINGLE_TAB_FRAME_CLOSE_ICON ] = QIcon ( "./QToolWindowManager/resources/window_close.ico" )

		from QToolWindowManager.QMainFrame import CToolWindowManagerClassFactory
		mgr = QToolWindowManager ( self, toolConfig, CToolWindowManagerClassFactory () )
		self.setCentralWidget ( mgr )

		widget = QPushButton ( 'hello' )
		widget.setWindowTitle ( 'hello' )
		widget.setObjectName ( 'hello' )
		mgr.addToolWindow ( widget, None, QToolWindowAreaReference.Combine )

		widget = QPushButton ( 'world' )
		widget.setWindowTitle ( 'world' )
		widget.setObjectName ( 'world' )
		mgr.addToolWindow ( widget, None, QToolWindowAreaReference.Top )

		widget = QPushButton ( 'happy' )
		widget.setWindowTitle ( 'happy' )
		widget.setObjectName ( 'happy' )
		mgr.addToolWindow ( widget, None, QToolWindowAreaReference.Bottom )

		widget = QPushButton ( 'christmas' )
		widget.setWindowTitle ( 'christmas' )
		widget.setObjectName ( 'christmas' )
		mgr.addToolWindow ( widget, None, QToolWindowAreaReference.Floating )

		# result = mgr.saveState ()
		# for w in mgr.toolWindows:
		# 	mgr.moveToolWindow ( w, None, QToolWindowAreaReference.Combine )
		# mgr.restoreState ( result )
		# area = mgr.areaOf ( widget )
		# mgr.hideToolWindow ( widget )
		# area.addToolWindow ( widget )

window = Test ()
window.show ()
window.raise_ ()
app.exec_ ()