# Form implementation generated from reading ui file 'design/lab_03.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1387, 771)
        self.tabWidget = QtWidgets.QTabWidget(parent=Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1381, 761))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.mainFrame = QtWidgets.QFrame(parent=self.main_tab)
        self.mainFrame.setGeometry(QtCore.QRect(0, 0, 1151, 741))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.mainFrame)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1151, 731))
        self.graphicsView.setObjectName("graphicsView")
        self.loggerFrame = QtWidgets.QFrame(parent=self.main_tab)
        self.loggerFrame.setGeometry(QtCore.QRect(1160, 610, 211, 51))
        self.loggerFrame.setAutoFillBackground(True)
        self.loggerFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.loggerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.loggerFrame.setObjectName("loggerFrame")
        self.loggerLabel = QtWidgets.QLabel(parent=self.loggerFrame)
        self.loggerLabel.setGeometry(QtCore.QRect(10, 0, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loggerLabel.setFont(font)
        self.loggerLabel.setWordWrap(True)
        self.loggerLabel.setObjectName("loggerLabel")
        self.frame_5 = QtWidgets.QFrame(parent=self.main_tab)
        self.frame_5.setGeometry(QtCore.QRect(1160, 670, 211, 51))
        self.frame_5.setAutoFillBackground(True)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.exitButton = QtWidgets.QPushButton(parent=self.frame_5)
        self.exitButton.setGeometry(QtCore.QRect(130, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.exitButton.setObjectName("exitButton")
        self.resetButton = QtWidgets.QPushButton(parent=self.frame_5)
        self.resetButton.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.frame_8 = QtWidgets.QFrame(parent=self.main_tab)
        self.frame_8.setGeometry(QtCore.QRect(1160, 230, 211, 221))
        self.frame_8.setAutoFillBackground(True)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setLineWidth(5)
        self.frame_8.setObjectName("frame_8")
        self.label_22 = QtWidgets.QLabel(parent=self.frame_8)
        self.label_22.setGeometry(QtCore.QRect(0, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.algoGroupBox = QtWidgets.QGroupBox(parent=self.frame_8)
        self.algoGroupBox.setGeometry(QtCore.QRect(10, 30, 191, 181))
        self.algoGroupBox.setTitle("")
        self.algoGroupBox.setCheckable(False)
        self.algoGroupBox.setChecked(False)
        self.algoGroupBox.setObjectName("algoGroupBox")
        self.ddaAlgoButton = QtWidgets.QToolButton(parent=self.algoGroupBox)
        self.ddaAlgoButton.setGeometry(QtCore.QRect(0, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ddaAlgoButton.setFont(font)
        self.ddaAlgoButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.ddaAlgoButton.setCheckable(True)
        self.ddaAlgoButton.setChecked(True)
        self.ddaAlgoButton.setAutoExclusive(True)
        self.ddaAlgoButton.setObjectName("ddaAlgoButton")
        self.libAlgoButton = QtWidgets.QToolButton(parent=self.algoGroupBox)
        self.libAlgoButton.setGeometry(QtCore.QRect(0, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.libAlgoButton.setFont(font)
        self.libAlgoButton.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.libAlgoButton.setCheckable(True)
        self.libAlgoButton.setChecked(False)
        self.libAlgoButton.setAutoExclusive(True)
        self.libAlgoButton.setObjectName("libAlgoButton")
        self.brezFloatAlgoButton = QtWidgets.QToolButton(parent=self.algoGroupBox)
        self.brezFloatAlgoButton.setGeometry(QtCore.QRect(0, 60, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.brezFloatAlgoButton.setFont(font)
        self.brezFloatAlgoButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.brezFloatAlgoButton.setCheckable(True)
        self.brezFloatAlgoButton.setAutoExclusive(True)
        self.brezFloatAlgoButton.setObjectName("brezFloatAlgoButton")
        self.brezIntAlgoButton = QtWidgets.QToolButton(parent=self.algoGroupBox)
        self.brezIntAlgoButton.setGeometry(QtCore.QRect(0, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.brezIntAlgoButton.setFont(font)
        self.brezIntAlgoButton.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.brezIntAlgoButton.setCheckable(True)
        self.brezIntAlgoButton.setAutoExclusive(True)
        self.brezIntAlgoButton.setObjectName("brezIntAlgoButton")
        self.brezAAAlgoButton = QtWidgets.QPushButton(parent=self.algoGroupBox)
        self.brezAAAlgoButton.setGeometry(QtCore.QRect(0, 120, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.brezAAAlgoButton.setFont(font)
        self.brezAAAlgoButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.brezAAAlgoButton.setCheckable(True)
        self.brezAAAlgoButton.setChecked(False)
        self.brezAAAlgoButton.setAutoRepeat(False)
        self.brezAAAlgoButton.setAutoExclusive(True)
        self.brezAAAlgoButton.setObjectName("brezAAAlgoButton")
        self.wuAlgoButton = QtWidgets.QToolButton(parent=self.algoGroupBox)
        self.wuAlgoButton.setGeometry(QtCore.QRect(0, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.wuAlgoButton.setFont(font)
        self.wuAlgoButton.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.wuAlgoButton.setCheckable(True)
        self.wuAlgoButton.setAutoExclusive(True)
        self.wuAlgoButton.setObjectName("wuAlgoButton")
        self.frame_9 = QtWidgets.QFrame(parent=self.main_tab)
        self.frame_9.setGeometry(QtCore.QRect(1160, 450, 211, 161))
        self.frame_9.setAutoFillBackground(True)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setLineWidth(5)
        self.frame_9.setObjectName("frame_9")
        self.label_23 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_23.setGeometry(QtCore.QRect(0, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.colorGroupBox = QtWidgets.QGroupBox(parent=self.frame_9)
        self.colorGroupBox.setGeometry(QtCore.QRect(10, 30, 181, 121))
        self.colorGroupBox.setTitle("")
        self.colorGroupBox.setObjectName("colorGroupBox")
        self.blueButton = QtWidgets.QToolButton(parent=self.colorGroupBox)
        self.blueButton.setGeometry(QtCore.QRect(0, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.blueButton.setFont(font)
        self.blueButton.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.blueButton.setCheckable(True)
        self.blueButton.setChecked(False)
        self.blueButton.setAutoExclusive(True)
        self.blueButton.setObjectName("blueButton")
        self.whiteButton = QtWidgets.QToolButton(parent=self.colorGroupBox)
        self.whiteButton.setGeometry(QtCore.QRect(0, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.whiteButton.setFont(font)
        self.whiteButton.setStyleSheet("")
        self.whiteButton.setCheckable(True)
        self.whiteButton.setChecked(False)
        self.whiteButton.setAutoExclusive(True)
        self.whiteButton.setObjectName("whiteButton")
        self.blackButton = QtWidgets.QToolButton(parent=self.colorGroupBox)
        self.blackButton.setGeometry(QtCore.QRect(0, 90, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.blackButton.setFont(font)
        self.blackButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(61, 61, 61);")
        self.blackButton.setCheckable(True)
        self.blackButton.setChecked(False)
        self.blackButton.setAutoExclusive(True)
        self.blackButton.setObjectName("blackButton")
        self.redButton = QtWidgets.QToolButton(parent=self.colorGroupBox)
        self.redButton.setGeometry(QtCore.QRect(0, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.redButton.setFont(font)
        self.redButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.redButton.setCheckable(True)
        self.redButton.setChecked(True)
        self.redButton.setAutoExclusive(True)
        self.redButton.setObjectName("redButton")
        self.frame_4 = QtWidgets.QFrame(parent=self.main_tab)
        self.frame_4.setGeometry(QtCore.QRect(1160, 0, 211, 131))
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(5)
        self.frame_4.setObjectName("frame_4")
        self.point_aXForm = QtWidgets.QLineEdit(parent=self.frame_4)
        self.point_aXForm.setGeometry(QtCore.QRect(50, 30, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.point_aXForm.setFont(font)
        self.point_aXForm.setObjectName("point_aXForm")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 41, 20))
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
        self.label_16 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(120, 30, 41, 21))
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
        self.point_aYForm = QtWidgets.QLineEdit(parent=self.frame_4)
        self.point_aYForm.setGeometry(QtCore.QRect(160, 30, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.point_aYForm.setFont(font)
        self.point_aYForm.setObjectName("point_aYForm")
        self.label_18 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(10, 60, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_18.setScaledContents(False)
        self.label_18.setObjectName("label_18")
        self.point_bYForm = QtWidgets.QLineEdit(parent=self.frame_4)
        self.point_bYForm.setGeometry(QtCore.QRect(160, 60, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.point_bYForm.setFont(font)
        self.point_bYForm.setText("")
        self.point_bYForm.setObjectName("point_bYForm")
        self.label_20 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_20.setGeometry(QtCore.QRect(120, 60, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_20.setScaledContents(False)
        self.label_20.setObjectName("label_20")
        self.point_bXForm = QtWidgets.QLineEdit(parent=self.frame_4)
        self.point_bXForm.setGeometry(QtCore.QRect(50, 60, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.point_bXForm.setFont(font)
        self.point_bXForm.setText("")
        self.point_bXForm.setObjectName("point_bXForm")
        self.drawButton = QtWidgets.QPushButton(parent=self.frame_4)
        self.drawButton.setGeometry(QtCore.QRect(10, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.drawButton.setFont(font)
        self.drawButton.setStyleSheet("")
        self.drawButton.setObjectName("drawButton")
        self.frame_7 = QtWidgets.QFrame(parent=self.main_tab)
        self.frame_7.setGeometry(QtCore.QRect(1160, 130, 211, 101))
        self.frame_7.setAutoFillBackground(True)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setLineWidth(5)
        self.frame_7.setObjectName("frame_7")
        self.stepForm = QtWidgets.QLineEdit(parent=self.frame_7)
        self.stepForm.setGeometry(QtCore.QRect(70, 30, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stepForm.setFont(font)
        self.stepForm.setObjectName("stepForm")
        self.label_19 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_19.setGeometry(QtCore.QRect(10, 30, 61, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_19.setScaledContents(False)
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.label_24 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_24.setGeometry(QtCore.QRect(130, 30, 31, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_24.setScaledContents(False)
        self.label_24.setObjectName("label_24")
        self.radiusForm = QtWidgets.QLineEdit(parent=self.frame_7)
        self.radiusForm.setGeometry(QtCore.QRect(160, 30, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radiusForm.setFont(font)
        self.radiusForm.setObjectName("radiusForm")
        self.drawSunButton = QtWidgets.QPushButton(parent=self.frame_7)
        self.drawSunButton.setGeometry(QtCore.QRect(10, 60, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.drawSunButton.setFont(font)
        self.drawSunButton.setStyleSheet("")
        self.drawSunButton.setObjectName("drawSunButton")
        self.tabWidget.addTab(self.main_tab, "")
        self.statistic_tab = QtWidgets.QWidget()
        self.statistic_tab.setObjectName("statistic_tab")
        self.graphicsView_2 = QtWidgets.QGraphicsView(parent=self.statistic_tab)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 621, 731))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.frame_6 = QtWidgets.QFrame(parent=self.statistic_tab)
        self.frame_6.setGeometry(QtCore.QRect(1280, 670, 91, 51))
        self.frame_6.setAutoFillBackground(True)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.exitButton_2 = QtWidgets.QPushButton(parent=self.frame_6)
        self.exitButton_2.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exitButton_2.setFont(font)
        self.exitButton_2.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.exitButton_2.setObjectName("exitButton_2")
        self.frame = QtWidgets.QFrame(parent=self.statistic_tab)
        self.frame.setGeometry(QtCore.QRect(1270, 289, 101, 61))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.analysisButton = QtWidgets.QPushButton(parent=self.frame)
        self.analysisButton.setGeometry(QtCore.QRect(10, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.analysisButton.setFont(font)
        self.analysisButton.setObjectName("analysisButton")
        self.graphicsView_3 = QtWidgets.QGraphicsView(parent=self.statistic_tab)
        self.graphicsView_3.setGeometry(QtCore.QRect(630, 0, 631, 731))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.tabWidget.addTab(self.statistic_tab, "")
        self.actionabc = QtGui.QAction(parent=Dialog)
        self.actionabc.setObjectName("actionabc")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loggerLabel.setText(_translate("Dialog", "App started..."))
        self.exitButton.setText(_translate("Dialog", "Выход"))
        self.resetButton.setText(_translate("Dialog", "Сброс"))
        self.label_22.setText(_translate("Dialog", "Алгоритм"))
        self.ddaAlgoButton.setText(_translate("Dialog", "ЦДА"))
        self.libAlgoButton.setText(_translate("Dialog", "Библ. Функция"))
        self.brezFloatAlgoButton.setText(_translate("Dialog", "Брезенхем (float)"))
        self.brezIntAlgoButton.setText(_translate("Dialog", "Брезенхем (int)"))
        self.brezAAAlgoButton.setText(_translate("Dialog", "Брезенхам (сглаж.)"))
        self.wuAlgoButton.setText(_translate("Dialog", "Ву"))
        self.label_23.setText(_translate("Dialog", "Цвет"))
        self.blueButton.setText(_translate("Dialog", "Синий"))
        self.whiteButton.setText(_translate("Dialog", "Белый"))
        self.blackButton.setText(_translate("Dialog", "Черный"))
        self.redButton.setText(_translate("Dialog", "Красный"))
        self.label_15.setText(_translate("Dialog", "х1 ="))
        self.label_16.setText(_translate("Dialog", "Точки"))
        self.label_17.setText(_translate("Dialog", "y1 ="))
        self.label_18.setText(_translate("Dialog", "х2 ="))
        self.label_20.setText(_translate("Dialog", "y2 ="))
        self.drawButton.setText(_translate("Dialog", "Нарисовать"))
        self.label_19.setText(_translate("Dialog", "Шаг ="))
        self.label_21.setText(_translate("Dialog", "Спектр углов (град.)"))
        self.label_24.setText(_translate("Dialog", "r ="))
        self.drawSunButton.setText(_translate("Dialog", "Нарисовать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), _translate("Dialog", "Main Tab"))
        self.exitButton_2.setText(_translate("Dialog", "Выход"))
        self.analysisButton.setText(_translate("Dialog", "Анализ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statistic_tab), _translate("Dialog", "Statistic"))
        self.actionabc.setText(_translate("Dialog", "abc"))
