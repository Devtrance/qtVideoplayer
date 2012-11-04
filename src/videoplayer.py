# -*- coding: utf-8 -*-

import platform,  PySide

from PySide import QtUiTools, QtGui, QtCore, phonon

from ui.videoplayer_ui import Ui_MainWindow

class VideoPlayer(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)
        self.setupUi(self)
        
        # Menú para btnAddMedia
        self.addMediaMenu = QtGui.QMenu()
        self.axnAddLocalFile = self.addMediaMenu.addAction('Add local &File')       # Acciones
        self.axnAddURL = self.addMediaMenu.addAction('Add &URL')
        self.btnAddMedia.setMenu(self.addMediaMenu)
    
    # Slots
    @QtCore.Slot()
    def on_axnAddLocalFile_triggered(self):
        print "Add local file"
        
    @QtCore.Slot()
    def on_axnAddURL_triggered(self):
        pass
        
    @QtCore.Slot()
    def on_btnAbout_clicked(self):
        print "About"
        
    @QtCore.Slot()
    def on_btnClearPlayList_clicked(self):
        pass
        
    @QtCore.Slot()

    def on_btnFullscreen_clicked(self):
        pass
        
    @QtCore.Slot()
    def on_btnNext_clicked(self):
        pass
        
    @QtCore.Slot()
    def on_btnPlayPause_clicked(self):
        pass
        
    @QtCore.Slot()
    def on_btnPrevious_clicked(self):
        pass
    
    @QtCore.Slot()
    def on_btnRemoveMedia_clicked(self):
        pass
    
    @QtCore.Slot()
    def on_btnRepeatPlayList_clicked(self):
        pass
    
    @QtCore.Slot()
    def on_btnShufflePlayList_clicked(self):
        pass
    
    @QtCore.Slot(int)
    def on_cbxVideoAspect_currentIndexChanged(self, aspect):
        pass
    
    @QtCore.Slot()          # Parameter: @QtCore.Slot(QtGui.QListWidgetItem)
    def on_lswPlayList_doubleClicked(self, model_index):
        pass
    
