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

# In this code, window is an instance of QWidget, which provides all the features you’ll need to create the application’s window (or form). With .setWindowTitle(), you can add a title to your application’s window. In this case, the title to show is PyQt5 App.

# You can use .setGeometry() to define the size of the window and where to
# place it on your screen. The first two parameters are the x and y coordinates
# at which the window will be placed on the screen. The third and fourth
# parameters are the width and height of the window.

# Every functional GUI application needs widgets! Here, you use a QLabel object
# (helloMsg) to show the message Hello World! on your application’s window.
# QLabel objects can accept HTML text, so you can use the HTML element
# '<h1>Hello World!</h1>' to format the text as an h1 header. Finally, you use
# .move() to place helloMsg at the coordinates (60, 15) on your application’s
# window.

# Note: In PyQt5, you can use any widget (a subclass of QWidget) as a top-level window, or even a button or a label. The only condition is that you pass no parent to it. When you use a widget like this, PyQt5 automatically gives it a title bar and turns it into a normal window.

# The parent-child relationship is used for two complementary purposes:

# A widget that doesn’t have a parent is a main window or a top-level window. A
# widget that has a parent (which is always another widget) is contained (or
# shown) within its parent. This relationship also defines ownership, with
# parents owning their children. The PyQt5 ownership model ensures that if you
# delete a parent (for example, a top-level window), then all of its children
# (widgets) are automatically deleted as well.

# To avoid memory leaks, you should always make sure that any QWidget object
# has a parent, with the sole exception of top-level windows

# 4. Show your application's GUI
window.show()

# Here, you call .show() on window. The call to .show() schedules a paint
# event. In other words, it adds a new event to the application’s event queue.
# You cover the event loop in a later section.

# Note: A paint event is a request for painting the widgets that compose a GUI.

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())

# Finally, you start the application’s event loop by calling app.exec_(). The
# call to .exec_() is wrapped in a call to sys.exit(), which allows you to
# cleanly exit Python and release memory resources when the application
# terminates.

def notes():
    """
    Learning the Basics of PyQt.
    ============================
    You’ll need to master the basic concepts of PyQt logic in order to efficiently use the library to develop GUI applications. Some of these concepts include:

    * Widgets
    * Layout managers
    * Dialogs
    * Main windows
    * Applications
    * Event loops
    * Signals and slots

    These elements will be the building blocks of your PyQt GUI applications.
    Most of them are represented as Python classes. PyQt5.QtWidgets is the
    module that provides all these classes. These elements are extremely
    important, so you’ll cover them in the next few sections.

    Widgets
    -------
    QWidget is the base class for all user interface objects, or widgets.
    These are rectangular-shaped graphical components that you can place on
    your application’s windows to build the GUI. Widgets contain a series of
    attributes and methods that allow you to model their appearance and
    behavior. They can also paint a representation of themselves on the
    screen.

    """
    return