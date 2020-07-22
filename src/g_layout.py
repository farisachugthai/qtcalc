# Filename: v_layout.py
"""Grid layout example.

=======================
Part 3: Grid Layout
=======================

The third layout manager class is QGridLayout, which arranges widgets into a
grid of rows and columns. Every widget will have a relative position on the
grid. You can define a widget’s position by passing it a pair of coordinates
in the form of (row, column). These coordinates should be valid int numbers.
They define which cell of the grid you’re going to place the widget on.

"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QGridLayout')
layout = QGridLayout()

# layout.addWidget(QPushButton('Button (0, 0)'), row=0, column=0)
layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())