# Kinda works. Whole bunch of todos scattered throughout
import sys

# Only exists in PyQt4. Just use a list
# from PyQt5.QtCore import QStringList
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class FileDialogDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        self.btn = QPushButton("Image Previewer")
        self.btn.clicked.connect(self.image_previewer)

        layout.addWidget(self.btn)
        self.label = QLabel("Image preview")

        layout.addWidget(self.label)
        self.btn1 = QPushButton("Preview text files")
        self.btn1.clicked.connect(self.text_previewer)
        layout.addWidget(self.btn1)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("Faris's File Explorer")

    def image_previewer(self):
        """Preview a user provided image."""
        # TODO: hardcoded path
        fname = QFileDialog.getOpenFileName(
            self, "Open file", "c:\\Users\\fac\\Pictures", "Image files (*.jpg *.gif)"
        )
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())

    def text_previewer(self):
        """Preview a text file."""
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        # Rose an TypeError
        dlg.setFilter("Text files (*.txt)")

        if dlg.exec_():
            filenames = dlg.selectedFiles()
        else:
            return
        f = open(filenames[0], "r")

        with f:
            # TODO: if you feed a non text file IE a png the whole program crashes
            data = f.read()
            self.contents.setText(data)


def qt_mainloop(app):
    """Simply put this into it's own function to get a cleaner stack trace."""
    return app.exec_()


def main():
    """Initialize the QApplication and define it a little."""
    app = QApplication(sys.argv)
    app.setOrganizationName("Faris's File Explorer")
    app.setApplicationName("Faris's File Explorer")

    ex = FileDialogDemo()
    ex.show()
    sys.exit(qt_mainloop(app))


if __name__ == "__main__":
    main()
