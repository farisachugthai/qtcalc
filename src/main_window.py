# main_window.py
"""Main Window-Style application.

===================
Part 6: Main Window
===================

You can’t create a main window without first setting a central widget. You
must have a central widget, even if it’s just a placeholder. When this is the
case, you can use a QWidget object as your central widget. You can set the
main window’s central widget with .setCentralWidget(). The main window’s
layout will allow you to have only one central widget, but it can be a single
or a composite widget.


After running
=============
You can see that your Main Window-Style application has the following
components:

    - One main menu called Menu
    - One toolbar with a functional Exit tool button
    - One central widget (a QLabel object)
    - One status bar at the bottom of the window


Applications
============
The most basic class you’ll use when developing PyQt GUI applications is
QApplication. This class is at the core of any PyQt application. It manages
the application’s control flow as well as its main settings. In PyQt, any
instance of QApplication is considered to be an application. Every PyQt GUI
application must have one QApplication object. Some of the application’s
responsibilities include:

    - Handling initialization and finalization
    - Providing the event loop and event handling
    - Handling most of the system-wide and application-wide settings
    - Providing access to global information, such as the application’s directory, screen size, and so on
    - Parsing common command-line arguments
    - Defining the application’s look and feel
    - Providing localization capabilities

These are just some of the core responsibilities of QApplication. As you can
see, this is a fundamental class when it comes to developing PyQt GUI
applications!

One of the most important responsibilities of QApplication is to provide the
event loop and the entire event handling mechanism. Let’s take a closer look
at the event loop now.


Event Loops
===========
GUI applications are event-driven. This means that functions and methods are
executed in response to user actions like clicking on a button, selecting an
item from a combo box, entering or updating the text in a text edit, pressing
a key on the keyboard, and so on. These user actions are generally called
events.

Events are commonly handled by an event loop (also called the main loop). An
event loop is an infinite loop in which all events from the user, the window
system, and any other sources are processed and dispatched. The event loop
waits for an event to occur and then dispatches it to perform some task. The
event loop continues to work until the application is terminated.

Event loops are used by all GUI applications. The event loop is kind of an
infinite loop that waits for the occurrence of events. If an event happens,
then the loop checks if the event is a Terminate event. In that case, the
loop is terminated and the application exits. Otherwise, the event is sent to
the application’s event queue for further processing, and the loop starts
again.

In PyQt, you can run the application’s event loop by calling .exec_() on the
QApplication object.

.. note::

    PyQt was first developed to target Python 2, which already has an
    `exec` keyword. In earlier versions, an underscore was added to the end
    ``.exec_()`` to help avoid name conflicts.

PyQt5 targets Python 3, which doesn’t have an exec keyword. Still, the library provides two methods that start the event loop:

    - ``.exec_()``
    - ``.exec()``

This means that you can remove ``.exec_()`` from your code, and you can
safely use .exec() instead.

For an event to trigger a response action, you need to connect the event with
the action you want to be executed. In PyQt5, you can establish that
connection by using the signals and slots mechanism.
"""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QMainWindow")
        self.setCentralWidget(QLabel("I'm the central widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction("Exit", self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the status bar")
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())