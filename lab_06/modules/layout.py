# Form implementation generated from reading ui file 'design/lab_06.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1389, 771)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1381, 761))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.mainFrame = QtWidgets.QFrame(self.main_tab)
        self.mainFrame.setGeometry(QtCore.QRect(0, 0, 1011, 741))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.graphicsView = GraphicsView(self.mainFrame)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1011, 731))
        self.graphicsView.setObjectName("graphicsView")
        self.frame_5 = QtWidgets.QFrame(self.main_tab)
        self.frame_5.setGeometry(QtCore.QRect(1150, 660, 221, 61))
        self.frame_5.setAutoFillBackground(True)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.exitButton = QtWidgets.QPushButton(self.frame_5)
        self.exitButton.setGeometry(QtCore.QRect(130, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.exitButton.setObjectName("exitButton")
        self.resetButton = QtWidgets.QPushButton(self.frame_5)
        self.resetButton.setGeometry(QtCore.QRect(10, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.frame_9 = QtWidgets.QFrame(self.main_tab)
        self.frame_9.setGeometry(QtCore.QRect(1020, 250, 351, 191))
        self.frame_9.setAutoFillBackground(True)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setLineWidth(5)
        self.frame_9.setObjectName("frame_9")
        self.label_23 = QtWidgets.QLabel(self.frame_9)
        self.label_23.setGeometry(QtCore.QRect(0, 0, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.borderColorButton = QtWidgets.QPushButton(self.frame_9)
        self.borderColorButton.setGeometry(QtCore.QRect(260, 60, 80, 31))
        self.borderColorButton.setObjectName("borderColorButton")
        self.borderColorLabel = QtWidgets.QLabel(self.frame_9)
        self.borderColorLabel.setGeometry(QtCore.QRect(40, 60, 201, 31))
        self.borderColorLabel.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.borderColorLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.borderColorLabel.setText("")
        self.borderColorLabel.setObjectName("borderColorLabel")
        self.fillColorLabel = QtWidgets.QLabel(self.frame_9)
        self.fillColorLabel.setGeometry(QtCore.QRect(40, 140, 201, 31))
        self.fillColorLabel.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.fillColorLabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.fillColorLabel.setText("")
        self.fillColorLabel.setObjectName("fillColorLabel")
        self.fillColorButton = QtWidgets.QPushButton(self.frame_9)
        self.fillColorButton.setGeometry(QtCore.QRect(260, 140, 80, 31))
        self.fillColorButton.setObjectName("fillColorButton")
        self.label_24 = QtWidgets.QLabel(self.frame_9)
        self.label_24.setGeometry(QtCore.QRect(0, 30, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_9)
        self.label_25.setGeometry(QtCore.QRect(0, 110, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_25.setWordWrap(True)
        self.label_25.setObjectName("label_25")
        self.frame_4 = QtWidgets.QFrame(self.main_tab)
        self.frame_4.setGeometry(QtCore.QRect(1020, 140, 351, 101))
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(5)
        self.frame_4.setObjectName("frame_4")
        self.pointXForm = QtWidgets.QLineEdit(self.frame_4)
        self.pointXForm.setGeometry(QtCore.QRect(40, 30, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pointXForm.setFont(font)
        self.pointXForm.setObjectName("pointXForm")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 31, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_15.setScaledContents(False)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(190, 30, 31, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_17.setScaledContents(False)
        self.label_17.setObjectName("label_17")
        self.pointYForm = QtWidgets.QLineEdit(self.frame_4)
        self.pointYForm.setGeometry(QtCore.QRect(220, 30, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pointYForm.setFont(font)
        self.pointYForm.setObjectName("pointYForm")
        self.addPointButton = QtWidgets.QPushButton(self.frame_4)
        self.addPointButton.setGeometry(QtCore.QRect(10, 60, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addPointButton.setFont(font)
        self.addPointButton.setStyleSheet("")
        self.addPointButton.setObjectName("addPointButton")
        self.frame_10 = QtWidgets.QFrame(self.main_tab)
        self.frame_10.setGeometry(QtCore.QRect(1020, 0, 351, 121))
        self.frame_10.setAutoFillBackground(True)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setLineWidth(5)
        self.frame_10.setObjectName("frame_10")
        self.label_26 = QtWidgets.QLabel(self.frame_10)
        self.label_26.setGeometry(QtCore.QRect(0, 0, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.delayButton = QtWidgets.QRadioButton(self.frame_10)
        self.delayButton.setGeometry(QtCore.QRect(20, 40, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delayButton.setFont(font)
        self.delayButton.setObjectName("delayButton")
        self.delaySlider = QtWidgets.QSlider(self.frame_10)
        self.delaySlider.setGeometry(QtCore.QRect(20, 90, 311, 16))
        self.delaySlider.setMinimum(1)
        self.delaySlider.setMaximum(100)
        self.delaySlider.setProperty("value", 50)
        self.delaySlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.delaySlider.setInvertedAppearance(False)
        self.delaySlider.setInvertedControls(False)
        self.delaySlider.setObjectName("delaySlider")
        self.label = QtWidgets.QLabel(self.frame_10)
        self.label.setGeometry(QtCore.QRect(300, 70, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.loggerFrame = QtWidgets.QFrame(self.main_tab)
        self.loggerFrame.setGeometry(QtCore.QRect(1020, 590, 351, 61))
        self.loggerFrame.setAutoFillBackground(True)
        self.loggerFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.loggerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.loggerFrame.setObjectName("loggerFrame")
        self.loggerLabel = QtWidgets.QLabel(self.loggerFrame)
        self.loggerLabel.setGeometry(QtCore.QRect(10, 0, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loggerLabel.setFont(font)
        self.loggerLabel.setWordWrap(True)
        self.loggerLabel.setObjectName("loggerLabel")
        self.frame_7 = QtWidgets.QFrame(self.main_tab)
        self.frame_7.setGeometry(QtCore.QRect(1020, 450, 351, 61))
        self.frame_7.setAutoFillBackground(True)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.drawButton = QtWidgets.QPushButton(self.frame_7)
        self.drawButton.setGeometry(QtCore.QRect(10, 10, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.drawButton.setFont(font)
        self.drawButton.setObjectName("drawButton")
        self.frame_8 = QtWidgets.QFrame(self.main_tab)
        self.frame_8.setGeometry(QtCore.QRect(1020, 520, 351, 61))
        self.frame_8.setAutoFillBackground(True)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.encloseButton = QtWidgets.QPushButton(self.frame_8)
        self.encloseButton.setGeometry(QtCore.QRect(10, 10, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.encloseButton.setFont(font)
        self.encloseButton.setObjectName("encloseButton")
        self.tabWidget.addTab(self.main_tab, "")
        self.statistic_tab = QtWidgets.QWidget()
        self.statistic_tab.setObjectName("statistic_tab")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.statistic_tab)
        self.graphicsView_2.setGeometry(QtCore.QRect(80, 70, 1131, 581))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.frame_6 = QtWidgets.QFrame(self.statistic_tab)
        self.frame_6.setGeometry(QtCore.QRect(1280, 670, 91, 51))
        self.frame_6.setAutoFillBackground(True)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.exitButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.exitButton_2.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exitButton_2.setFont(font)
        self.exitButton_2.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.exitButton_2.setObjectName("exitButton_2")
        self.frame = QtWidgets.QFrame(self.statistic_tab)
        self.frame.setGeometry(QtCore.QRect(1270, 289, 101, 61))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.analysisButton = QtWidgets.QPushButton(self.frame)
        self.analysisButton.setGeometry(QtCore.QRect(10, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.analysisButton.setFont(font)
        self.analysisButton.setObjectName("analysisButton")
        self.tabWidget.addTab(self.statistic_tab, "")
        self.actionabc = QtGui.QAction(Dialog)
        self.actionabc.setObjectName("actionabc")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pointXForm, self.pointYForm)
        Dialog.setTabOrder(self.pointYForm, self.addPointButton)
        Dialog.setTabOrder(self.addPointButton, self.resetButton)
        Dialog.setTabOrder(self.resetButton, self.exitButton)
        Dialog.setTabOrder(self.exitButton, self.graphicsView)
        Dialog.setTabOrder(self.graphicsView, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.graphicsView_2)
        Dialog.setTabOrder(self.graphicsView_2, self.exitButton_2)
        Dialog.setTabOrder(self.exitButton_2, self.analysisButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.exitButton.setText(_translate("Dialog", "Выход"))
        self.resetButton.setText(_translate("Dialog", "Сброс"))
        self.label_23.setText(_translate("Dialog", "Цвет"))
        self.borderColorButton.setText(_translate("Dialog", "Выбрать"))
        self.fillColorButton.setText(_translate("Dialog", "Выбрать"))
        self.label_24.setText(_translate("Dialog", "Цвет Границ"))
        self.label_25.setText(_translate("Dialog", "Цвет Заполнения"))
        self.pointXForm.setText(_translate("Dialog", "400"))
        self.label_15.setText(_translate("Dialog", "х ="))
        self.label_16.setText(_translate("Dialog", "Добавить Точку"))
        self.label_17.setText(_translate("Dialog", "y ="))
        self.pointYForm.setText(_translate("Dialog", "400"))
        self.addPointButton.setText(_translate("Dialog", "Добавить"))
        self.label_26.setText(_translate("Dialog", "Задержка"))
        self.delayButton.setText(_translate("Dialog", "Задержка"))
        self.label.setText(_translate("Dialog", "Max"))
        self.label_2.setText(_translate("Dialog", "Min"))
        self.loggerLabel.setText(_translate("Dialog", "Статус: ОК"))
        self.drawButton.setText(_translate("Dialog", "Выполнить закраску"))
        self.encloseButton.setText(_translate("Dialog", "Замкнуть"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), _translate("Dialog", "Main Tab"))
        self.exitButton_2.setText(_translate("Dialog", "Выход"))
        self.analysisButton.setText(_translate("Dialog", "Анализ"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.statistic_tab), _translate("Dialog", "Statistic"))
        self.actionabc.setText(_translate("Dialog", "abc"))
from .graphicsView import GraphicsView
