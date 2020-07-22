# Filename: v_layout.py
"""Form layout example.

===============================
Part 5: PyQt QFormLayout schema
===============================

The last layout manager class is QFormLayout, which arranges widgets in a
two-column layout. The first column usually displays messages in labels. The
second column generally contains widgets like QLineEdit, QComboBox, QSpinBox,
and so on. These allow the user to enter or edit data regarding the
information in the first column.

The left column consists of labels, and the right column consists of field
widgets. If you’re dealing with a database application, then this kind of
layout can be an attractive option for increased productivity when you’re
creating your forms.

"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
# Note that this differs from the other 3 by including a lineedit
# instead of the pushbuttons
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QFormLayout')

layout = QFormLayout()

layout.addRow("Name: ", QLineEdit())
layout.addRow("Age: ", QLineEdit())
layout.addRow("Job: ", QLineEdit())
layout.addRow("Hobbies: ", QLineEdit())

window.setLayout(layout)

window.show()
sys.exit(app.exec_())