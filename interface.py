from PyQt5 import QtCore, QtGui, QtWidgets


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("LoginWindow")
        MainWindow.resize(904, 637)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(904, 637))
        MainWindow.setMaximumSize(QtCore.QSize(904, 637))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(904, 637))
        self.centralwidget.setMaximumSize(QtCore.QSize(904, 637))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setAutoFillBackground(False)
        self.MainFrame.setStyleSheet(".QFrame{\n"
"background-color: rgb(203, 232, 238);\n"
"\n"
"}")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setMidLineWidth(2)
        self.MainFrame.setObjectName("MainFrame")
        self.FrameLogo = QtWidgets.QFrame(self.MainFrame)
        self.FrameLogo.setGeometry(QtCore.QRect(0, 44, 265, 55))
        self.FrameLogo.setStyleSheet("QFrame{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(185, 225, 233)\n"
"}")
        self.FrameLogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameLogo.setObjectName("FrameLogo")
        self.label_brightgoal = QtWidgets.QLabel(self.FrameLogo)
        self.label_brightgoal.setGeometry(QtCore.QRect(100, 10, 117, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_brightgoal.setFont(font)
        self.label_brightgoal.setStyleSheet("QLabel{\n"
"    color: rgb(0, 93, 112);\n"
"}")
        self.label_brightgoal.setObjectName("label_brightgoal")
        self.label_logo = QtWidgets.QLabel(self.FrameLogo)
        self.label_logo.setGeometry(QtCore.QRect(62, 12, 33, 33))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("Interface Assets/Brightgoal logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.label_heading_1 = QtWidgets.QLabel(self.MainFrame)
        self.label_heading_1.setGeometry(QtCore.QRect(68, 134, 397, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(17)
        self.label_heading_1.setFont(font)
        self.label_heading_1.setStyleSheet("QLabel{\n"
"    color: rgb(0, 93, 112);\n"
"}")
        self.label_heading_1.setObjectName("label_heading_1")
        self.label_instruction_1 = QtWidgets.QLabel(self.MainFrame)
        self.label_instruction_1.setGeometry(QtCore.QRect(70, 180, 397, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(11)
        self.label_instruction_1.setFont(font)
        self.label_instruction_1.setStyleSheet("QLabel{\n"
"    color: rgb(0, 93, 112);\n"
"}")
        self.label_instruction_1.setObjectName("label_instruction_1")
        self.label_instruction_2 = QtWidgets.QLabel(self.MainFrame)
        self.label_instruction_2.setGeometry(QtCore.QRect(68, 214, 397, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_instruction_2.setFont(font)
        self.label_instruction_2.setStyleSheet("QLabel{\n"
"    color: rgb(0, 93, 112);\n"
"}")
        self.label_instruction_2.setObjectName("label_instruction_2")
        self.label_instruction_3 = QtWidgets.QLabel(self.MainFrame)
        self.label_instruction_3.setGeometry(QtCore.QRect(66, 248, 397, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(11)
        self.label_instruction_3.setFont(font)
        self.label_instruction_3.setStyleSheet("QLabel{\n"
"    color: rgb(0, 93, 112);\n"
"}")
        self.label_instruction_3.setObjectName("label_instruction_3")
        self.FrameQrCode = QtWidgets.QFrame(self.MainFrame)
        self.FrameQrCode.setGeometry(QtCore.QRect(594, 120, 250, 250))
        self.FrameQrCode.setStyleSheet("QFrame{\n"
"    border-radius:125px;\n"
"    border: 2px solid rgb(1, 113, 135);\n"
"    background-color: rgb(103, 170, 183);\n"
"}")
        self.FrameQrCode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameQrCode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameQrCode.setObjectName("FrameQrCode")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.FrameQrCode)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_qr_code = QtWidgets.QLabel(self.FrameQrCode)
        self.label_qr_code.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    background-color: none;\n"
"    margin: 35px;\n"
"}")
        self.label_qr_code.setText("")
        self.label_qr_code.setPixmap(QtGui.QPixmap("Interface Assets/qr_code.png"))
        self.label_qr_code.setScaledContents(True)
        self.label_qr_code.setIndent(-1)
        self.label_qr_code.setObjectName("label_qr_code")
        self.horizontalLayout_2.addWidget(self.label_qr_code)
        self.label_instruction_4 = QtWidgets.QLabel(self.MainFrame)
        self.label_instruction_4.setGeometry(QtCore.QRect(64, 318, 173, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(10)
        self.label_instruction_4.setFont(font)
        self.label_instruction_4.setStyleSheet("QLabel{\n"
"    color: rgb(0, 93, 112);\n"
"}")
        self.label_instruction_4.setObjectName("label_instruction_4")
        self.label_heading_2 = QtWidgets.QLabel(self.MainFrame)
        self.label_heading_2.setGeometry(QtCore.QRect(62, 386, 173, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(10)
        self.label_heading_2.setFont(font)
        self.label_heading_2.setStyleSheet("QLabel{\n"
"    color: rgb(0, 93, 112);\n"
"}")
        self.label_heading_2.setObjectName("label_heading_2")
        self.label_privacy_policy = QtWidgets.QLabel(self.MainFrame)
        self.label_privacy_policy.setGeometry(QtCore.QRect(60, 420, 795, 137))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(10)
        self.label_privacy_policy.setFont(font)
        self.label_privacy_policy.setStyleSheet("QLabel{\n"
"    color: rgb(0, 93, 112);\n"
"}")
        self.label_privacy_policy.setWordWrap(True)
        self.label_privacy_policy.setObjectName("label_privacy_policy")
        self.accept_privacy_policy = QtWidgets.QCheckBox(self.MainFrame)
        self.accept_privacy_policy.setGeometry(QtCore.QRect(60, 566, 161, 17))
        self.accept_privacy_policy.setObjectName("accept_privacy_policy")
        self.horizontalLayout.addWidget(self.MainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Brightgoal"))
        self.label_brightgoal.setText(_translate("MainWindow", "Brightgoal"))
        self.label_heading_1.setText(_translate("MainWindow", "To use WhatsApp on your Computer"))
        self.label_instruction_1.setText(_translate("MainWindow", "1. Open WhatsApp on your phone"))
        self.label_instruction_2.setText(_translate("MainWindow", "2. Tap on \'Menu\' or \'Setting\' and Select \'Linked Devices\'"))
        self.label_instruction_3.setText(_translate("MainWindow", "3. Point your phone to this screen to caputer the code"))
        self.label_instruction_4.setText(_translate("MainWindow", "Need help to get started?"))
        self.label_heading_2.setText(_translate("MainWindow", "Privacy and Policy"))
        self.label_privacy_policy.setText(_translate("MainWindow", "This software is developed to automate Whatsapp and make your work easier, this pack provides lots of features to do things even faster than normal only for genuine use\n"
"if your using the application to perform unwanted activities we won’t be responsible for this.\n"
"whatever you are doing using this application ensure that it won’t cause you any problem, otherwise will be responsible for it on your own.\n"
"Thanks for using our Application, visit www.brightgoal.com for more information.\n"
"developed by Harvindar Singh"))
        self.accept_privacy_policy.setText(_translate("MainWindow", "Accept Privacy and Policy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = LoginWindow()

    MainWindow.show()
    sys.exit(app.exec_())
