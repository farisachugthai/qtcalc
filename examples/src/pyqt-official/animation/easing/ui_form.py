# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Thu May  2 16:46:55 2013
#      by: PyQt5 UI code generator snapshot-5.0-e46cc7cf20da
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(545, 471)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.easingCurvePicker = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.easingCurvePicker.sizePolicy().hasHeightForWidth()
        )
        self.easingCurvePicker.setSizePolicy(sizePolicy)
        self.easingCurvePicker.setMaximumSize(QtCore.QSize(16777215, 120))
        self.easingCurvePicker.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.easingCurvePicker.setMovement(QtWidgets.QListView.Static)
        self.easingCurvePicker.setProperty("isWrapping", False)
        self.easingCurvePicker.setViewMode(QtWidgets.QListView.IconMode)
        self.easingCurvePicker.setSelectionRectVisible(False)
        self.easingCurvePicker.setObjectName("easingCurvePicker")
        self.gridLayout.addWidget(self.easingCurvePicker, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.lineRadio.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineRadio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineRadio.setChecked(True)
        self.lineRadio.setObjectName("lineRadio")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.lineRadio)
        self.gridLayout_2.addWidget(self.lineRadio, 0, 0, 1, 1)
        self.circleRadio = QtWidgets.QRadioButton(self.groupBox_2)
        self.circleRadio.setMaximumSize(QtCore.QSize(16777215, 40))
        self.circleRadio.setObjectName("circleRadio")
        self.buttonGroup.addButton(self.circleRadio)
        self.gridLayout_2.addWidget(self.circleRadio, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(
            QtWidgets.QFormLayout.AllNonFixedFieldsGrow
        )
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.periodSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.periodSpinBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.periodSpinBox.sizePolicy().hasHeightForWidth()
        )
        self.periodSpinBox.setSizePolicy(sizePolicy)
        self.periodSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.periodSpinBox.setMinimum(-1.0)
        self.periodSpinBox.setSingleStep(0.1)
        self.periodSpinBox.setProperty("value", -1.0)
        self.periodSpinBox.setObjectName("periodSpinBox")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.periodSpinBox
        )
        self.amplitudeSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.amplitudeSpinBox.setEnabled(False)
        self.amplitudeSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.amplitudeSpinBox.setMinimum(-1.0)
        self.amplitudeSpinBox.setSingleStep(0.1)
        self.amplitudeSpinBox.setProperty("value", -1.0)
        self.amplitudeSpinBox.setObjectName("amplitudeSpinBox")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.amplitudeSpinBox
        )
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.overshootSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.overshootSpinBox.setEnabled(False)
        self.overshootSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.overshootSpinBox.setMinimum(-1.0)
        self.overshootSpinBox.setSingleStep(0.1)
        self.overshootSpinBox.setProperty("value", -1.0)
        self.overshootSpinBox.setObjectName("overshootSpinBox")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.overshootSpinBox
        )
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Easing curves"))
        self.groupBox_2.setTitle(_translate("Form", "Path type"))
        self.lineRadio.setText(_translate("Form", "Line"))
        self.circleRadio.setText(_translate("Form", "Circle"))
        self.groupBox.setTitle(_translate("Form", "Properties"))
        self.label.setText(_translate("Form", "Period"))
        self.label_3.setText(_translate("Form", "Overshoot"))
        self.label_2.setText(_translate("Form", "Amplitude"))
