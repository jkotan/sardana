# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'curvesAppearanceChooser.ui'
#
# Created: Fri Apr  9 10:47:57 2010
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_curvesAppearanceChooserDlg(object):
    def setupUi(self, curvesAppearanceChooserDlg):
        curvesAppearanceChooserDlg.setObjectName("curvesAppearanceChooserDlg")
        curvesAppearanceChooserDlg.resize(808, 204)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(curvesAppearanceChooserDlg.sizePolicy().hasHeightForWidth())
        curvesAppearanceChooserDlg.setSizePolicy(sizePolicy)
        curvesAppearanceChooserDlg.setMaximumSize(QtCore.QSize(16777215, 205))
        self.hboxlayout = QtGui.QHBoxLayout(curvesAppearanceChooserDlg)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.curvesLW = QtGui.QListWidget(curvesAppearanceChooserDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curvesLW.sizePolicy().hasHeightForWidth())
        self.curvesLW.setSizePolicy(sizePolicy)
        self.curvesLW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.curvesLW.setObjectName("curvesLW")
        self.vboxlayout.addWidget(self.curvesLW)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.resetBT = QtGui.QPushButton(curvesAppearanceChooserDlg)
        self.resetBT.setObjectName("resetBT")
        self.hboxlayout1.addWidget(self.resetBT)
        self.applyBT = QtGui.QPushButton(curvesAppearanceChooserDlg)
        self.applyBT.setObjectName("applyBT")
        self.hboxlayout1.addWidget(self.applyBT)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout)
        self.lineGB = QtGui.QGroupBox(curvesAppearanceChooserDlg)
        self.lineGB.setObjectName("lineGB")
        self.gridlayout = QtGui.QGridLayout(self.lineGB)
        self.gridlayout.setObjectName("gridlayout")
        self.label_4 = QtGui.QLabel(self.lineGB)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lStyleCB = QtGui.QComboBox(self.lineGB)
        self.lStyleCB.setObjectName("lStyleCB")
        self.gridlayout.addWidget(self.lStyleCB, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.lineGB)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lWidthSB = QtGui.QSpinBox(self.lineGB)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lWidthSB.sizePolicy().hasHeightForWidth())
        self.lWidthSB.setSizePolicy(sizePolicy)
        self.lWidthSB.setMinimum(-1)
        self.lWidthSB.setMaximum(10)
        self.lWidthSB.setProperty("value", QtCore.QVariant(1))
        self.lWidthSB.setObjectName("lWidthSB")
        self.gridlayout.addWidget(self.lWidthSB, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.lineGB)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lColorCB = QtGui.QComboBox(self.lineGB)
        self.lColorCB.setObjectName("lColorCB")
        self.gridlayout.addWidget(self.lColorCB, 2, 1, 1, 1)
        self.labelCurveStyle = QtGui.QLabel(self.lineGB)
        self.labelCurveStyle.setObjectName("labelCurveStyle")
        self.gridlayout.addWidget(self.labelCurveStyle, 3, 0, 1, 1)
        self.cStyleCB = QtGui.QComboBox(self.lineGB)
        self.cStyleCB.setObjectName("cStyleCB")
        self.gridlayout.addWidget(self.cStyleCB, 3, 1, 1, 1)
        self.cFillCB = QtGui.QCheckBox(self.lineGB)
        self.cFillCB.setObjectName("cFillCB")
        self.gridlayout.addWidget(self.cFillCB, 4, 0, 1, 2)
        self.hboxlayout.addWidget(self.lineGB)
        self.symbolGB = QtGui.QGroupBox(curvesAppearanceChooserDlg)
        self.symbolGB.setObjectName("symbolGB")
        self.gridlayout1 = QtGui.QGridLayout(self.symbolGB)
        self.gridlayout1.setObjectName("gridlayout1")
        self.label = QtGui.QLabel(self.symbolGB)
        self.label.setObjectName("label")
        self.gridlayout1.addWidget(self.label, 0, 0, 1, 1)
        self.sStyleCB = QtGui.QComboBox(self.symbolGB)
        self.sStyleCB.setObjectName("sStyleCB")
        self.gridlayout1.addWidget(self.sStyleCB, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.symbolGB)
        self.label_2.setObjectName("label_2")
        self.gridlayout1.addWidget(self.label_2, 1, 0, 1, 1)
        self.sSizeSB = QtGui.QSpinBox(self.symbolGB)
        self.sSizeSB.setMinimum(-1)
        self.sSizeSB.setMaximum(10)
        self.sSizeSB.setSingleStep(1)
        self.sSizeSB.setProperty("value", QtCore.QVariant(3))
        self.sSizeSB.setObjectName("sSizeSB")
        self.gridlayout1.addWidget(self.sSizeSB, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.symbolGB)
        self.label_3.setObjectName("label_3")
        self.gridlayout1.addWidget(self.label_3, 2, 0, 1, 1)
        self.sColorCB = QtGui.QComboBox(self.symbolGB)
        self.sColorCB.setObjectName("sColorCB")
        self.gridlayout1.addWidget(self.sColorCB, 2, 1, 1, 1)
        self.sFillCB = QtGui.QCheckBox(self.symbolGB)
        self.sFillCB.setTristate(False)
        self.sFillCB.setObjectName("sFillCB")
        self.gridlayout1.addWidget(self.sFillCB, 3, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(111, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem, 4, 0, 1, 2)
        self.hboxlayout.addWidget(self.symbolGB)
        self.otherGB = QtGui.QGroupBox(curvesAppearanceChooserDlg)
        self.otherGB.setObjectName("otherGB")
        self.gridlayout2 = QtGui.QGridLayout(self.otherGB)
        self.gridlayout2.setObjectName("gridlayout2")
        self.groupBox = QtGui.QGroupBox(self.otherGB)
        self.groupBox.setObjectName("groupBox")
        self.hboxlayout2 = QtGui.QHBoxLayout(self.groupBox)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.assignToY1BT = QtGui.QToolButton(self.groupBox)
        self.assignToY1BT.setObjectName("assignToY1BT")
        self.hboxlayout2.addWidget(self.assignToY1BT)
        self.assignToY2BT = QtGui.QToolButton(self.groupBox)
        self.assignToY2BT.setObjectName("assignToY2BT")
        self.hboxlayout2.addWidget(self.assignToY2BT)
        self.gridlayout2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.changeTitlesBT = QtGui.QPushButton(self.otherGB)
        self.changeTitlesBT.setObjectName("changeTitlesBT")
        self.gridlayout2.addWidget(self.changeTitlesBT, 1, 0, 1, 1)
        self.bckgndBT = QtGui.QPushButton(self.otherGB)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bckgndBT.sizePolicy().hasHeightForWidth())
        self.bckgndBT.setSizePolicy(sizePolicy)
        self.bckgndBT.setObjectName("bckgndBT")
        self.gridlayout2.addWidget(self.bckgndBT, 2, 0, 1, 1)
        self.hboxlayout.addWidget(self.otherGB)
        self.label_4.setBuddy(self.lStyleCB)
        self.label_5.setBuddy(self.lWidthSB)
        self.label_6.setBuddy(self.lColorCB)
        self.label.setBuddy(self.sStyleCB)
        self.label_2.setBuddy(self.sSizeSB)
        self.label_3.setBuddy(self.sColorCB)

        self.retranslateUi(curvesAppearanceChooserDlg)
        QtCore.QMetaObject.connectSlotsByName(curvesAppearanceChooserDlg)

    def retranslateUi(self, curvesAppearanceChooserDlg):
        curvesAppearanceChooserDlg.setWindowTitle(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.curvesLW.setSortingEnabled(True)
        self.resetBT.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "&Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.applyBT.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "&Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.lineGB.setTitle(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "S&tyle", None, QtGui.QApplication.UnicodeUTF8))
        self.lStyleCB.setToolTip(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Style of the pen used to connect the points.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "&Width", None, QtGui.QApplication.UnicodeUTF8))
        self.lWidthSB.setSpecialValueText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "--", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "C&olor", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCurveStyle.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.cStyleCB.setToolTip(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Connector mode: how the data points are connected (steps, straight lines,...)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.cFillCB.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "&Area Fill", None, QtGui.QApplication.UnicodeUTF8))
        self.symbolGB.setTitle(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Symbols", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "&Style", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Si&ze", None, QtGui.QApplication.UnicodeUTF8))
        self.sSizeSB.setSpecialValueText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "--", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "&Color", None, QtGui.QApplication.UnicodeUTF8))
        self.sFillCB.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "&Fill", None, QtGui.QApplication.UnicodeUTF8))
        self.otherGB.setTitle(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Assign to axis", None, QtGui.QApplication.UnicodeUTF8))
        self.assignToY1BT.setToolTip(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Assign selected curves to Y1 (left axis)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.assignToY1BT.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Y1", None, QtGui.QApplication.UnicodeUTF8))
        self.assignToY2BT.setToolTip(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Assign selected curves to Y2 (right axis)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.assignToY2BT.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Y2", None, QtGui.QApplication.UnicodeUTF8))
        self.changeTitlesBT.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Curve Title(s)...", None, QtGui.QApplication.UnicodeUTF8))
        self.bckgndBT.setText(QtGui.QApplication.translate("curvesAppearanceChooserDlg", "Background fill...", None, QtGui.QApplication.UnicodeUTF8))
