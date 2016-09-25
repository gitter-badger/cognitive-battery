# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CognitiveBattery(object):
    def setupUi(self, CognitiveBattery):
        CognitiveBattery.setObjectName(_fromUtf8("CognitiveBattery"))
        CognitiveBattery.resize(554, 621)
        self.centralwidget = QtGui.QWidget(CognitiveBattery)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.sessionInfoLayout = QtGui.QVBoxLayout()
        self.sessionInfoLayout.setObjectName(_fromUtf8("sessionInfoLayout"))
        self.sessionInfoText = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sessionInfoText.sizePolicy().hasHeightForWidth())
        self.sessionInfoText.setSizePolicy(sizePolicy)
        self.sessionInfoText.setTextFormat(QtCore.Qt.AutoText)
        self.sessionInfoText.setObjectName(_fromUtf8("sessionInfoText"))
        self.sessionInfoLayout.addWidget(self.sessionInfoText)
        self.sessionInfoColumnLayout = QtGui.QHBoxLayout()
        self.sessionInfoColumnLayout.setObjectName(_fromUtf8("sessionInfoColumnLayout"))
        self.sessionInfoLabelLayout = QtGui.QVBoxLayout()
        self.sessionInfoLabelLayout.setObjectName(_fromUtf8("sessionInfoLabelLayout"))
        self.raText = QtGui.QLabel(self.centralwidget)
        self.raText.setObjectName(_fromUtf8("raText"))
        self.sessionInfoLabelLayout.addWidget(self.raText)
        self.subNumText = QtGui.QLabel(self.centralwidget)
        self.subNumText.setObjectName(_fromUtf8("subNumText"))
        self.sessionInfoLabelLayout.addWidget(self.subNumText)
        self.experimentIDText = QtGui.QLabel(self.centralwidget)
        self.experimentIDText.setObjectName(_fromUtf8("experimentIDText"))
        self.sessionInfoLabelLayout.addWidget(self.experimentIDText)
        self.conditionText = QtGui.QLabel(self.centralwidget)
        self.conditionText.setObjectName(_fromUtf8("conditionText"))
        self.sessionInfoLabelLayout.addWidget(self.conditionText)
        self.ageText = QtGui.QLabel(self.centralwidget)
        self.ageText.setObjectName(_fromUtf8("ageText"))
        self.sessionInfoLabelLayout.addWidget(self.ageText)
        self.sexText = QtGui.QLabel(self.centralwidget)
        self.sexText.setObjectName(_fromUtf8("sexText"))
        self.sessionInfoLabelLayout.addWidget(self.sexText)
        self.sessionInfoColumnLayout.addLayout(self.sessionInfoLabelLayout)
        self.sessionInfoInputLayout = QtGui.QVBoxLayout()
        self.sessionInfoInputLayout.setObjectName(_fromUtf8("sessionInfoInputLayout"))
        self.raBox = QtGui.QLineEdit(self.centralwidget)
        self.raBox.setObjectName(_fromUtf8("raBox"))
        self.sessionInfoInputLayout.addWidget(self.raBox)
        self.subNumBox = QtGui.QLineEdit(self.centralwidget)
        self.subNumBox.setObjectName(_fromUtf8("subNumBox"))
        self.sessionInfoInputLayout.addWidget(self.subNumBox)
        self.experimentIDBox = QtGui.QLineEdit(self.centralwidget)
        self.experimentIDBox.setObjectName(_fromUtf8("experimentIDBox"))
        self.sessionInfoInputLayout.addWidget(self.experimentIDBox)
        self.conditionBox = QtGui.QLineEdit(self.centralwidget)
        self.conditionBox.setObjectName(_fromUtf8("conditionBox"))
        self.sessionInfoInputLayout.addWidget(self.conditionBox)
        self.ageBox = QtGui.QLineEdit(self.centralwidget)
        self.ageBox.setObjectName(_fromUtf8("ageBox"))
        self.sessionInfoInputLayout.addWidget(self.ageBox)
        self.sexLayout = QtGui.QHBoxLayout()
        self.sexLayout.setContentsMargins(-1, -1, -1, 0)
        self.sexLayout.setObjectName(_fromUtf8("sexLayout"))
        self.maleRadio = QtGui.QRadioButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maleRadio.sizePolicy().hasHeightForWidth())
        self.maleRadio.setSizePolicy(sizePolicy)
        self.maleRadio.setObjectName(_fromUtf8("maleRadio"))
        self.sexLayout.addWidget(self.maleRadio)
        self.femaleRadio = QtGui.QRadioButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.femaleRadio.sizePolicy().hasHeightForWidth())
        self.femaleRadio.setSizePolicy(sizePolicy)
        self.femaleRadio.setObjectName(_fromUtf8("femaleRadio"))
        self.sexLayout.addWidget(self.femaleRadio)
        self.sessionInfoInputLayout.addLayout(self.sexLayout)
        self.sessionInfoColumnLayout.addLayout(self.sessionInfoInputLayout)
        self.sessionInfoLayout.addLayout(self.sessionInfoColumnLayout)
        self.mainLayout.addLayout(self.sessionInfoLayout)
        self.sessionLine = QtGui.QFrame(self.centralwidget)
        self.sessionLine.setLineWidth(1)
        self.sessionLine.setFrameShape(QtGui.QFrame.HLine)
        self.sessionLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.sessionLine.setObjectName(_fromUtf8("sessionLine"))
        self.mainLayout.addWidget(self.sessionLine)
        self.batteryLayout = QtGui.QVBoxLayout()
        self.batteryLayout.setObjectName(_fromUtf8("batteryLayout"))
        self.batterySelectText = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batterySelectText.sizePolicy().hasHeightForWidth())
        self.batterySelectText.setSizePolicy(sizePolicy)
        self.batterySelectText.setScaledContents(True)
        self.batterySelectText.setObjectName(_fromUtf8("batterySelectText"))
        self.batteryLayout.addWidget(self.batterySelectText)
        self.taskOrderLayout = QtGui.QHBoxLayout()
        self.taskOrderLayout.setContentsMargins(-1, -1, -1, 10)
        self.taskOrderLayout.setObjectName(_fromUtf8("taskOrderLayout"))
        self.reorderText = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.reorderText.setFont(font)
        self.reorderText.setObjectName(_fromUtf8("reorderText"))
        self.taskOrderLayout.addWidget(self.reorderText)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.taskOrderLayout.addItem(spacerItem)
        self.randomOrderCheck = QtGui.QCheckBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.randomOrderCheck.sizePolicy().hasHeightForWidth())
        self.randomOrderCheck.setSizePolicy(sizePolicy)
        self.randomOrderCheck.setChecked(False)
        self.randomOrderCheck.setObjectName(_fromUtf8("randomOrderCheck"))
        self.taskOrderLayout.addWidget(self.randomOrderCheck)
        self.batteryLayout.addLayout(self.taskOrderLayout)
        self.selectionLayout = QtGui.QHBoxLayout()
        self.selectionLayout.setContentsMargins(-1, -1, -1, 10)
        self.selectionLayout.setObjectName(_fromUtf8("selectionLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.selectionLayout.addItem(spacerItem1)
        self.selectAllButton = QtGui.QPushButton(self.centralwidget)
        self.selectAllButton.setObjectName(_fromUtf8("selectAllButton"))
        self.selectionLayout.addWidget(self.selectAllButton)
        self.deselectAllButton = QtGui.QPushButton(self.centralwidget)
        self.deselectAllButton.setObjectName(_fromUtf8("deselectAllButton"))
        self.selectionLayout.addWidget(self.deselectAllButton)
        self.batteryLayout.addLayout(self.selectionLayout)
        self.taskListLayout = QtGui.QHBoxLayout()
        self.taskListLayout.setContentsMargins(-1, -1, -1, 0)
        self.taskListLayout.setObjectName(_fromUtf8("taskListLayout"))
        self.taskList = QtGui.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.taskList.setFont(font)
        self.taskList.setProperty("showDropIndicator", False)
        self.taskList.setDragEnabled(True)
        self.taskList.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.taskList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.taskList.setAlternatingRowColors(True)
        self.taskList.setMovement(QtGui.QListView.Snap)
        self.taskList.setObjectName(_fromUtf8("taskList"))
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.taskList.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.taskList.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.taskList.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.taskList.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.taskList.addItem(item)
        self.taskListLayout.addWidget(self.taskList)
        self.reorderButtonLayout = QtGui.QVBoxLayout()
        self.reorderButtonLayout.setContentsMargins(0, -1, -1, -1)
        self.reorderButtonLayout.setSpacing(6)
        self.reorderButtonLayout.setObjectName(_fromUtf8("reorderButtonLayout"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.reorderButtonLayout.addItem(spacerItem2)
        self.upButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        self.upButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.reorderButtonLayout.addWidget(self.upButton)
        self.downButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy)
        self.downButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.reorderButtonLayout.addWidget(self.downButton)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.reorderButtonLayout.addItem(spacerItem3)
        self.taskListLayout.addLayout(self.reorderButtonLayout)
        self.batteryLayout.addLayout(self.taskListLayout)
        self.mainLayout.addLayout(self.batteryLayout)
        self.saveLoadLayout = QtGui.QHBoxLayout()
        self.saveLoadLayout.setObjectName(_fromUtf8("saveLoadLayout"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.saveLoadLayout.addWidget(self.startButton)
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.saveLoadLayout.addWidget(self.cancelButton)
        self.mainLayout.addLayout(self.saveLoadLayout)
        self.verticalLayout.addLayout(self.mainLayout)
        CognitiveBattery.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CognitiveBattery)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        CognitiveBattery.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CognitiveBattery)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CognitiveBattery.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(CognitiveBattery)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionExit = QtGui.QAction(CognitiveBattery)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionDocumentation = QtGui.QAction(CognitiveBattery)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionView_License = QtGui.QAction(CognitiveBattery)
        self.actionView_License.setObjectName(_fromUtf8("actionView_License"))
        self.actionContribute = QtGui.QAction(CognitiveBattery)
        self.actionContribute.setObjectName(_fromUtf8("actionContribute"))
        self.actionBrowse_Issues = QtGui.QAction(CognitiveBattery)
        self.actionBrowse_Issues.setObjectName(_fromUtf8("actionBrowse_Issues"))
        self.actionReport_Bug = QtGui.QAction(CognitiveBattery)
        self.actionReport_Bug.setObjectName(_fromUtf8("actionReport_Bug"))
        self.actionRequest_Feature = QtGui.QAction(CognitiveBattery)
        self.actionRequest_Feature.setObjectName(_fromUtf8("actionRequest_Feature"))
        self.actionAbout = QtGui.QAction(CognitiveBattery)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionView_License)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionContribute)
        self.menuHelp.addAction(self.actionBrowse_Issues)
        self.menuHelp.addAction(self.actionReport_Bug)
        self.menuHelp.addAction(self.actionRequest_Feature)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuOptions.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(CognitiveBattery)
        QtCore.QMetaObject.connectSlotsByName(CognitiveBattery)

    def retranslateUi(self, CognitiveBattery):
        CognitiveBattery.setWindowTitle(_translate("CognitiveBattery", "Cognitive Battery", None))
        self.sessionInfoText.setText(_translate("CognitiveBattery", "<html><head/><body><p><span style=\" font-weight:600;\">Session information:</span></p></body></html>", None))
        self.raText.setText(_translate("CognitiveBattery", "Research Assistant:", None))
        self.subNumText.setText(_translate("CognitiveBattery", "Subject #:", None))
        self.experimentIDText.setText(_translate("CognitiveBattery", "Experiment name/ID:", None))
        self.conditionText.setText(_translate("CognitiveBattery", "Condition:", None))
        self.ageText.setText(_translate("CognitiveBattery", "Age:", None))
        self.sexText.setText(_translate("CognitiveBattery", "Sex:", None))
        self.raBox.setStatusTip(_translate("CognitiveBattery", "Enter name of the research assistant", None))
        self.subNumBox.setStatusTip(_translate("CognitiveBattery", "Enter the subject number or ID", None))
        self.experimentIDBox.setStatusTip(_translate("CognitiveBattery", "Enter the experiment name or ID", None))
        self.conditionBox.setStatusTip(_translate("CognitiveBattery", "Enter the current condition", None))
        self.ageBox.setStatusTip(_translate("CognitiveBattery", "Enter the participant\'s age", None))
        self.maleRadio.setText(_translate("CognitiveBattery", "Male", None))
        self.femaleRadio.setText(_translate("CognitiveBattery", "Female", None))
        self.batterySelectText.setText(_translate("CognitiveBattery", "<html><head/><body><p><span style=\" font-weight:600;\">Task selection:</span></p></body></html>", None))
        self.reorderText.setText(_translate("CognitiveBattery", "(use the Up/Down buttons to set adminstration order)", None))
        self.randomOrderCheck.setStatusTip(_translate("CognitiveBattery", "Run tasks in a random order", None))
        self.randomOrderCheck.setText(_translate("CognitiveBattery", "Random order", None))
        self.selectAllButton.setStatusTip(_translate("CognitiveBattery", "Select all tasks", None))
        self.selectAllButton.setText(_translate("CognitiveBattery", "Select All", None))
        self.deselectAllButton.setStatusTip(_translate("CognitiveBattery", "Deselect all tasks", None))
        self.deselectAllButton.setText(_translate("CognitiveBattery", "Deselect All", None))
        __sortingEnabled = self.taskList.isSortingEnabled()
        self.taskList.setSortingEnabled(False)
        item = self.taskList.item(0)
        item.setText(_translate("CognitiveBattery", "Attention Network Test (ANT)", None))
        item = self.taskList.item(1)
        item.setText(_translate("CognitiveBattery", "Sustained Attention to Response Task (SART)", None))
        item = self.taskList.item(2)
        item.setText(_translate("CognitiveBattery", "Digit Span (backwards)", None))
        item = self.taskList.item(3)
        item.setText(_translate("CognitiveBattery", "Mental Rotation Task", None))
        item = self.taskList.item(4)
        item.setText(_translate("CognitiveBattery", "Raven\'s Progressive Matrices", None))
        self.taskList.setSortingEnabled(__sortingEnabled)
        self.upButton.setStatusTip(_translate("CognitiveBattery", "Move selected task up in order of administration", None))
        self.upButton.setText(_translate("CognitiveBattery", "Up", None))
        self.downButton.setStatusTip(_translate("CognitiveBattery", "Move selected task down in order of administration", None))
        self.downButton.setText(_translate("CognitiveBattery", "Down", None))
        self.startButton.setStatusTip(_translate("CognitiveBattery", "Start the testing session", None))
        self.startButton.setText(_translate("CognitiveBattery", "Start", None))
        self.cancelButton.setStatusTip(_translate("CognitiveBattery", "Quit the battery", None))
        self.cancelButton.setText(_translate("CognitiveBattery", "Cancel", None))
        self.menuFile.setTitle(_translate("CognitiveBattery", "File", None))
        self.menuHelp.setTitle(_translate("CognitiveBattery", "Help", None))
        self.menuOptions.setTitle(_translate("CognitiveBattery", "Options", None))
        self.actionSettings.setText(_translate("CognitiveBattery", "Settings", None))
        self.actionSettings.setStatusTip(_translate("CognitiveBattery", "Change battery settings", None))
        self.actionExit.setText(_translate("CognitiveBattery", "Exit", None))
        self.actionExit.setStatusTip(_translate("CognitiveBattery", "Exit the battery", None))
        self.actionDocumentation.setText(_translate("CognitiveBattery", "Documentation", None))
        self.actionDocumentation.setStatusTip(_translate("CognitiveBattery", "Visit the GitHub support page", None))
        self.actionView_License.setText(_translate("CognitiveBattery", "View License", None))
        self.actionView_License.setStatusTip(_translate("CognitiveBattery", "View application license", None))
        self.actionContribute.setText(_translate("CognitiveBattery", "Contribute", None))
        self.actionContribute.setStatusTip(_translate("CognitiveBattery", "Contribute code on GitHub", None))
        self.actionBrowse_Issues.setText(_translate("CognitiveBattery", "Browse Issues", None))
        self.actionBrowse_Issues.setStatusTip(_translate("CognitiveBattery", "Browse known bugs and issues", None))
        self.actionReport_Bug.setText(_translate("CognitiveBattery", "Report Bug", None))
        self.actionReport_Bug.setStatusTip(_translate("CognitiveBattery", "Report a bug", None))
        self.actionRequest_Feature.setText(_translate("CognitiveBattery", "Request Feature", None))
        self.actionRequest_Feature.setStatusTip(_translate("CognitiveBattery", "Request a feature", None))
        self.actionAbout.setText(_translate("CognitiveBattery", "About", None))
        self.actionAbout.setStatusTip(_translate("CognitiveBattery", "About the battery", None))

