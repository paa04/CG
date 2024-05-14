# Form implementation generated from reading ui file 'design/lab_04.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1387, 771)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1381, 761))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.mainFrame = QtWidgets.QFrame(self.main_tab)
        self.mainFrame.setGeometry(QtCore.QRect(0, 0, 1011, 741))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.graphicsView = QtWidgets.QGraphicsView(self.mainFrame)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1011, 731))
        self.graphicsView.setObjectName("graphicsView")
        self.frame_5 = QtWidgets.QFrame(self.main_tab)
        self.frame_5.setGeometry(QtCore.QRect(1160, 670, 211, 51))
        self.frame_5.setAutoFillBackground(True)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.exitButton = QtWidgets.QPushButton(self.frame_5)
        self.exitButton.setGeometry(QtCore.QRect(130, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.exitButton.setObjectName("exitButton")
        self.resetButton = QtWidgets.QPushButton(self.frame_5)
        self.resetButton.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.frame_8 = QtWidgets.QFrame(self.main_tab)
        self.frame_8.setGeometry(QtCore.QRect(1020, 310, 351, 191))
        self.frame_8.setAutoFillBackground(True)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setLineWidth(5)
        self.frame_8.setObjectName("frame_8")
        self.label_22 = QtWidgets.QLabel(self.frame_8)
        self.label_22.setGeometry(QtCore.QRect(0, 0, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.algoGroupBox = QtWidgets.QGroupBox(self.frame_8)
        self.algoGroupBox.setGeometry(QtCore.QRect(10, 30, 331, 151))
        self.algoGroupBox.setTitle("")
        self.algoGroupBox.setCheckable(False)
        self.algoGroupBox.setChecked(False)
        self.algoGroupBox.setObjectName("algoGroupBox")
        self.libAlgoButton = QtWidgets.QToolButton(self.algoGroupBox)
        self.libAlgoButton.setGeometry(QtCore.QRect(0, 0, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.libAlgoButton.setFont(font)
        self.libAlgoButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.libAlgoButton.setCheckable(True)
        self.libAlgoButton.setChecked(True)
        self.libAlgoButton.setAutoExclusive(True)
        self.libAlgoButton.setObjectName("libAlgoButton")
        self.canonAlgoButton = QtWidgets.QToolButton(self.algoGroupBox)
        self.canonAlgoButton.setGeometry(QtCore.QRect(0, 30, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.canonAlgoButton.setFont(font)
        self.canonAlgoButton.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.canonAlgoButton.setCheckable(True)
        self.canonAlgoButton.setChecked(False)
        self.canonAlgoButton.setAutoExclusive(True)
        self.canonAlgoButton.setObjectName("canonAlgoButton")
        self.paramAlgoButton = QtWidgets.QToolButton(self.algoGroupBox)
        self.paramAlgoButton.setGeometry(QtCore.QRect(0, 60, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.paramAlgoButton.setFont(font)
        self.paramAlgoButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.paramAlgoButton.setCheckable(True)
        self.paramAlgoButton.setAutoExclusive(True)
        self.paramAlgoButton.setObjectName("paramAlgoButton")
        self.brezAlgoButton = QtWidgets.QToolButton(self.algoGroupBox)
        self.brezAlgoButton.setGeometry(QtCore.QRect(0, 90, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.brezAlgoButton.setFont(font)
        self.brezAlgoButton.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.brezAlgoButton.setCheckable(True)
        self.brezAlgoButton.setAutoExclusive(True)
        self.brezAlgoButton.setObjectName("brezAlgoButton")
        self.midPointAlgoButton = QtWidgets.QPushButton(self.algoGroupBox)
        self.midPointAlgoButton.setGeometry(QtCore.QRect(0, 120, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.midPointAlgoButton.setFont(font)
        self.midPointAlgoButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.midPointAlgoButton.setCheckable(True)
        self.midPointAlgoButton.setChecked(False)
        self.midPointAlgoButton.setAutoRepeat(False)
        self.midPointAlgoButton.setAutoExclusive(True)
        self.midPointAlgoButton.setObjectName("midPointAlgoButton")
        self.frame_9 = QtWidgets.QFrame(self.main_tab)
        self.frame_9.setGeometry(QtCore.QRect(1020, 500, 351, 161))
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
        self.colorGroupBox = QtWidgets.QGroupBox(self.frame_9)
        self.colorGroupBox.setGeometry(QtCore.QRect(10, 30, 331, 121))
        self.colorGroupBox.setTitle("")
        self.colorGroupBox.setObjectName("colorGroupBox")
        self.blueButton = QtWidgets.QToolButton(self.colorGroupBox)
        self.blueButton.setGeometry(QtCore.QRect(0, 30, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.blueButton.setFont(font)
        self.blueButton.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.blueButton.setCheckable(True)
        self.blueButton.setChecked(False)
        self.blueButton.setAutoExclusive(True)
        self.blueButton.setObjectName("blueButton")
        self.whiteButton = QtWidgets.QToolButton(self.colorGroupBox)
        self.whiteButton.setGeometry(QtCore.QRect(0, 0, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.whiteButton.setFont(font)
        self.whiteButton.setStyleSheet("")
        self.whiteButton.setCheckable(True)
        self.whiteButton.setChecked(False)
        self.whiteButton.setAutoExclusive(True)
        self.whiteButton.setObjectName("whiteButton")
        self.blackButton = QtWidgets.QToolButton(self.colorGroupBox)
        self.blackButton.setGeometry(QtCore.QRect(0, 90, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.blackButton.setFont(font)
        self.blackButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(61, 61, 61);")
        self.blackButton.setCheckable(True)
        self.blackButton.setChecked(False)
        self.blackButton.setAutoExclusive(True)
        self.blackButton.setObjectName("blackButton")
        self.redButton = QtWidgets.QToolButton(self.colorGroupBox)
        self.redButton.setGeometry(QtCore.QRect(0, 60, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.redButton.setFont(font)
        self.redButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.redButton.setCheckable(True)
        self.redButton.setChecked(True)
        self.redButton.setAutoExclusive(True)
        self.redButton.setObjectName("redButton")
        self.frame_4 = QtWidgets.QFrame(self.main_tab)
        self.frame_4.setGeometry(QtCore.QRect(1020, 0, 211, 131))
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(5)
        self.frame_4.setObjectName("frame_4")
        self.centerXForm = QtWidgets.QLineEdit(self.frame_4)
        self.centerXForm.setGeometry(QtCore.QRect(50, 30, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.centerXForm.setFont(font)
        self.centerXForm.setObjectName("centerXForm")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
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
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_4)
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
        self.centerYForm = QtWidgets.QLineEdit(self.frame_4)
        self.centerYForm.setGeometry(QtCore.QRect(160, 30, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.centerYForm.setFont(font)
        self.centerYForm.setObjectName("centerYForm")
        self.label_18 = QtWidgets.QLabel(self.frame_4)
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
        self.radius_bForm = QtWidgets.QLineEdit(self.frame_4)
        self.radius_bForm.setEnabled(False)
        self.radius_bForm.setGeometry(QtCore.QRect(160, 60, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radius_bForm.setFont(font)
        self.radius_bForm.setText("")
        self.radius_bForm.setDragEnabled(False)
        self.radius_bForm.setReadOnly(False)
        self.radius_bForm.setObjectName("radius_bForm")
        self.r2Label = QtWidgets.QLabel(self.frame_4)
        self.r2Label.setEnabled(False)
        self.r2Label.setGeometry(QtCore.QRect(120, 60, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2Label.sizePolicy().hasHeightForWidth())
        self.r2Label.setSizePolicy(sizePolicy)
        self.r2Label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.r2Label.setFont(font)
        self.r2Label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.r2Label.setScaledContents(False)
        self.r2Label.setObjectName("r2Label")
        self.radius_aForm = QtWidgets.QLineEdit(self.frame_4)
        self.radius_aForm.setGeometry(QtCore.QRect(50, 60, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radius_aForm.setFont(font)
        self.radius_aForm.setObjectName("radius_aForm")
        self.drawButton = QtWidgets.QPushButton(self.frame_4)
        self.drawButton.setGeometry(QtCore.QRect(10, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.drawButton.setFont(font)
        self.drawButton.setStyleSheet("")
        self.drawButton.setObjectName("drawButton")
        self.frame_7 = QtWidgets.QFrame(self.main_tab)
        self.frame_7.setGeometry(QtCore.QRect(1020, 140, 351, 171))
        self.frame_7.setAutoFillBackground(True)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setLineWidth(5)
        self.frame_7.setObjectName("frame_7")
        self.stepForm = QtWidgets.QLineEdit(self.frame_7)
        self.stepForm.setGeometry(QtCore.QRect(70, 70, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stepForm.setFont(font)
        self.stepForm.setObjectName("stepForm")
        self.label_19 = QtWidgets.QLabel(self.frame_7)
        self.label_19.setGeometry(QtCore.QRect(10, 70, 61, 20))
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
        self.label_21 = QtWidgets.QLabel(self.frame_7)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.label_24 = QtWidgets.QLabel(self.frame_7)
        self.label_24.setGeometry(QtCore.QRect(250, 70, 51, 21))
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
        self.radius_aSunForm = QtWidgets.QLineEdit(self.frame_7)
        self.radius_aSunForm.setGeometry(QtCore.QRect(300, 70, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radius_aSunForm.setFont(font)
        self.radius_aSunForm.setObjectName("radius_aSunForm")
        self.drawSunButton = QtWidgets.QPushButton(self.frame_7)
        self.drawSunButton.setGeometry(QtCore.QRect(80, 130, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.drawSunButton.setFont(font)
        self.drawSunButton.setStyleSheet("")
        self.drawSunButton.setObjectName("drawSunButton")
        self.centerSunYForm = QtWidgets.QLineEdit(self.frame_7)
        self.centerSunYForm.setGeometry(QtCore.QRect(180, 100, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.centerSunYForm.setFont(font)
        self.centerSunYForm.setObjectName("centerSunYForm")
        self.label_27 = QtWidgets.QLabel(self.frame_7)
        self.label_27.setGeometry(QtCore.QRect(140, 70, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_27.setFont(font)
        self.label_27.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_27.setScaledContents(False)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_7)
        self.label_28.setGeometry(QtCore.QRect(140, 100, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_28.setFont(font)
        self.label_28.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_28.setScaledContents(False)
        self.label_28.setObjectName("label_28")
        self.centerSunXForm = QtWidgets.QLineEdit(self.frame_7)
        self.centerSunXForm.setGeometry(QtCore.QRect(180, 70, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.centerSunXForm.setFont(font)
        self.centerSunXForm.setObjectName("centerSunXForm")
        self.radius_bSunForm = QtWidgets.QLineEdit(self.frame_7)
        self.radius_bSunForm.setEnabled(False)
        self.radius_bSunForm.setGeometry(QtCore.QRect(300, 100, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radius_bSunForm.setFont(font)
        self.radius_bSunForm.setObjectName("radius_bSunForm")
        self.r2SunLabel = QtWidgets.QLabel(self.frame_7)
        self.r2SunLabel.setEnabled(False)
        self.r2SunLabel.setGeometry(QtCore.QRect(250, 100, 51, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r2SunLabel.sizePolicy().hasHeightForWidth())
        self.r2SunLabel.setSizePolicy(sizePolicy)
        self.r2SunLabel.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.r2SunLabel.setFont(font)
        self.r2SunLabel.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.r2SunLabel.setScaledContents(False)
        self.r2SunLabel.setObjectName("r2SunLabel")
        self.label_30 = QtWidgets.QLabel(self.frame_7)
        self.label_30.setGeometry(QtCore.QRect(30, 100, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_30.setFont(font)
        self.label_30.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_30.setScaledContents(False)
        self.label_30.setObjectName("label_30")
        self.amountForm = QtWidgets.QLineEdit(self.frame_7)
        self.amountForm.setGeometry(QtCore.QRect(70, 100, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.amountForm.setFont(font)
        self.amountForm.setObjectName("amountForm")
        self.label_31 = QtWidgets.QLabel(self.frame_7)
        self.label_31.setGeometry(QtCore.QRect(140, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.frame_10 = QtWidgets.QFrame(self.main_tab)
        self.frame_10.setGeometry(QtCore.QRect(1230, 0, 141, 131))
        self.frame_10.setAutoFillBackground(True)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setLineWidth(5)
        self.frame_10.setObjectName("frame_10")
        self.label_26 = QtWidgets.QLabel(self.frame_10)
        self.label_26.setGeometry(QtCore.QRect(0, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.figureGroupBox = QtWidgets.QGroupBox(self.frame_10)
        self.figureGroupBox.setGeometry(QtCore.QRect(10, 40, 121, 71))
        self.figureGroupBox.setTitle("")
        self.figureGroupBox.setObjectName("figureGroupBox")
        self.ellipseButton = QtWidgets.QToolButton(self.figureGroupBox)
        self.ellipseButton.setGeometry(QtCore.QRect(0, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ellipseButton.setFont(font)
        self.ellipseButton.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.ellipseButton.setCheckable(True)
        self.ellipseButton.setChecked(False)
        self.ellipseButton.setAutoExclusive(True)
        self.ellipseButton.setObjectName("ellipseButton")
        self.circleButton = QtWidgets.QToolButton(self.figureGroupBox)
        self.circleButton.setGeometry(QtCore.QRect(0, 0, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.circleButton.setFont(font)
        self.circleButton.setStyleSheet("")
        self.circleButton.setCheckable(True)
        self.circleButton.setChecked(True)
        self.circleButton.setAutoExclusive(True)
        self.circleButton.setObjectName("circleButton")
        self.loggerFrame = QtWidgets.QFrame(self.main_tab)
        self.loggerFrame.setGeometry(QtCore.QRect(1020, 670, 141, 51))
        self.loggerFrame.setAutoFillBackground(True)
        self.loggerFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.loggerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.loggerFrame.setObjectName("loggerFrame")
        self.loggerLabel = QtWidgets.QLabel(self.loggerFrame)
        self.loggerLabel.setGeometry(QtCore.QRect(10, 0, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loggerLabel.setFont(font)
        self.loggerLabel.setWordWrap(True)
        self.loggerLabel.setObjectName("loggerLabel")
        self.tabWidget.addTab(self.main_tab, "")
        self.statistic_tab = QtWidgets.QWidget()
        self.statistic_tab.setObjectName("statistic_tab")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.statistic_tab)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 621, 731))
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
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.statistic_tab)
        self.graphicsView_3.setGeometry(QtCore.QRect(630, 0, 631, 731))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.tabWidget.addTab(self.statistic_tab, "")
        self.actionabc = QtGui.QAction(Dialog)
        self.actionabc.setObjectName("actionabc")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.centerXForm, self.centerYForm)
        Dialog.setTabOrder(self.centerYForm, self.radius_aForm)
        Dialog.setTabOrder(self.radius_aForm, self.radius_bForm)
        Dialog.setTabOrder(self.radius_bForm, self.drawButton)
        Dialog.setTabOrder(self.drawButton, self.stepForm)
        Dialog.setTabOrder(self.stepForm, self.amountForm)
        Dialog.setTabOrder(self.amountForm, self.centerSunXForm)
        Dialog.setTabOrder(self.centerSunXForm, self.centerSunYForm)
        Dialog.setTabOrder(self.centerSunYForm, self.radius_aSunForm)
        Dialog.setTabOrder(self.radius_aSunForm, self.radius_bSunForm)
        Dialog.setTabOrder(self.radius_bSunForm, self.drawSunButton)
        Dialog.setTabOrder(self.drawSunButton, self.libAlgoButton)
        Dialog.setTabOrder(self.libAlgoButton, self.canonAlgoButton)
        Dialog.setTabOrder(self.canonAlgoButton, self.paramAlgoButton)
        Dialog.setTabOrder(self.paramAlgoButton, self.brezAlgoButton)
        Dialog.setTabOrder(self.brezAlgoButton, self.midPointAlgoButton)
        Dialog.setTabOrder(self.midPointAlgoButton, self.whiteButton)
        Dialog.setTabOrder(self.whiteButton, self.blueButton)
        Dialog.setTabOrder(self.blueButton, self.redButton)
        Dialog.setTabOrder(self.redButton, self.blackButton)
        Dialog.setTabOrder(self.blackButton, self.resetButton)
        Dialog.setTabOrder(self.resetButton, self.exitButton)
        Dialog.setTabOrder(self.exitButton, self.ellipseButton)
        Dialog.setTabOrder(self.ellipseButton, self.circleButton)
        Dialog.setTabOrder(self.circleButton, self.graphicsView)
        Dialog.setTabOrder(self.graphicsView, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.graphicsView_2)
        Dialog.setTabOrder(self.graphicsView_2, self.exitButton_2)
        Dialog.setTabOrder(self.exitButton_2, self.analysisButton)
        Dialog.setTabOrder(self.analysisButton, self.graphicsView_3)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.exitButton.setText(_translate("Dialog", "Выход"))
        self.resetButton.setText(_translate("Dialog", "Сброс"))
        self.label_22.setText(_translate("Dialog", "Алгоритм"))
        self.libAlgoButton.setText(_translate("Dialog", "Библ. Функция"))
        self.canonAlgoButton.setText(_translate("Dialog", "Каноническое уравнение"))
        self.paramAlgoButton.setText(_translate("Dialog", "Параметрическое уравнение"))
        self.brezAlgoButton.setText(_translate("Dialog", "Алгоритм Брезенхема"))
        self.midPointAlgoButton.setText(_translate("Dialog", "Алгоритм средней точки"))
        self.label_23.setText(_translate("Dialog", "Цвет"))
        self.blueButton.setText(_translate("Dialog", "Синий"))
        self.whiteButton.setText(_translate("Dialog", "Белый"))
        self.blackButton.setText(_translate("Dialog", "Черный"))
        self.redButton.setText(_translate("Dialog", "Красный"))
        self.centerXForm.setText(_translate("Dialog", "400"))
        self.label_15.setText(_translate("Dialog", "х ="))
        self.label_16.setText(_translate("Dialog", "Парметры"))
        self.label_17.setText(_translate("Dialog", "y ="))
        self.centerYForm.setText(_translate("Dialog", "400"))
        self.label_18.setText(_translate("Dialog", "R1 ="))
        self.r2Label.setText(_translate("Dialog", "R2 ="))
        self.radius_aForm.setText(_translate("Dialog", "25"))
        self.drawButton.setText(_translate("Dialog", "Нарисовать"))
        self.stepForm.setText(_translate("Dialog", "15"))
        self.label_19.setText(_translate("Dialog", "Шаг ="))
        self.label_21.setText(_translate("Dialog", "Парметры спектра"))
        self.label_24.setText(_translate("Dialog", "R1 ="))
        self.radius_aSunForm.setText(_translate("Dialog", "50"))
        self.drawSunButton.setText(_translate("Dialog", "Нарисовать"))
        self.centerSunYForm.setText(_translate("Dialog", "400"))
        self.label_27.setText(_translate("Dialog", "х ="))
        self.label_28.setText(_translate("Dialog", "y ="))
        self.centerSunXForm.setText(_translate("Dialog", "400"))
        self.r2SunLabel.setText(_translate("Dialog", "R2 ="))
        self.label_30.setText(_translate("Dialog", "N ="))
        self.amountForm.setText(_translate("Dialog", "20"))
        self.label_31.setText(_translate("Dialog", "Центр"))
        self.label_26.setText(_translate("Dialog", "Фигура"))
        self.ellipseButton.setText(_translate("Dialog", "Эллипс"))
        self.circleButton.setText(_translate("Dialog", "Окружность"))
        self.loggerLabel.setText(_translate("Dialog", "App started..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), _translate("Dialog", "Окно преобразований"))
        self.exitButton_2.setText(_translate("Dialog", "Выход"))
        self.analysisButton.setText(_translate("Dialog", "Анализ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statistic_tab), _translate("Dialog", "Графики"))
        self.actionabc.setText(_translate("Dialog", "abc"))
