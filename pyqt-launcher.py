#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *

# Create an PyQT4 application object.
a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()

# Set window size.
w.resize(320, 240)

# Set window title
w.setWindowTitle("Hello World!")



import commands
retcode, output = commands.getstatusoutput('free')
print (retcode, output)


l = QLabel(output, w)
p = l.palette()
p.setColor(l.foregroundRole(), QColor(255,0,0))
p.setColor(l.backgroundRole(), QColor(0,255,0))
l.setPalette(p)

# Show window
w.show()

sys.exit(a.exec_())
