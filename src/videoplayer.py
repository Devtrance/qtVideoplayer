# -*- coding: utf-8 -*-

import vlc, user, sys
from PySide import QtGui, QtCore

from ui.videoplayer_ui import Ui_MainWindow


class VideoPlayer(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)
        self.setupUi(self)

        # Menú para btnAddMedia
        self.addMediaMenu = QtGui.QMenu()

        # creating a basic vlc instance
        self.Instance = vlc.Instance()
        # creating an empty vlc media player
        self.MediaPlayer = self.Instance.media_player_new()

        self.axnAddLocalFile = self.addMediaMenu.addAction('Add local &File')
        self.axnAddURL = self.addMediaMenu.addAction('Add &URL')
        self.btnAddMedia.setMenu(self.addMediaMenu)

        # Conexiones para el menu
        self.axnAddLocalFile.triggered.connect(self.on_axnAddLocalFile_triggered)
        self.axnAddURL.triggered.connect(self.on_axnAddURL_triggered)

    # Eventos
    def on_axnAddLocalFile_triggered(self):
        filename = QtGui.QFileDialog.getOpenFileName(self,
                                                     "Open File", user.home)
        if not filename:
            return

         # create the media
        self.Media = self.Instance.media_new(unicode(filename[0]))
        # put the media in the media player
        self.MediaPlayer.set_media(self.Media)

        # parse the metadata of the file
        self.Media.parse()
        # set the title of the track as window title
        self.setWindowTitle(self.Media.get_meta(0))

        if sys.platform == "linux2": # for Linux using the X Server
            self.MediaPlayer.set_xwindow(self.videoDestination.winId())
        elif sys.platform == "win32": # for Windows
            self.MediaPlayer.set_hwnd(self.videoDestination.winId())
        elif sys.platform == "darwin": # for MacOS
            self.MediaPlayer.set_agl(self.videoDestination.windId())

        self.PlayPause()

    def on_axnAddURL_triggered(self):
        print "Add URL"

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

    # Funciones
    def PlayPause(self):
        """Toggle play/pause status
        """
        if self.MediaPlayer.is_playing():
            self.MediaPlayer.pause()
            self.isPaused = True
        else:
            if self.MediaPlayer.play() == -1:
                self.on_axnAddLocalFile_triggered()
                return
            self.MediaPlayer.play()
            self.isPaused = False
