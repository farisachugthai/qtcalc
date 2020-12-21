# /usr/bin/env/python
# -*- coding: utf-8 -*-
"""Simple calculator built using PyQt5.

more notes here
"""
import sys

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


def main():
    """Create the QApplication, an instance of PyCalcUi and run."""
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()
