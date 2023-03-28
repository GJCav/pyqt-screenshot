# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\repos\screenshot\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(451, 281)
        main_window.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(main_window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shotArea = QtWidgets.QWidget(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shotArea.sizePolicy().hasHeightForWidth())
        self.shotArea.setSizePolicy(sizePolicy)
        self.shotArea.setStyleSheet("border: 4px dashed blue;\n"
"background: transparent;")
        self.shotArea.setObjectName("shotArea")
        self.verticalLayout_2.addWidget(self.shotArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeBtn = QtWidgets.QPushButton(main_window)
        self.closeBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\repos\\screenshot\\icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon)
        self.closeBtn.setIconSize(QtCore.QSize(16, 16))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn)
        self.saveBtn = QtWidgets.QPushButton(main_window)
        self.saveBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\repos\\screenshot\\icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn.setIcon(icon1)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout.addWidget(self.saveBtn)
        self.shotBtn = QtWidgets.QPushButton(main_window)
        self.shotBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\repos\\screenshot\\icon/screenshot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shotBtn.setIcon(icon2)
        self.shotBtn.setObjectName("shotBtn")
        self.horizontalLayout.addWidget(self.shotBtn)
        self.moveBtn = QtWidgets.QPushButton(main_window)
        self.moveBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("d:\\repos\\screenshot\\icon/move.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveBtn.setIcon(icon3)
        self.moveBtn.setObjectName("moveBtn")
        self.horizontalLayout.addWidget(self.moveBtn)
        self.resizeBtn = QtWidgets.QPushButton(main_window)
        self.resizeBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("d:\\repos\\screenshot\\icon/resize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resizeBtn.setIcon(icon4)
        self.resizeBtn.setObjectName("resizeBtn")
        self.horizontalLayout.addWidget(self.resizeBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Screenshot"))
