# /usr/bin/env/python
# -*- coding: utf-8 -*-
"""Simple calculator built using PyQt5.

Notes on QWidget and parent-child relationships
-----------------------------------------------

In PyQt5, you can use any widget (a subclass of QWidget) as a top-level
window, or even a button or a label. The only condition is that you pass no
parent to it. When you use a widget like this, PyQt5 automatically gives it a
title bar and turns it into a normal window.

The parent-child relationship is used for two complementary purposes:

A widget that doesn’t have a parent is a main window or a top-level window. A
widget that has a parent (which is always another widget) is contained (or
shown) within its parent. This relationship also defines ownership, with
parents owning their children. The PyQt5 ownership model ensures that if you
delete a parent (for example, a top-level window), then all of its children
(widgets) are automatically deleted as well.

To avoid memory leaks, you should always make sure that any QWidget object
has a parent, with the sole exception of top-level windows


"""
import sys

from PyQt5.QtCore import QLine, Qt
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class PyCalcUi(QMainWindow):
    """PyCalc's View in the MVC Format."""

    def __init__(self):
        """Initialize the MainWindow subclass and add a widget."""
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(235, 235)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        # Remember after defining widgets we want to define a layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # dict: {button_text: position on the layout}
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "C": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "(": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            ")": (2, 4),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "+": (3, 3),
            "=": (3, 4),
        }

        # Instantiate all the buttons
        # Btw can I compliment the author for intelligently building the
        # a dict of what number it is and where
        # Iterating over the dict and using it's values to define elements in
        # the dict that we bind to the object.
        # Like I was trying to think how I would have written the code
        # for self.buttons
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget((self.buttons[btnText], pos[0], pos[1]))

        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def displayText(self):
        """The getter for the display text.

        This information is going to connect to the equals sign (=)
        and the signal for when the user clicks on it.
        I.E. the return value of this will be the expression to evaluate.
        """

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def clearDisplay(self):
        self.setDisplayText("")


def main():
    """Create the QApplication, an instance of PyCalcUi and run."""
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    sys.exit(pycalc.exec_())


if __name__ == "__main__":
    main()
