#!/usr/bin/env python
import sys

# Step 1: Import different widgets from QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# 2. Create an instance of the QApplication.
# Everything subclasses this, in effect, so we need it first
# as a general rule of thumb.
# .. note:: QApplication is initialized with a list by requirement,
#           so by convention we pass sys.argv
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
hellomsg =  QLabel('<h1>Hello World!</h1>', parent=window)
hellomsg.move(60, 15)

# 4. Show your application's GUI
window.show()
# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())