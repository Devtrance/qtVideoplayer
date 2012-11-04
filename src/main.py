#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PySide.QtGui import QApplication
from videoplayer import VideoPlayer

class Core():
    __version__ = '0.0.1'
    
    def __init__(self):
        app = QApplication(sys.argv)
        app.setApplicationName('OpenDev Player')
        player = VideoPlayer()
        player.show()
        app.exec_()


def main():
    Core()
    
if __name__ == '__main__':
    main()
