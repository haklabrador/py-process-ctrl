#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
import commands

from PyQt4.QtGui import *

# Create an PyQT4 application object.
a = QApplication(sys.argv)

from main_ui import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.runButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self, *args):
        print args
        retcode, output = commands.getstatusoutput('free')
        print (retcode, output)
        self.textEdit.setText(output)

window = MyMainWindow()

# Show window
window.show()

sys.exit(a.exec_())
