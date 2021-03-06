# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dialog_qt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(396, 156)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setOpenExternalLinks(False)
        self.title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.emailLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.gridLayout.addWidget(self.emailLabel, 2, 0, 1, 1)
        self.emailValue = QtWidgets.QLabel(Dialog)
        self.emailValue.setOpenExternalLinks(True)
        self.emailValue.setObjectName("emailValue")
        self.gridLayout.addWidget(self.emailValue, 2, 1, 1, 1)
        self.versionValue = QtWidgets.QLabel(Dialog)
        self.versionValue.setText("")
        self.versionValue.setObjectName("versionValue")
        self.gridLayout.addWidget(self.versionValue, 0, 1, 1, 1)
        self.websiteValue = QtWidgets.QLabel(Dialog)
        self.websiteValue.setOpenExternalLinks(True)
        self.websiteValue.setObjectName("websiteValue")
        self.gridLayout.addWidget(self.websiteValue, 3, 1, 1, 1)
        self.authorValue = QtWidgets.QLabel(Dialog)
        self.authorValue.setObjectName("authorValue")
        self.gridLayout.addWidget(self.authorValue, 1, 1, 1, 1)
        self.websiteLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.websiteLabel.setFont(font)
        self.websiteLabel.setObjectName("websiteLabel")
        self.gridLayout.addWidget(self.websiteLabel, 3, 0, 1, 1)
        self.versionLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.versionLabel.setFont(font)
        self.versionLabel.setObjectName("versionLabel")
        self.gridLayout.addWidget(self.versionLabel, 0, 0, 1, 1)
        self.authorLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.authorLabel.setFont(font)
        self.authorLabel.setObjectName("authorLabel")
        self.gridLayout.addWidget(self.authorLabel, 1, 0, 1, 1)
        self.mainLayout.addLayout(self.gridLayout)
        self.icon = QtWidgets.QLabel(Dialog)
        self.icon.setText("")
        self.icon.setScaledContents(False)
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.icon.setObjectName("icon")
        self.mainLayout.addWidget(self.icon)
        self.verticalLayout.addLayout(self.mainLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.title.setText(_translate("Dialog", "Cognitive Battery"))
        self.emailLabel.setText(_translate("Dialog", "Email:"))
        self.emailValue.setText(_translate("Dialog", "<a href=\"mailto:simonho213@gmail.com?Subject=Cognitive%20Battery\">simonho213@gmail.com</a>"))
        self.websiteValue.setText(_translate("Dialog", "<a href=\"http://www.simonho.ca\">www.simonho.ca</a>"))
        self.authorValue.setText(_translate("Dialog", "Simon Ho"))
        self.websiteLabel.setText(_translate("Dialog", "Website:"))
        self.versionLabel.setText(_translate("Dialog", "Version:"))
        self.authorLabel.setText(_translate("Dialog", "Author:"))

