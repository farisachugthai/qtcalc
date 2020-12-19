#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Signals and slots.

PyQt widgets act as event-catchers. This means that every widget can catch a
specific number of events, like mouse clicks, keypresses, and so on. In
response to these events, widgets always emit a signal, which is a kind of
message that announces a change in its state.

The signal on its own doesn’t perform any action. If you want a signal to
trigger an action, then you need to connect it to a slot. This is the
function or method that will perform an action whenever the connecting signal
is emitted. You can use any Python callable (or callback) as a slot.

If a signal is connected to a slot, then the slot is called whenever the
signal is emitted. If a signal isn’t connected to any slot, then nothing
happens and the signal is ignored. Here are some of the most useful features
of this mechanism:

A signal can be connected to one or many slots.
A signal may also be connected to another signal.
A slot may be connected to one or many signals.
You can use the following syntax to connect a signal to a slot:

    widget.signal.connect(slot_function)

This will connect slot_function to widget.signal. Whenever signal is emitted,
slot_function() will be called.

In line 13, you create greeting(), which you’ll use as a slot. Then in line
26, you connect the button’s clicked signal to greeting(). This way, whenever
the user clicks on the button, greeting() is called and msg will alternate
between the message Hello World! and an empty string:
"""
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def greeting():
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Signals and slots")
layout = QVBoxLayout()

btn = QPushButton("Greet")
btn.clicked.connect(greeting)  # Connect clicked to greeting()


def on_button_clicked():
    """Create an annoying popup."""
    alert = QMessageBox()
    alert.setText("You clicked the button!")
    alert.exec_()


button = QPushButton("Click")
button.clicked.connect(on_button_clicked)

layout.addWidget(btn)
layout.addWidget(button)

msg = QLabel("")
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
