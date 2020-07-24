"""Allow a user to provide a ``ui`` file to initialize.

Generalize the script in `<./python-example/main.py>`_.
"""
import argparse

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def parse_args():
    parser = argparse.ArgumentParser(prog="ui_loader", description=(
        "Load a .ui file created by QtDesigner and run it."
        ))

    parser.add_argument("file", type=argparse.FileType(mode="r"),
            help="The .ui file to load.")

    return parser

def initialize_app(fobj):
    """Initialize the QApplication in a simple manner.

    Handles sys.argv in a more limited manner, *intentionally*, through a minimal
    application of argparse.

    Parameters
    ----------
    fobj : `io.TextIOWrapper`.
        The file to load.

    """
    Form, Window = uic.loadUiType(fobj)
    # where sys.argv is usually handled. pass an empty list instead.
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec_()


if __name__ == '__main__':
    parse = parse_args()
    args = parse.parse_args()
    initialize_app(args.file)
