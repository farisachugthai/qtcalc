# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Sun May  5 07:55:08 2013
#      by: PyQt5 UI code generator 5.0-snapshot-74eb89bd4fb2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(378, 385)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.hostName = QtWidgets.QLineEdit(self.groupBox)
        self.hostName.setObjectName("hostName")
        self.gridLayout.addWidget(self.hostName, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setProperty("value", 42)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setProperty("value", 42)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox_2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        self.horizontalSlider.valueChanged["int"].connect(self.spinBox.setValue)
        self.spinBox.valueChanged["int"].connect(self.horizontalSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.groupBox, self.hostName)
        Form.setTabOrder(self.hostName, self.dateTimeEdit)
        Form.setTabOrder(self.dateTimeEdit, self.horizontalSlider)
        Form.setTabOrder(self.horizontalSlider, self.spinBox)
        Form.setTabOrder(self.spinBox, self.groupBox_2)
        Form.setTabOrder(self.groupBox_2, self.treeWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BackSide"))
        self.groupBox.setTitle(_translate("Form", "Settings"))
        self.label.setText(_translate("Form", "Title:"))
        self.hostName.setText(_translate("Form", "Pad Navigator Example"))
        self.label_2.setText(_translate("Form", "Modified:"))
        self.label_3.setText(_translate("Form", "Extent"))
        self.groupBox_2.setTitle(_translate("Form", "Other input"))
        self.treeWidget.headerItem().setText(
            0, _translate("Form", "Widgets On Graphics View")
        )
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(
            0, _translate("Form", "QGraphicsProxyWidget")
        )
        self.treeWidget.topLevelItem(0).child(0).setText(
            0, _translate("Form", "QGraphicsWidget")
        )
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(
            0, _translate("Form", "QObject")
        )
        self.treeWidget.topLevelItem(0).child(0).child(1).setText(
            0, _translate("Form", "QGraphicsItem")
        )
        self.treeWidget.topLevelItem(0).child(0).child(2).setText(
            0, _translate("Form", "QGraphicsLayoutItem")
        )
        self.treeWidget.topLevelItem(1).setText(
            0, _translate("Form", "QGraphicsGridLayout")
        )
        self.treeWidget.topLevelItem(1).child(0).setText(
            0, _translate("Form", "QGraphicsLayout")
        )
        self.treeWidget.topLevelItem(1).child(0).child(0).setText(
            0, _translate("Form", "QGraphicsLayoutItem")
        )
        self.treeWidget.topLevelItem(2).setText(
            0, _translate("Form", "QGraphicsLinearLayout")
        )
        self.treeWidget.topLevelItem(2).child(0).setText(
            0, _translate("Form", "QGraphicsLayout")
        )
        self.treeWidget.topLevelItem(2).child(0).child(0).setText(
            0, _translate("Form", "QGraphicsLayoutItem")
        )
        self.treeWidget.setSortingEnabled(__sortingEnabled)
