# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(851, 1129)
        icon = QIcon()
        icon.addFile(u":/folder1/Icons/programmer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QFrame {\n"
"border: none;}\n"
"\n"
"/* QComboBox*/\n"
"QComboBox {\n"
"border-radius: 10px;\n"
"border: 1px solid #5e5c58;\n"
"background-color: rgba(255, 255, 255, 150);\n"
"color: rgb(0, 0, 0);\n"
"padding-left: 15px;}\n"
"\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"border-top-right-radius: 3px;;}\n"
"\n"
"QComboBox::down-arrow {    \n"
"image: url(:/folder1/Icons/downArrow.png);\n"
"width : 12px;}\n"
"\n"
"QComboBox::down-arrow:disabled {    \n"
"image: url(:/folder1/Icons/downArrowDis.png);}\n"
"\n"
"QComboBox::hover{\n"
"border: 2px solid  #5a83c6;}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"padding: 5px;}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.page_login.setStyleSheet(u"/* QLabel and QLineEdit*/\n"
"#lineEdit_password, #lineEdit_project_name {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}\n"
"\n"
"/* QPushButton*/\n"
"#button_login_next_page {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_login_next_page:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_login_next_page:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}")
        self.verticalLayout_18 = QVBoxLayout(self.page_login)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.page_login)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 70))
        self.frame_29.setMaximumSize(QSize(16777215, 70))
        self.frame_29.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_29.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.icon_interface_3 = QLabel(self.frame_29)
        self.icon_interface_3.setObjectName(u"icon_interface_3")
        self.icon_interface_3.setMinimumSize(QSize(50, 50))
        self.icon_interface_3.setMaximumSize(QSize(50, 50))
        self.icon_interface_3.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_3.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.icon_interface_3)

        self.interface_name_3 = QLabel(self.frame_29)
        self.interface_name_3.setObjectName(u"interface_name_3")
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(22)
        font.setBold(True)
        self.interface_name_3.setFont(font)
        self.interface_name_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.interface_name_3)


        self.verticalLayout_18.addWidget(self.frame_29)

        self.frame_22 = QFrame(self.page_login)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 16777215))
        self.frame_22.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_22.setLineWidth(0)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(465, 300))
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_23)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 75))
        self.frame_24.setMaximumSize(QSize(16777215, 75))
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_24)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.frame_24)
        self.label_14.setObjectName(u"label_14")
        font1 = QFont()
        font1.setPointSize(29)
        font1.setBold(True)
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_14)


        self.verticalLayout_15.addWidget(self.frame_24)

        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit_project_name = QLineEdit(self.frame_26)
        self.lineEdit_project_name.setObjectName(u"lineEdit_project_name")
        self.lineEdit_project_name.setMinimumSize(QSize(0, 20))
        self.lineEdit_project_name.setMaximumSize(QSize(250, 30))
        self.lineEdit_project_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lineEdit_project_name)


        self.verticalLayout_15.addWidget(self.frame_26)

        self.frame_30 = QFrame(self.frame_23)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_password = QLineEdit(self.frame_30)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(0, 20))
        self.lineEdit_password.setMaximumSize(QSize(250, 30))
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.lineEdit_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lineEdit_password)


        self.verticalLayout_15.addWidget(self.frame_30)

        self.frame_28 = QFrame(self.frame_23)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 60))
        self.frame_28.setMaximumSize(QSize(16777215, 60))
        self.frame_28.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.button_login_next_page = QPushButton(self.frame_28)
        self.button_login_next_page.setObjectName(u"button_login_next_page")
        self.button_login_next_page.setMinimumSize(QSize(100, 38))
        self.button_login_next_page.setMaximumSize(QSize(100, 38))
        self.button_login_next_page.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.button_login_next_page)


        self.verticalLayout_15.addWidget(self.frame_28)


        self.horizontalLayout_62.addWidget(self.frame_23)


        self.verticalLayout_18.addWidget(self.frame_22)

        self.frame_97 = QFrame(self.page_login)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMaximumSize(QSize(16777215, 20))
        self.frame_97.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_97)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_97)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_15)


        self.verticalLayout_18.addWidget(self.frame_97)

        self.pages.addWidget(self.page_login)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setStyleSheet(u"#label_abaqus, #label_result {\n"
"background-color: rgb(248, 248, 248);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}\n"
"\n"
"\n"
"/* QPushButton*/\n"
"#button_settings_next_page {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_abaqus, #button_result {\n"
"background-color: rgb(248, 248, 248);\n"
"border-radius: 17px;}\n"
"\n"
"#button_abaqus:hover, #button_result:hover, #button_settings_next_page:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_abaqus:pressed, #button_result:pressed, #button_settings_next_page:pressed {\n"
" background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.page_settings)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_settings)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 70))
        self.frame.setMaximumSize(QSize(16777215, 70))
        self.frame.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_interface = QLabel(self.frame)
        self.icon_interface.setObjectName(u"icon_interface")
        self.icon_interface.setMinimumSize(QSize(50, 50))
        self.icon_interface.setMaximumSize(QSize(50, 50))
        self.icon_interface.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon_interface)

        self.interface_name = QLabel(self.frame)
        self.interface_name.setObjectName(u"interface_name")
        self.interface_name.setFont(font)
        self.interface_name.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.interface_name)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(465, 300))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 100))
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_4.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_4)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_abaqus = QLabel(self.frame_8)
        self.label_abaqus.setObjectName(u"label_abaqus")
        self.label_abaqus.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_3.addWidget(self.label_abaqus)

        self.button_abaqus = QPushButton(self.frame_8)
        self.button_abaqus.setObjectName(u"button_abaqus")
        self.button_abaqus.setMinimumSize(QSize(34, 34))
        self.button_abaqus.setMaximumSize(QSize(34, 34))
        self.button_abaqus.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/folder1/Icons/import.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_abaqus.setIcon(icon1)
        self.button_abaqus.setIconSize(QSize(35, 35))

        self.horizontalLayout_3.addWidget(self.button_abaqus)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 100))
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_result = QLabel(self.frame_5)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setMaximumSize(QSize(16777215, 25))
        self.label_result.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_result)

        self.button_result = QPushButton(self.frame_5)
        self.button_result.setObjectName(u"button_result")
        self.button_result.setMinimumSize(QSize(34, 34))
        self.button_result.setMaximumSize(QSize(34, 34))
        self.button_result.setIcon(icon1)
        self.button_result.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.button_result)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_10)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 60))
        self.frame_11.setMaximumSize(QSize(16777215, 60))
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button_settings_next_page = QPushButton(self.frame_11)
        self.button_settings_next_page.setObjectName(u"button_settings_next_page")
        self.button_settings_next_page.setMinimumSize(QSize(100, 38))
        self.button_settings_next_page.setMaximumSize(QSize(100, 38))
        self.button_settings_next_page.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.button_settings_next_page)


        self.verticalLayout_7.addWidget(self.frame_11)


        self.horizontalLayout_63.addWidget(self.frame_4)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_settings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 20))
        self.frame_3.setMaximumSize(QSize(16777215, 20))
        self.frame_3.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.pages.addWidget(self.page_settings)
        self.page_conditions_limitation = QWidget()
        self.page_conditions_limitation.setObjectName(u"page_conditions_limitation")
        self.page_conditions_limitation.setStyleSheet(u"/* QPushButton*/\n"
"#button_conditions_limitation_next_page, #button_conditions_limitation_back {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_conditions_limitation_next_page:hover, #button_conditions_limitation_back:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_conditions_limitation_next_page:pressed, #button_conditions_limitation_back:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"")
        self.verticalLayout_23 = QVBoxLayout(self.page_conditions_limitation)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.page_conditions_limitation)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 70))
        self.frame_40.setMaximumSize(QSize(16777215, 70))
        self.frame_40.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_40.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.icon_interface_4 = QLabel(self.frame_40)
        self.icon_interface_4.setObjectName(u"icon_interface_4")
        self.icon_interface_4.setMinimumSize(QSize(50, 50))
        self.icon_interface_4.setMaximumSize(QSize(50, 50))
        self.icon_interface_4.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_4.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.icon_interface_4)

        self.interface_name_4 = QLabel(self.frame_40)
        self.interface_name_4.setObjectName(u"interface_name_4")
        self.interface_name_4.setFont(font)
        self.interface_name_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.interface_name_4)


        self.verticalLayout_23.addWidget(self.frame_40)

        self.frame_27 = QFrame(self.page_conditions_limitation)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_27.setLineWidth(0)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.frame_99 = QFrame(self.frame_27)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMaximumSize(QSize(465, 300))
        self.frame_99.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_99)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 16777215))
        self.frame_31.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_31)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 16777215))
        self.frame_33.setStyleSheet(u"")
        self.frame_33.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_17 = QLabel(self.frame_33)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 200))
        self.label_17.setTextFormat(Qt.TextFormat.AutoText)
        self.label_17.setScaledContents(False)
        self.label_17.setWordWrap(True)

        self.horizontalLayout_65.addWidget(self.label_17)


        self.verticalLayout_20.addWidget(self.frame_33)

        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 60))
        self.frame_32.setMaximumSize(QSize(16777215, 60))
        self.frame_32.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.button_conditions_limitation_back = QPushButton(self.frame_32)
        self.button_conditions_limitation_back.setObjectName(u"button_conditions_limitation_back")
        self.button_conditions_limitation_back.setMinimumSize(QSize(100, 38))
        self.button_conditions_limitation_back.setMaximumSize(QSize(100, 38))
        self.button_conditions_limitation_back.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.button_conditions_limitation_back)

        self.button_conditions_limitation_next_page = QPushButton(self.frame_32)
        self.button_conditions_limitation_next_page.setObjectName(u"button_conditions_limitation_next_page")
        self.button_conditions_limitation_next_page.setMinimumSize(QSize(100, 38))
        self.button_conditions_limitation_next_page.setMaximumSize(QSize(100, 38))
        self.button_conditions_limitation_next_page.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.button_conditions_limitation_next_page)


        self.verticalLayout_20.addWidget(self.frame_32)


        self.horizontalLayout_68.addWidget(self.frame_31)


        self.horizontalLayout_64.addWidget(self.frame_99)


        self.verticalLayout_23.addWidget(self.frame_27)

        self.frame_25 = QFrame(self.page_conditions_limitation)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 20))
        self.frame_25.setMaximumSize(QSize(16777215, 20))
        self.frame_25.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_25.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_25)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_25)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_16)


        self.verticalLayout_23.addWidget(self.frame_25)

        self.pages.addWidget(self.page_conditions_limitation)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QLineEdit {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}\n"
"\n"
"\n"
"#button_output_analysis_back, #button_output_analysis_next {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_output_analysis_back:hover, #button_output_analysis_next:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_output_analysis_back:pressed, #button_output_analysis_next:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"")
        self.verticalLayout_91 = QVBoxLayout(self.page_2)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.frame_153 = QFrame(self.page_2)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setMinimumSize(QSize(0, 70))
        self.frame_153.setMaximumSize(QSize(16777215, 70))
        self.frame_153.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_153.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_153.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_166 = QHBoxLayout(self.frame_153)
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.icon_interface_13 = QLabel(self.frame_153)
        self.icon_interface_13.setObjectName(u"icon_interface_13")
        self.icon_interface_13.setMinimumSize(QSize(50, 50))
        self.icon_interface_13.setMaximumSize(QSize(50, 50))
        self.icon_interface_13.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_13.setScaledContents(True)

        self.horizontalLayout_166.addWidget(self.icon_interface_13)

        self.interface_name_13 = QLabel(self.frame_153)
        self.interface_name_13.setObjectName(u"interface_name_13")
        self.interface_name_13.setFont(font)
        self.interface_name_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_166.addWidget(self.interface_name_13)


        self.verticalLayout_91.addWidget(self.frame_153)

        self.frame_83 = QFrame(self.page_2)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_83.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_83.setLineWidth(0)
        self.horizontalLayout_167 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.frame_155 = QFrame(self.frame_83)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setMaximumSize(QSize(465, 400))
        self.frame_155.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_168 = QHBoxLayout(self.frame_155)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.horizontalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_155)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMaximumSize(QSize(16777215, 16777215))
        self.frame_85.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_85.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_85)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.frame_158 = QFrame(self.frame_85)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setMaximumSize(QSize(16777215, 16777215))
        self.frame_158.setStyleSheet(u"")
        self.frame_158.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_158.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_158)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.frame_166 = QFrame(self.frame_158)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setMinimumSize(QSize(0, 250))
        self.frame_166.setMaximumSize(QSize(500, 16777215))
        self.frame_166.setStyleSheet(u"")
        self.frame_166.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_166.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_166)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.frame_87 = QFrame(self.frame_166)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(0, 0))
        self.frame_87.setMaximumSize(QSize(16777215, 50))
        self.frame_87.setStyleSheet(u"")
        self.frame_87.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_87.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_184 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.horizontalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.frame_163 = QFrame(self.frame_87)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_163.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_163.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_173 = QHBoxLayout(self.frame_163)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.chip = QRadioButton(self.frame_163)
        self.chip.setObjectName(u"chip")
        self.chip.setMinimumSize(QSize(85, 0))
        self.chip.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_173.addWidget(self.chip)


        self.horizontalLayout_184.addWidget(self.frame_163)

        self.frame_162 = QFrame(self.frame_87)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_162.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_162.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_172 = QHBoxLayout(self.frame_162)
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.temperature = QRadioButton(self.frame_162)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setMinimumSize(QSize(92, 0))
        self.temperature.setMaximumSize(QSize(92, 16777215))

        self.horizontalLayout_172.addWidget(self.temperature)


        self.horizontalLayout_184.addWidget(self.frame_162)

        self.frame_160 = QFrame(self.frame_87)
        self.frame_160.setObjectName(u"frame_160")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_160.sizePolicy().hasHeightForWidth())
        self.frame_160.setSizePolicy(sizePolicy)
        self.frame_160.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_160.setStyleSheet(u"")
        self.frame_160.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_160.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_169 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_169.setSpacing(0)
        self.horizontalLayout_169.setObjectName(u"horizontalLayout_169")
        self.horizontalLayout_169.setContentsMargins(0, 0, 0, 0)
        self.forces = QRadioButton(self.frame_160)
        self.forces.setObjectName(u"forces")
        self.forces.setMinimumSize(QSize(0, 0))
        self.forces.setMaximumSize(QSize(60, 16777215))
        self.forces.setChecked(False)

        self.horizontalLayout_169.addWidget(self.forces)


        self.horizontalLayout_184.addWidget(self.frame_160)


        self.verticalLayout_93.addWidget(self.frame_87)

        self.frame_167 = QFrame(self.frame_166)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setMinimumSize(QSize(0, 80))
        self.frame_167.setMaximumSize(QSize(16777215, 80))
        self.frame_167.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_167.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_167.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_175 = QHBoxLayout(self.frame_167)
        self.horizontalLayout_175.setSpacing(0)
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_175.setContentsMargins(5, 0, 5, 0)
        self.label_34 = QLabel(self.frame_167)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 16777215))
        self.label_34.setFont(font2)
        self.label_34.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_34.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_175.addWidget(self.label_34)


        self.verticalLayout_93.addWidget(self.frame_167)

        self.frame_168 = QFrame(self.frame_166)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setMinimumSize(QSize(450, 0))
        self.frame_168.setMaximumSize(QSize(450, 16777215))
        self.frame_168.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_168.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_168)
        self.verticalLayout_94.setSpacing(0)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.frame_169 = QFrame(self.frame_168)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_169.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_176 = QHBoxLayout(self.frame_169)
        self.horizontalLayout_176.setSpacing(0)
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.frame_170 = QFrame(self.frame_169)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_170.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_177 = QHBoxLayout(self.frame_170)
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.horizontalLayout_177.setContentsMargins(0, 0, -1, 0)
        self.label_35 = QLabel(self.frame_170)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(50, 0))
        self.label_35.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_177.addWidget(self.label_35)

        self.wfc = QLineEdit(self.frame_170)
        self.wfc.setObjectName(u"wfc")
        self.wfc.setEnabled(True)
        self.wfc.setMinimumSize(QSize(120, 0))
        self.wfc.setMaximumSize(QSize(120, 16777215))
        self.wfc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_177.addWidget(self.wfc)


        self.horizontalLayout_176.addWidget(self.frame_170)

        self.frame_172 = QFrame(self.frame_169)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_172.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_178 = QHBoxLayout(self.frame_172)
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.horizontalLayout_178.setContentsMargins(0, 0, -1, 0)
        self.label_36 = QLabel(self.frame_172)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(50, 0))
        self.label_36.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_178.addWidget(self.label_36)

        self.wfn = QLineEdit(self.frame_172)
        self.wfn.setObjectName(u"wfn")
        self.wfn.setEnabled(True)
        self.wfn.setMinimumSize(QSize(120, 0))
        self.wfn.setMaximumSize(QSize(120, 16777215))
        self.wfn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_178.addWidget(self.wfn)


        self.horizontalLayout_176.addWidget(self.frame_172)


        self.verticalLayout_94.addWidget(self.frame_169)

        self.frame_173 = QFrame(self.frame_168)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_173.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_179 = QHBoxLayout(self.frame_173)
        self.horizontalLayout_179.setSpacing(0)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.horizontalLayout_179.setContentsMargins(0, 0, 0, 0)
        self.frame_174 = QFrame(self.frame_173)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_174.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_180 = QHBoxLayout(self.frame_174)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(0, 0, -1, 0)
        self.label_37 = QLabel(self.frame_174)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(50, 0))
        self.label_37.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_180.addWidget(self.label_37)

        self.wcsr = QLineEdit(self.frame_174)
        self.wcsr.setObjectName(u"wcsr")
        self.wcsr.setEnabled(True)
        self.wcsr.setMinimumSize(QSize(120, 0))
        self.wcsr.setMaximumSize(QSize(120, 16777215))
        self.wcsr.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_180.addWidget(self.wcsr)


        self.horizontalLayout_179.addWidget(self.frame_174)

        self.frame_175 = QFrame(self.frame_173)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_175.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_181 = QHBoxLayout(self.frame_175)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(0, 0, -1, 0)
        self.label_91 = QLabel(self.frame_175)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(50, 0))
        self.label_91.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_181.addWidget(self.label_91)

        self.wccr = QLineEdit(self.frame_175)
        self.wccr.setObjectName(u"wccr")
        self.wccr.setEnabled(True)
        self.wccr.setMinimumSize(QSize(120, 0))
        self.wccr.setMaximumSize(QSize(120, 16777215))
        self.wccr.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_181.addWidget(self.wccr)


        self.horizontalLayout_179.addWidget(self.frame_175)


        self.verticalLayout_94.addWidget(self.frame_173)

        self.frame_176 = QFrame(self.frame_168)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setMaximumSize(QSize(225, 16777215))
        self.frame_176.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_176.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_182 = QHBoxLayout(self.frame_176)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(0, 0, -1, 0)
        self.label_92 = QLabel(self.frame_176)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMinimumSize(QSize(50, 0))
        self.label_92.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_182.addWidget(self.label_92)

        self.wt = QLineEdit(self.frame_176)
        self.wt.setObjectName(u"wt")
        self.wt.setEnabled(True)
        self.wt.setMinimumSize(QSize(120, 0))
        self.wt.setMaximumSize(QSize(120, 16777215))
        self.wt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_182.addWidget(self.wt)


        self.verticalLayout_94.addWidget(self.frame_176)


        self.verticalLayout_93.addWidget(self.frame_168)


        self.verticalLayout_92.addWidget(self.frame_166)


        self.verticalLayout_90.addWidget(self.frame_158)

        self.frame_159 = QFrame(self.frame_85)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setMinimumSize(QSize(0, 60))
        self.frame_159.setMaximumSize(QSize(16777215, 60))
        self.frame_159.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_159.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_170 = QHBoxLayout(self.frame_159)
        self.horizontalLayout_170.setObjectName(u"horizontalLayout_170")
        self.button_output_analysis_back = QPushButton(self.frame_159)
        self.button_output_analysis_back.setObjectName(u"button_output_analysis_back")
        self.button_output_analysis_back.setMinimumSize(QSize(100, 38))
        self.button_output_analysis_back.setMaximumSize(QSize(100, 38))
        self.button_output_analysis_back.setStyleSheet(u"")

        self.horizontalLayout_170.addWidget(self.button_output_analysis_back)

        self.button_output_analysis_next = QPushButton(self.frame_159)
        self.button_output_analysis_next.setObjectName(u"button_output_analysis_next")
        self.button_output_analysis_next.setMinimumSize(QSize(100, 38))
        self.button_output_analysis_next.setMaximumSize(QSize(100, 38))
        self.button_output_analysis_next.setStyleSheet(u"")

        self.horizontalLayout_170.addWidget(self.button_output_analysis_next)


        self.verticalLayout_90.addWidget(self.frame_159)


        self.horizontalLayout_168.addWidget(self.frame_85)


        self.horizontalLayout_167.addWidget(self.frame_155)


        self.verticalLayout_91.addWidget(self.frame_83)

        self.frame_154 = QFrame(self.page_2)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setMinimumSize(QSize(0, 20))
        self.frame_154.setMaximumSize(QSize(16777215, 20))
        self.frame_154.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_154.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_154.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_154)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_154)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_85.addWidget(self.label_33)


        self.verticalLayout_91.addWidget(self.frame_154)

        self.pages.addWidget(self.page_2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"QPushButton:pressed,  {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"")
        self.verticalLayout_75 = QVBoxLayout(self.page)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_93 = QFrame(self.page)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(0, 70))
        self.frame_93.setMaximumSize(QSize(16777215, 70))
        self.frame_93.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_93.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_93.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.icon_interface_10 = QLabel(self.frame_93)
        self.icon_interface_10.setObjectName(u"icon_interface_10")
        self.icon_interface_10.setMinimumSize(QSize(50, 50))
        self.icon_interface_10.setMaximumSize(QSize(50, 50))
        self.icon_interface_10.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_10.setScaledContents(True)

        self.horizontalLayout_112.addWidget(self.icon_interface_10)

        self.interface_name_10 = QLabel(self.frame_93)
        self.interface_name_10.setObjectName(u"interface_name_10")
        self.interface_name_10.setFont(font)
        self.interface_name_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_112.addWidget(self.interface_name_10)


        self.verticalLayout_75.addWidget(self.frame_93)

        self.frame_59 = QFrame(self.page)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_59.setLineWidth(0)
        self.horizontalLayout_108 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.frame_126 = QFrame(self.frame_59)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setMaximumSize(QSize(465, 400))
        self.frame_126.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.frame_126)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMaximumSize(QSize(16777215, 16777215))
        self.frame_84.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_84.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_84)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.frame_89 = QFrame(self.frame_84)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMaximumSize(QSize(16777215, 16777215))
        self.frame_89.setStyleSheet(u"")
        self.frame_89.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_89.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.label_31 = QLabel(self.frame_89)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 300))
        self.label_31.setTextFormat(Qt.TextFormat.AutoText)
        self.label_31.setScaledContents(False)
        self.label_31.setWordWrap(True)

        self.horizontalLayout_110.addWidget(self.label_31)


        self.verticalLayout_68.addWidget(self.frame_89)

        self.frame_92 = QFrame(self.frame_84)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(0, 60))
        self.frame_92.setMaximumSize(QSize(16777215, 60))
        self.frame_92.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_92.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.button_import_inp = QPushButton(self.frame_92)
        self.button_import_inp.setObjectName(u"button_import_inp")
        self.button_import_inp.setMinimumSize(QSize(100, 38))
        self.button_import_inp.setMaximumSize(QSize(100, 38))
        self.button_import_inp.setStyleSheet(u"")

        self.horizontalLayout_111.addWidget(self.button_import_inp)

        self.button_create_geometry = QPushButton(self.frame_92)
        self.button_create_geometry.setObjectName(u"button_create_geometry")
        self.button_create_geometry.setMinimumSize(QSize(100, 38))
        self.button_create_geometry.setMaximumSize(QSize(100, 38))
        self.button_create_geometry.setStyleSheet(u"")

        self.horizontalLayout_111.addWidget(self.button_create_geometry)


        self.verticalLayout_68.addWidget(self.frame_92)


        self.horizontalLayout_109.addWidget(self.frame_84)


        self.horizontalLayout_108.addWidget(self.frame_126)


        self.verticalLayout_75.addWidget(self.frame_59)

        self.frame_94 = QFrame(self.page)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(0, 20))
        self.frame_94.setMaximumSize(QSize(16777215, 20))
        self.frame_94.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_94.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_94.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_94)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_94)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_70.addWidget(self.label_32)


        self.verticalLayout_75.addWidget(self.frame_94)

        self.pages.addWidget(self.page)
        self.geometryPage = QWidget()
        self.geometryPage.setObjectName(u"geometryPage")
        self.geometryPage.setStyleSheet(u"#frame_127, #frame_262 {\n"
"    background-color: #b6b6b6;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#frame_262 {\n"
"    border-radius: 15px; \n"
"	border: 3px solid #3498db;\n"
"}")
        self.verticalLayout_89 = QVBoxLayout(self.geometryPage)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_171 = QFrame(self.geometryPage)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setMinimumSize(QSize(0, 70))
        self.frame_171.setMaximumSize(QSize(16777215, 70))
        self.frame_171.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_171.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_171.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_126 = QHBoxLayout(self.frame_171)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.icon_interface_12 = QLabel(self.frame_171)
        self.icon_interface_12.setObjectName(u"icon_interface_12")
        self.icon_interface_12.setMinimumSize(QSize(50, 50))
        self.icon_interface_12.setMaximumSize(QSize(50, 50))
        self.icon_interface_12.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_12.setScaledContents(True)

        self.horizontalLayout_126.addWidget(self.icon_interface_12)

        self.interface_name_12 = QLabel(self.frame_171)
        self.interface_name_12.setObjectName(u"interface_name_12")
        self.interface_name_12.setFont(font)
        self.interface_name_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_126.addWidget(self.interface_name_12)


        self.verticalLayout_89.addWidget(self.frame_171)

        self.frame_95 = QFrame(self.geometryPage)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_95.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_95.setLineWidth(0)
        self.horizontalLayout_113 = QHBoxLayout(self.frame_95)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.frame_96 = QFrame(self.frame_95)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMaximumSize(QSize(800, 16777215))
        self.frame_96.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_96)
        self.verticalLayout_77.setSpacing(10)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.frame_127 = QFrame(self.frame_96)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setStyleSheet(u"")
        self.frame_127.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_127)
        self.verticalLayout_84.setSpacing(5)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(9, 9, 9, 9)
        self.tabWidget = QTabWidget(self.frame_127)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setStyleSheet(u"QWidget{\n"
"	background-color: #b6b6b6;}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #b6b6b6;\n"
"	border-radius: 5px;\n"
"    background-color: #b6b6b6;}\n"
"\n"
"QTabBar::tab {\n"
"	border-radius: 5px;\n"
"    background: #e1e1e1;\n"
"    border: 1px solid #b6b6b6;\n"
"    padding: 5px;\n"
"    color: black;\n"
"	width: 120;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #567cbe;  /* Cor de fundo da aba selecionada */\n"
"    color: white;  /* Cor do texto da aba selecionada */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #73a6ff;  /* Cor de fundo da aba ao passar o mouse */\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.eulerianTab = QWidget()
        self.eulerianTab.setObjectName(u"eulerianTab")
        self.verticalLayout_151 = QVBoxLayout(self.eulerianTab)
        self.verticalLayout_151.setSpacing(0)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.verticalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.frame_203 = QFrame(self.eulerianTab)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QFrame {\n"
"        background-color: rgb(182, 182, 182);\n"
"        border-radius: 15px; \n"
"    }")
        self.frame_203.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_203)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(-1, 9, -1, -1)
        self.frame_207 = QFrame(self.frame_203)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setMinimumSize(QSize(0, 250))
        self.frame_207.setMaximumSize(QSize(16777215, 250))
        self.frame_207.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.frame_207)
        self.horizontalLayout_114.setSpacing(0)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.frame_208 = QFrame(self.frame_207)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.frame_208)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(-1, 0, -1, -1)
        self.frame_209 = QFrame(self.frame_208)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setMinimumSize(QSize(0, 35))
        self.frame_209.setMaximumSize(QSize(16777215, 35))
        self.frame_209.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.frame_209)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_209)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(0, 35))
        self.label_53.setMaximumSize(QSize(16777215, 35))
        self.label_53.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_133.addWidget(self.label_53)


        self.verticalLayout_132.addWidget(self.frame_209)

        self.frame_210 = QFrame(self.frame_208)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_115 = QHBoxLayout(self.frame_210)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(20, -1, -1, -1)
        self.frame_211 = QFrame(self.frame_210)
        self.frame_211.setObjectName(u"frame_211")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_211.sizePolicy().hasHeightForWidth())
        self.frame_211.setSizePolicy(sizePolicy1)
        self.frame_211.setMaximumSize(QSize(120, 16777215))
        self.frame_211.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.frame_211)
        self.verticalLayout_134.setSpacing(7)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.label_143 = QLabel(self.frame_211)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(0, 18))
        self.label_143.setMaximumSize(QSize(16777215, 18))
        font3 = QFont()
        font3.setFamilies([u"Yu Gothic UI Semilight"])
        self.label_143.setFont(font3)
        self.label_143.setStyleSheet(u"")

        self.verticalLayout_134.addWidget(self.label_143)

        self.label_145 = QLabel(self.frame_211)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(0, 18))
        self.label_145.setMaximumSize(QSize(16777215, 18))
        self.label_145.setFont(font3)
        self.label_145.setStyleSheet(u"")

        self.verticalLayout_134.addWidget(self.label_145)

        self.label_153 = QLabel(self.frame_211)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMinimumSize(QSize(0, 18))
        self.label_153.setMaximumSize(QSize(16777215, 18))
        self.label_153.setFont(font3)
        self.label_153.setStyleSheet(u"")

        self.verticalLayout_134.addWidget(self.label_153)

        self.label_154 = QLabel(self.frame_211)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setMinimumSize(QSize(0, 18))
        self.label_154.setMaximumSize(QSize(16777215, 18))
        self.label_154.setFont(font3)
        self.label_154.setStyleSheet(u"")

        self.verticalLayout_134.addWidget(self.label_154)


        self.horizontalLayout_115.addWidget(self.frame_211)

        self.frame_212 = QFrame(self.frame_210)
        self.frame_212.setObjectName(u"frame_212")
        sizePolicy1.setHeightForWidth(self.frame_212.sizePolicy().hasHeightForWidth())
        self.frame_212.setSizePolicy(sizePolicy1)
        self.frame_212.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_212.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_212)
        self.verticalLayout_135.setSpacing(7)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.eulerianName = QLineEdit(self.frame_212)
        self.eulerianName.setObjectName(u"eulerianName")
        self.eulerianName.setEnabled(False)
        self.eulerianName.setMinimumSize(QSize(0, 20))
        self.eulerianName.setMaximumSize(QSize(180, 16777215))
        self.eulerianName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_135.addWidget(self.eulerianName)

        self.eulerianHeight = QLineEdit(self.frame_212)
        self.eulerianHeight.setObjectName(u"eulerianHeight")
        self.eulerianHeight.setMinimumSize(QSize(0, 20))
        self.eulerianHeight.setMaximumSize(QSize(180, 16777215))
        self.eulerianHeight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_135.addWidget(self.eulerianHeight)

        self.eulerianWidth = QLineEdit(self.frame_212)
        self.eulerianWidth.setObjectName(u"eulerianWidth")
        self.eulerianWidth.setMinimumSize(QSize(0, 20))
        self.eulerianWidth.setMaximumSize(QSize(180, 16777215))
        self.eulerianWidth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_135.addWidget(self.eulerianWidth)

        self.eulerianTrickness = QLineEdit(self.frame_212)
        self.eulerianTrickness.setObjectName(u"eulerianTrickness")
        self.eulerianTrickness.setMinimumSize(QSize(0, 20))
        self.eulerianTrickness.setMaximumSize(QSize(180, 16777215))
        self.eulerianTrickness.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_135.addWidget(self.eulerianTrickness)


        self.horizontalLayout_115.addWidget(self.frame_212)


        self.verticalLayout_132.addWidget(self.frame_210)


        self.horizontalLayout_114.addWidget(self.frame_208)

        self.frame_213 = QFrame(self.frame_207)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_213)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(-1, 0, -1, -1)
        self.frame_214 = QFrame(self.frame_213)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setMinimumSize(QSize(0, 35))
        self.frame_214.setMaximumSize(QSize(16777215, 35))
        self.frame_214.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.frame_214)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_214)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(0, 35))
        self.label_55.setMaximumSize(QSize(16777215, 35))
        self.label_55.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_137.addWidget(self.label_55)


        self.verticalLayout_136.addWidget(self.frame_214)

        self.frame_215 = QFrame(self.frame_213)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_116 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_116.setSpacing(20)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setContentsMargins(20, -1, -1, -1)
        self.frame_216 = QFrame(self.frame_215)
        self.frame_216.setObjectName(u"frame_216")
        self.frame_216.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_216.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_117 = QHBoxLayout(self.frame_216)
        self.horizontalLayout_117.setSpacing(6)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.frame_217 = QFrame(self.frame_216)
        self.frame_217.setObjectName(u"frame_217")
        sizePolicy1.setHeightForWidth(self.frame_217.sizePolicy().hasHeightForWidth())
        self.frame_217.setSizePolicy(sizePolicy1)
        self.frame_217.setMaximumSize(QSize(40, 16777215))
        self.frame_217.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_217.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.frame_217)
        self.verticalLayout_138.setSpacing(7)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.verticalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.label_157 = QLabel(self.frame_217)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setMinimumSize(QSize(0, 18))
        self.label_157.setMaximumSize(QSize(16777215, 18))
        self.label_157.setFont(font3)
        self.label_157.setStyleSheet(u"")

        self.verticalLayout_138.addWidget(self.label_157)

        self.label_158 = QLabel(self.frame_217)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setMinimumSize(QSize(0, 18))
        self.label_158.setMaximumSize(QSize(16777215, 18))
        self.label_158.setFont(font3)
        self.label_158.setStyleSheet(u"")

        self.verticalLayout_138.addWidget(self.label_158)

        self.label_169 = QLabel(self.frame_217)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setMinimumSize(QSize(0, 18))
        self.label_169.setMaximumSize(QSize(16777215, 18))
        self.label_169.setFont(font3)
        self.label_169.setStyleSheet(u"")

        self.verticalLayout_138.addWidget(self.label_169)

        self.label_170 = QLabel(self.frame_217)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setMinimumSize(QSize(0, 18))
        self.label_170.setMaximumSize(QSize(16777215, 18))
        self.label_170.setFont(font3)
        self.label_170.setStyleSheet(u"")

        self.verticalLayout_138.addWidget(self.label_170)


        self.horizontalLayout_117.addWidget(self.frame_217)

        self.frame_218 = QFrame(self.frame_216)
        self.frame_218.setObjectName(u"frame_218")
        sizePolicy1.setHeightForWidth(self.frame_218.sizePolicy().hasHeightForWidth())
        self.frame_218.setSizePolicy(sizePolicy1)
        self.frame_218.setMaximumSize(QSize(120, 16777215))
        self.frame_218.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_218.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_218)
        self.verticalLayout_139.setSpacing(7)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.eulerianPartitionX1 = QLineEdit(self.frame_218)
        self.eulerianPartitionX1.setObjectName(u"eulerianPartitionX1")
        self.eulerianPartitionX1.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionX1.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_139.addWidget(self.eulerianPartitionX1)

        self.eulerianPartitionX2 = QLineEdit(self.frame_218)
        self.eulerianPartitionX2.setObjectName(u"eulerianPartitionX2")
        self.eulerianPartitionX2.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionX2.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_139.addWidget(self.eulerianPartitionX2)

        self.eulerianPartitionX3 = QLineEdit(self.frame_218)
        self.eulerianPartitionX3.setObjectName(u"eulerianPartitionX3")
        self.eulerianPartitionX3.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionX3.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_139.addWidget(self.eulerianPartitionX3)

        self.eulerianPartitionX4 = QLineEdit(self.frame_218)
        self.eulerianPartitionX4.setObjectName(u"eulerianPartitionX4")
        self.eulerianPartitionX4.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionX4.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionX4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_139.addWidget(self.eulerianPartitionX4)


        self.horizontalLayout_117.addWidget(self.frame_218)


        self.horizontalLayout_116.addWidget(self.frame_216)

        self.frame_219 = QFrame(self.frame_215)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_118 = QHBoxLayout(self.frame_219)
        self.horizontalLayout_118.setSpacing(6)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(0, 0, 0, 0)
        self.frame_220 = QFrame(self.frame_219)
        self.frame_220.setObjectName(u"frame_220")
        sizePolicy1.setHeightForWidth(self.frame_220.sizePolicy().hasHeightForWidth())
        self.frame_220.setSizePolicy(sizePolicy1)
        self.frame_220.setMaximumSize(QSize(40, 16777215))
        self.frame_220.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_220)
        self.verticalLayout_140.setSpacing(7)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.label_171 = QLabel(self.frame_220)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setMinimumSize(QSize(0, 18))
        self.label_171.setMaximumSize(QSize(16777215, 18))
        self.label_171.setFont(font3)
        self.label_171.setStyleSheet(u"")

        self.verticalLayout_140.addWidget(self.label_171)

        self.label_177 = QLabel(self.frame_220)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setMinimumSize(QSize(0, 18))
        self.label_177.setMaximumSize(QSize(16777215, 18))
        self.label_177.setFont(font3)
        self.label_177.setStyleSheet(u"")

        self.verticalLayout_140.addWidget(self.label_177)

        self.label_178 = QLabel(self.frame_220)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setMinimumSize(QSize(0, 18))
        self.label_178.setMaximumSize(QSize(16777215, 18))
        self.label_178.setFont(font3)
        self.label_178.setStyleSheet(u"")

        self.verticalLayout_140.addWidget(self.label_178)

        self.label_181 = QLabel(self.frame_220)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setMinimumSize(QSize(0, 18))
        self.label_181.setMaximumSize(QSize(16777215, 18))
        self.label_181.setFont(font3)
        self.label_181.setStyleSheet(u"")

        self.verticalLayout_140.addWidget(self.label_181)


        self.horizontalLayout_118.addWidget(self.frame_220)

        self.frame_221 = QFrame(self.frame_219)
        self.frame_221.setObjectName(u"frame_221")
        sizePolicy1.setHeightForWidth(self.frame_221.sizePolicy().hasHeightForWidth())
        self.frame_221.setSizePolicy(sizePolicy1)
        self.frame_221.setMaximumSize(QSize(120, 16777215))
        self.frame_221.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_221.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.frame_221)
        self.verticalLayout_141.setSpacing(7)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.eulerianPartitionY1 = QLineEdit(self.frame_221)
        self.eulerianPartitionY1.setObjectName(u"eulerianPartitionY1")
        self.eulerianPartitionY1.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionY1.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_141.addWidget(self.eulerianPartitionY1)

        self.eulerianPartitionY2 = QLineEdit(self.frame_221)
        self.eulerianPartitionY2.setObjectName(u"eulerianPartitionY2")
        self.eulerianPartitionY2.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionY2.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_141.addWidget(self.eulerianPartitionY2)

        self.eulerianPartitionY3 = QLineEdit(self.frame_221)
        self.eulerianPartitionY3.setObjectName(u"eulerianPartitionY3")
        self.eulerianPartitionY3.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionY3.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_141.addWidget(self.eulerianPartitionY3)

        self.eulerianPartitionY4 = QLineEdit(self.frame_221)
        self.eulerianPartitionY4.setObjectName(u"eulerianPartitionY4")
        self.eulerianPartitionY4.setMinimumSize(QSize(0, 20))
        self.eulerianPartitionY4.setMaximumSize(QSize(16777215, 16777215))
        self.eulerianPartitionY4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_141.addWidget(self.eulerianPartitionY4)


        self.horizontalLayout_118.addWidget(self.frame_221)


        self.horizontalLayout_116.addWidget(self.frame_219)


        self.verticalLayout_136.addWidget(self.frame_215)


        self.horizontalLayout_114.addWidget(self.frame_213)


        self.verticalLayout_131.addWidget(self.frame_207)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_131.addItem(self.verticalSpacer_17)

        self.frame_222 = QFrame(self.frame_203)
        self.frame_222.setObjectName(u"frame_222")
        self.frame_222.setMinimumSize(QSize(0, 250))
        self.frame_222.setMaximumSize(QSize(16777215, 250))
        self.frame_222.setStyleSheet(u"")
        self.frame_222.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_222.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.frame_222)
        self.verticalLayout_142.setSpacing(0)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(9, 0, 0, 0)
        self.frame_223 = QFrame(self.frame_222)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_223.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_223)
        self.verticalLayout_143.setSpacing(0)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(0, 0, 0, -1)
        self.frame_224 = QFrame(self.frame_223)
        self.frame_224.setObjectName(u"frame_224")
        self.frame_224.setMinimumSize(QSize(0, 35))
        self.frame_224.setMaximumSize(QSize(16777215, 35))
        self.frame_224.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_224.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_224)
        self.verticalLayout_144.setSpacing(0)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.verticalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.frame_224)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(0, 35))
        self.label_59.setMaximumSize(QSize(16777215, 35))
        self.label_59.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_59.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_144.addWidget(self.label_59)


        self.verticalLayout_143.addWidget(self.frame_224)

        self.frame_225 = QFrame(self.frame_223)
        self.frame_225.setObjectName(u"frame_225")
        self.frame_225.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_225.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_119 = QHBoxLayout(self.frame_225)
        self.horizontalLayout_119.setSpacing(0)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.frame_226 = QFrame(self.frame_225)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_226.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_145 = QVBoxLayout(self.frame_226)
        self.verticalLayout_145.setSpacing(0)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.verticalLayout_145.setContentsMargins(0, -1, 12, -1)
        self.frame_227 = QFrame(self.frame_226)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_120 = QHBoxLayout(self.frame_227)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setContentsMargins(20, -1, 0, -1)
        self.frame_228 = QFrame(self.frame_227)
        self.frame_228.setObjectName(u"frame_228")
        sizePolicy1.setHeightForWidth(self.frame_228.sizePolicy().hasHeightForWidth())
        self.frame_228.setSizePolicy(sizePolicy1)
        self.frame_228.setMaximumSize(QSize(120, 16777215))
        self.frame_228.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_146 = QVBoxLayout(self.frame_228)
        self.verticalLayout_146.setSpacing(7)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.verticalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.label_117 = QLabel(self.frame_228)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(0, 18))
        self.label_117.setMaximumSize(QSize(16777215, 18))
        self.label_117.setFont(font3)
        self.label_117.setStyleSheet(u"")

        self.verticalLayout_146.addWidget(self.label_117)

        self.label_118 = QLabel(self.frame_228)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(0, 18))
        self.label_118.setMaximumSize(QSize(16777215, 18))
        self.label_118.setFont(font3)
        self.label_118.setStyleSheet(u"")

        self.verticalLayout_146.addWidget(self.label_118)

        self.label_119 = QLabel(self.frame_228)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(0, 18))
        self.label_119.setMaximumSize(QSize(16777215, 18))
        self.label_119.setFont(font3)
        self.label_119.setStyleSheet(u"")

        self.verticalLayout_146.addWidget(self.label_119)

        self.label_120 = QLabel(self.frame_228)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(0, 18))
        self.label_120.setMaximumSize(QSize(16777215, 18))
        self.label_120.setFont(font3)
        self.label_120.setStyleSheet(u"")

        self.verticalLayout_146.addWidget(self.label_120)


        self.horizontalLayout_120.addWidget(self.frame_228)

        self.frame_229 = QFrame(self.frame_227)
        self.frame_229.setObjectName(u"frame_229")
        sizePolicy1.setHeightForWidth(self.frame_229.sizePolicy().hasHeightForWidth())
        self.frame_229.setSizePolicy(sizePolicy1)
        self.frame_229.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_229.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_229.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.frame_229)
        self.verticalLayout_147.setSpacing(7)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.verticalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.eulerianGlobalSize = QLineEdit(self.frame_229)
        self.eulerianGlobalSize.setObjectName(u"eulerianGlobalSize")
        self.eulerianGlobalSize.setMinimumSize(QSize(0, 20))
        self.eulerianGlobalSize.setMaximumSize(QSize(180, 16777215))
        self.eulerianGlobalSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_147.addWidget(self.eulerianGlobalSize)

        self.eulerianDeviationFactor = QLineEdit(self.frame_229)
        self.eulerianDeviationFactor.setObjectName(u"eulerianDeviationFactor")
        self.eulerianDeviationFactor.setMinimumSize(QSize(0, 20))
        self.eulerianDeviationFactor.setMaximumSize(QSize(180, 16777215))
        self.eulerianDeviationFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_147.addWidget(self.eulerianDeviationFactor)

        self.eulerianMininumFactor = QLineEdit(self.frame_229)
        self.eulerianMininumFactor.setObjectName(u"eulerianMininumFactor")
        self.eulerianMininumFactor.setMinimumSize(QSize(0, 20))
        self.eulerianMininumFactor.setMaximumSize(QSize(180, 16777215))
        self.eulerianMininumFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_147.addWidget(self.eulerianMininumFactor)

        self.eulerianOtherInfo = QLineEdit(self.frame_229)
        self.eulerianOtherInfo.setObjectName(u"eulerianOtherInfo")
        self.eulerianOtherInfo.setMinimumSize(QSize(0, 20))
        self.eulerianOtherInfo.setMaximumSize(QSize(180, 16777215))
        self.eulerianOtherInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_147.addWidget(self.eulerianOtherInfo)


        self.horizontalLayout_120.addWidget(self.frame_229)


        self.verticalLayout_145.addWidget(self.frame_227)


        self.horizontalLayout_119.addWidget(self.frame_226)

        self.frame_230 = QFrame(self.frame_225)
        self.frame_230.setObjectName(u"frame_230")
        self.frame_230.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_230.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.frame_230)
        self.verticalLayout_148.setSpacing(0)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.frame_231 = QFrame(self.frame_230)
        self.frame_231.setObjectName(u"frame_231")
        self.frame_231.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_231.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_121 = QHBoxLayout(self.frame_231)
        self.horizontalLayout_121.setSpacing(20)
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(15, -1, -1, -1)
        self.frame_232 = QFrame(self.frame_231)
        self.frame_232.setObjectName(u"frame_232")
        self.frame_232.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_232.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_122 = QHBoxLayout(self.frame_232)
        self.horizontalLayout_122.setSpacing(6)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.horizontalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.frame_233 = QFrame(self.frame_232)
        self.frame_233.setObjectName(u"frame_233")
        sizePolicy1.setHeightForWidth(self.frame_233.sizePolicy().hasHeightForWidth())
        self.frame_233.setSizePolicy(sizePolicy1)
        self.frame_233.setMaximumSize(QSize(120, 16777215))
        self.frame_233.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_233.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.frame_233)
        self.verticalLayout_149.setSpacing(7)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.verticalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.label_182 = QLabel(self.frame_233)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setMinimumSize(QSize(0, 18))
        self.label_182.setMaximumSize(QSize(16777215, 18))
        self.label_182.setFont(font3)
        self.label_182.setStyleSheet(u"")

        self.verticalLayout_149.addWidget(self.label_182)

        self.label_183 = QLabel(self.frame_233)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setMinimumSize(QSize(0, 18))
        self.label_183.setMaximumSize(QSize(16777215, 18))
        self.label_183.setFont(font3)
        self.label_183.setStyleSheet(u"")

        self.verticalLayout_149.addWidget(self.label_183)

        self.label_184 = QLabel(self.frame_233)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setMinimumSize(QSize(0, 18))
        self.label_184.setMaximumSize(QSize(16777215, 18))
        self.label_184.setFont(font3)
        self.label_184.setStyleSheet(u"")

        self.verticalLayout_149.addWidget(self.label_184)

        self.label_185 = QLabel(self.frame_233)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setMinimumSize(QSize(0, 18))
        self.label_185.setMaximumSize(QSize(16777215, 18))
        self.label_185.setFont(font3)
        self.label_185.setStyleSheet(u"")

        self.verticalLayout_149.addWidget(self.label_185)


        self.horizontalLayout_122.addWidget(self.frame_233)

        self.frame_234 = QFrame(self.frame_232)
        self.frame_234.setObjectName(u"frame_234")
        sizePolicy1.setHeightForWidth(self.frame_234.sizePolicy().hasHeightForWidth())
        self.frame_234.setSizePolicy(sizePolicy1)
        self.frame_234.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_234.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_234.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.frame_234)
        self.verticalLayout_150.setSpacing(7)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.eulerianOtherInfo_7 = QLineEdit(self.frame_234)
        self.eulerianOtherInfo_7.setObjectName(u"eulerianOtherInfo_7")
        self.eulerianOtherInfo_7.setMinimumSize(QSize(0, 20))
        self.eulerianOtherInfo_7.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_150.addWidget(self.eulerianOtherInfo_7)

        self.eulerianOtherInfo_8 = QLineEdit(self.frame_234)
        self.eulerianOtherInfo_8.setObjectName(u"eulerianOtherInfo_8")
        self.eulerianOtherInfo_8.setMinimumSize(QSize(0, 20))
        self.eulerianOtherInfo_8.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_150.addWidget(self.eulerianOtherInfo_8)

        self.eulerianOtherInfo_9 = QLineEdit(self.frame_234)
        self.eulerianOtherInfo_9.setObjectName(u"eulerianOtherInfo_9")
        self.eulerianOtherInfo_9.setMinimumSize(QSize(0, 20))
        self.eulerianOtherInfo_9.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_150.addWidget(self.eulerianOtherInfo_9)

        self.eulerianOtherInfo_10 = QLineEdit(self.frame_234)
        self.eulerianOtherInfo_10.setObjectName(u"eulerianOtherInfo_10")
        self.eulerianOtherInfo_10.setMinimumSize(QSize(0, 20))
        self.eulerianOtherInfo_10.setMaximumSize(QSize(189, 16777215))
        self.eulerianOtherInfo_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_150.addWidget(self.eulerianOtherInfo_10)


        self.horizontalLayout_122.addWidget(self.frame_234)


        self.horizontalLayout_121.addWidget(self.frame_232)


        self.verticalLayout_148.addWidget(self.frame_231)


        self.horizontalLayout_119.addWidget(self.frame_230)


        self.verticalLayout_143.addWidget(self.frame_225)


        self.verticalLayout_142.addWidget(self.frame_223)


        self.verticalLayout_131.addWidget(self.frame_222)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_131.addItem(self.verticalSpacer_18)

        self.eulerianWarning = QLabel(self.frame_203)
        self.eulerianWarning.setObjectName(u"eulerianWarning")
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic UI Semilight"])
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.eulerianWarning.setFont(font4)
        self.eulerianWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.eulerianWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.eulerianWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_131.addWidget(self.eulerianWarning)

        self.verticalSpacer_19 = QSpacerItem(20, 23, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_131.addItem(self.verticalSpacer_19)

        self.frame_98 = QFrame(self.frame_203)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_98)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.defautValues = QCheckBox(self.frame_98)
        self.defautValues.setObjectName(u"defautValues")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.defautValues.sizePolicy().hasHeightForWidth())
        self.defautValues.setSizePolicy(sizePolicy2)
        self.defautValues.setMaximumSize(QSize(16777215, 20))
        self.defautValues.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_76.addWidget(self.defautValues)


        self.verticalLayout_131.addWidget(self.frame_98)


        self.verticalLayout_151.addWidget(self.frame_203)

        self.tabWidget.addTab(self.eulerianTab, "")
        self.chipPlayeTab = QWidget()
        self.chipPlayeTab.setObjectName(u"chipPlayeTab")
        self.chipPlayeTab.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_223 = QVBoxLayout(self.chipPlayeTab)
        self.verticalLayout_223.setObjectName(u"verticalLayout_223")
        self.verticalLayout_223.setContentsMargins(0, 0, 0, 0)
        self.frame_332 = QFrame(self.chipPlayeTab)
        self.frame_332.setObjectName(u"frame_332")
        sizePolicy.setHeightForWidth(self.frame_332.sizePolicy().hasHeightForWidth())
        self.frame_332.setSizePolicy(sizePolicy)
        self.frame_332.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QFrame {\n"
"        background-color: rgb(182, 182, 182);\n"
"        border-radius: 15px; \n"
"    }")
        self.frame_332.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_332.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_216 = QVBoxLayout(self.frame_332)
        self.verticalLayout_216.setObjectName(u"verticalLayout_216")
        self.verticalLayout_216.setContentsMargins(9, 9, 0, 0)
        self.frame_333 = QFrame(self.frame_332)
        self.frame_333.setObjectName(u"frame_333")
        sizePolicy.setHeightForWidth(self.frame_333.sizePolicy().hasHeightForWidth())
        self.frame_333.setSizePolicy(sizePolicy)
        self.frame_333.setMinimumSize(QSize(311, 250))
        self.frame_333.setMaximumSize(QSize(16777215, 280))
        self.frame_333.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_333.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_217 = QVBoxLayout(self.frame_333)
        self.verticalLayout_217.setSpacing(0)
        self.verticalLayout_217.setObjectName(u"verticalLayout_217")
        self.verticalLayout_217.setContentsMargins(-1, 0, -1, -1)
        self.frame_334 = QFrame(self.frame_333)
        self.frame_334.setObjectName(u"frame_334")
        self.frame_334.setMinimumSize(QSize(0, 35))
        self.frame_334.setMaximumSize(QSize(16777215, 35))
        self.frame_334.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_334.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.frame_334)
        self.horizontalLayout_134.setSpacing(0)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.frame_334)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(0, 35))
        self.label_63.setMaximumSize(QSize(16777215, 35))
        self.label_63.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_134.addWidget(self.label_63)


        self.verticalLayout_217.addWidget(self.frame_334)

        self.frame_335 = QFrame(self.frame_333)
        self.frame_335.setObjectName(u"frame_335")
        self.frame_335.setMinimumSize(QSize(283, 180))
        self.frame_335.setMaximumSize(QSize(16777215, 16777215))
        self.frame_335.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.frame_335.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_335.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_135 = QHBoxLayout(self.frame_335)
        self.horizontalLayout_135.setSpacing(6)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.horizontalLayout_135.setContentsMargins(20, 9, -1, 9)
        self.frame_336 = QFrame(self.frame_335)
        self.frame_336.setObjectName(u"frame_336")
        sizePolicy.setHeightForWidth(self.frame_336.sizePolicy().hasHeightForWidth())
        self.frame_336.setSizePolicy(sizePolicy)
        self.frame_336.setMinimumSize(QSize(120, 0))
        self.frame_336.setStyleSheet(u"border: 0px;")
        self.frame_336.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_336.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_218 = QVBoxLayout(self.frame_336)
        self.verticalLayout_218.setSpacing(7)
        self.verticalLayout_218.setObjectName(u"verticalLayout_218")
        self.verticalLayout_218.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.frame_336)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(0, 20))
        self.label_65.setMaximumSize(QSize(16777215, 18))
        self.label_65.setFont(font3)
        self.label_65.setStyleSheet(u"")

        self.verticalLayout_218.addWidget(self.label_65)

        self.label_67 = QLabel(self.frame_336)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(0, 20))
        self.label_67.setMaximumSize(QSize(16777215, 18))
        self.label_67.setFont(font3)
        self.label_67.setStyleSheet(u"")

        self.verticalLayout_218.addWidget(self.label_67)

        self.label_68 = QLabel(self.frame_336)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(0, 20))
        self.label_68.setMaximumSize(QSize(16777215, 18))
        self.label_68.setFont(font3)
        self.label_68.setStyleSheet(u"")

        self.verticalLayout_218.addWidget(self.label_68)

        self.label_70 = QLabel(self.frame_336)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(0, 20))
        self.label_70.setMaximumSize(QSize(16777215, 18))
        self.label_70.setFont(font3)
        self.label_70.setStyleSheet(u"")

        self.verticalLayout_218.addWidget(self.label_70)


        self.horizontalLayout_135.addWidget(self.frame_336)

        self.frame_337 = QFrame(self.frame_335)
        self.frame_337.setObjectName(u"frame_337")
        sizePolicy.setHeightForWidth(self.frame_337.sizePolicy().hasHeightForWidth())
        self.frame_337.setSizePolicy(sizePolicy)
        self.frame_337.setMinimumSize(QSize(150, 0))
        self.frame_337.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_337.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_337.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_219 = QVBoxLayout(self.frame_337)
        self.verticalLayout_219.setSpacing(7)
        self.verticalLayout_219.setObjectName(u"verticalLayout_219")
        self.verticalLayout_219.setContentsMargins(0, 0, 0, 0)
        self.chipName = QLineEdit(self.frame_337)
        self.chipName.setObjectName(u"chipName")
        self.chipName.setEnabled(False)
        self.chipName.setMinimumSize(QSize(0, 20))
        self.chipName.setMaximumSize(QSize(180, 16777215))
        self.chipName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_219.addWidget(self.chipName)

        self.chipHeight = QLineEdit(self.frame_337)
        self.chipHeight.setObjectName(u"chipHeight")
        self.chipHeight.setMinimumSize(QSize(0, 20))
        self.chipHeight.setMaximumSize(QSize(180, 16777215))
        self.chipHeight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_219.addWidget(self.chipHeight)

        self.chipWidth = QLineEdit(self.frame_337)
        self.chipWidth.setObjectName(u"chipWidth")
        self.chipWidth.setMinimumSize(QSize(0, 20))
        self.chipWidth.setMaximumSize(QSize(180, 16777215))
        self.chipWidth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_219.addWidget(self.chipWidth)

        self.chipTrickness = QLineEdit(self.frame_337)
        self.chipTrickness.setObjectName(u"chipTrickness")
        self.chipTrickness.setMinimumSize(QSize(0, 20))
        self.chipTrickness.setMaximumSize(QSize(180, 16777215))
        self.chipTrickness.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_219.addWidget(self.chipTrickness)


        self.horizontalLayout_135.addWidget(self.frame_337)


        self.verticalLayout_217.addWidget(self.frame_335)


        self.verticalLayout_216.addWidget(self.frame_333)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_216.addItem(self.verticalSpacer_31)

        self.frame_338 = QFrame(self.frame_332)
        self.frame_338.setObjectName(u"frame_338")
        sizePolicy.setHeightForWidth(self.frame_338.sizePolicy().hasHeightForWidth())
        self.frame_338.setSizePolicy(sizePolicy)
        self.frame_338.setMinimumSize(QSize(311, 221))
        self.frame_338.setMaximumSize(QSize(16777215, 280))
        self.frame_338.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_338.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_220 = QVBoxLayout(self.frame_338)
        self.verticalLayout_220.setSpacing(6)
        self.verticalLayout_220.setObjectName(u"verticalLayout_220")
        self.verticalLayout_220.setContentsMargins(-1, 0, 0, 0)
        self.frame_339 = QFrame(self.frame_338)
        self.frame_339.setObjectName(u"frame_339")
        self.frame_339.setMinimumSize(QSize(0, 35))
        self.frame_339.setMaximumSize(QSize(16777215, 35))
        self.frame_339.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_339.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_136 = QHBoxLayout(self.frame_339)
        self.horizontalLayout_136.setSpacing(0)
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.frame_339)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(0, 35))
        self.label_77.setMaximumSize(QSize(16777215, 35))
        self.label_77.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_77.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_136.addWidget(self.label_77)


        self.verticalLayout_220.addWidget(self.frame_339)

        self.frame_340 = QFrame(self.frame_338)
        self.frame_340.setObjectName(u"frame_340")
        self.frame_340.setMinimumSize(QSize(283, 180))
        self.frame_340.setMaximumSize(QSize(16777215, 180))
        self.frame_340.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.frame_340.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_340.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_137 = QHBoxLayout(self.frame_340)
        self.horizontalLayout_137.setSpacing(6)
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalLayout_137.setContentsMargins(20, 12, -1, 0)
        self.frame_341 = QFrame(self.frame_340)
        self.frame_341.setObjectName(u"frame_341")
        sizePolicy.setHeightForWidth(self.frame_341.sizePolicy().hasHeightForWidth())
        self.frame_341.setSizePolicy(sizePolicy)
        self.frame_341.setMinimumSize(QSize(120, 0))
        self.frame_341.setStyleSheet(u"border: 0px;")
        self.frame_341.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_341.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_221 = QVBoxLayout(self.frame_341)
        self.verticalLayout_221.setSpacing(7)
        self.verticalLayout_221.setObjectName(u"verticalLayout_221")
        self.verticalLayout_221.setContentsMargins(0, 0, 0, 0)
        self.label_78 = QLabel(self.frame_341)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(0, 20))
        self.label_78.setMaximumSize(QSize(16777215, 18))
        self.label_78.setFont(font3)
        self.label_78.setStyleSheet(u"")

        self.verticalLayout_221.addWidget(self.label_78)

        self.label_79 = QLabel(self.frame_341)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(0, 20))
        self.label_79.setMaximumSize(QSize(16777215, 18))
        self.label_79.setFont(font3)
        self.label_79.setStyleSheet(u"")

        self.verticalLayout_221.addWidget(self.label_79)

        self.label_80 = QLabel(self.frame_341)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(0, 20))
        self.label_80.setMaximumSize(QSize(16777215, 18))
        self.label_80.setFont(font3)
        self.label_80.setStyleSheet(u"")

        self.verticalLayout_221.addWidget(self.label_80)

        self.label_81 = QLabel(self.frame_341)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(0, 20))
        self.label_81.setMaximumSize(QSize(16777215, 18))
        self.label_81.setFont(font3)
        self.label_81.setStyleSheet(u"")

        self.verticalLayout_221.addWidget(self.label_81)


        self.horizontalLayout_137.addWidget(self.frame_341)

        self.frame_342 = QFrame(self.frame_340)
        self.frame_342.setObjectName(u"frame_342")
        sizePolicy.setHeightForWidth(self.frame_342.sizePolicy().hasHeightForWidth())
        self.frame_342.setSizePolicy(sizePolicy)
        self.frame_342.setMinimumSize(QSize(150, 0))
        self.frame_342.setStyleSheet(u"QFrame{\n"
"border: 0px solid rgba(214, 214, 214, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_342.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_342.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_222 = QVBoxLayout(self.frame_342)
        self.verticalLayout_222.setSpacing(7)
        self.verticalLayout_222.setObjectName(u"verticalLayout_222")
        self.verticalLayout_222.setContentsMargins(0, 0, 0, 0)
        self.chipGlobalSize = QLineEdit(self.frame_342)
        self.chipGlobalSize.setObjectName(u"chipGlobalSize")
        self.chipGlobalSize.setMinimumSize(QSize(0, 20))
        self.chipGlobalSize.setMaximumSize(QSize(180, 16777215))
        self.chipGlobalSize.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.chipGlobalSize.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.chipGlobalSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_222.addWidget(self.chipGlobalSize)

        self.chipDeviationFactor = QLineEdit(self.frame_342)
        self.chipDeviationFactor.setObjectName(u"chipDeviationFactor")
        self.chipDeviationFactor.setMinimumSize(QSize(0, 20))
        self.chipDeviationFactor.setMaximumSize(QSize(180, 16777215))
        self.chipDeviationFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_222.addWidget(self.chipDeviationFactor)

        self.chipMininumFactor = QLineEdit(self.frame_342)
        self.chipMininumFactor.setObjectName(u"chipMininumFactor")
        self.chipMininumFactor.setMinimumSize(QSize(0, 20))
        self.chipMininumFactor.setMaximumSize(QSize(180, 16777215))
        self.chipMininumFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_222.addWidget(self.chipMininumFactor)

        self.chipOtherInfo = QLineEdit(self.frame_342)
        self.chipOtherInfo.setObjectName(u"chipOtherInfo")
        self.chipOtherInfo.setMinimumSize(QSize(0, 20))
        self.chipOtherInfo.setMaximumSize(QSize(180, 16777215))
        self.chipOtherInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_222.addWidget(self.chipOtherInfo)


        self.horizontalLayout_137.addWidget(self.frame_342)


        self.verticalLayout_220.addWidget(self.frame_340)


        self.verticalLayout_216.addWidget(self.frame_338)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_216.addItem(self.verticalSpacer_29)

        self.chipWarning = QLabel(self.frame_332)
        self.chipWarning.setObjectName(u"chipWarning")
        self.chipWarning.setFont(font4)
        self.chipWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chipWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.chipWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_216.addWidget(self.chipWarning)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_216.addItem(self.verticalSpacer_30)


        self.verticalLayout_223.addWidget(self.frame_332)

        self.tabWidget.addTab(self.chipPlayeTab, "")
        self.toolTab = QWidget()
        self.toolTab.setObjectName(u"toolTab")
        self.verticalLayout_215 = QVBoxLayout(self.toolTab)
        self.verticalLayout_215.setSpacing(0)
        self.verticalLayout_215.setObjectName(u"verticalLayout_215")
        self.verticalLayout_215.setContentsMargins(0, 0, 0, 0)
        self.frame_235 = QFrame(self.toolTab)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setStyleSheet(u"QLabel {\n"
"    font-size: 15px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semilight\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"\n"
"QFrame {\n"
"        background-color: rgb(182, 182, 182);\n"
"        border-radius: 15px; \n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_235.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_152 = QVBoxLayout(self.frame_235)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.frame_236 = QFrame(self.frame_235)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setMinimumSize(QSize(0, 250))
        self.frame_236.setMaximumSize(QSize(16777215, 250))
        self.frame_236.setStyleSheet(u"")
        self.frame_236.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_153 = QVBoxLayout(self.frame_236)
        self.verticalLayout_153.setSpacing(0)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(9, 0, 0, 0)
        self.frame_237 = QFrame(self.frame_236)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.frame_237)
        self.verticalLayout_154.setSpacing(0)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(0, 0, 0, -1)
        self.frame_238 = QFrame(self.frame_237)
        self.frame_238.setObjectName(u"frame_238")
        self.frame_238.setMinimumSize(QSize(0, 35))
        self.frame_238.setMaximumSize(QSize(16777215, 35))
        self.frame_238.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_238.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_238)
        self.verticalLayout_155.setSpacing(0)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.verticalLayout_155.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.frame_238)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(0, 35))
        self.label_82.setMaximumSize(QSize(16777215, 35))
        self.label_82.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_82.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_155.addWidget(self.label_82)


        self.verticalLayout_154.addWidget(self.frame_238)

        self.frame_239 = QFrame(self.frame_237)
        self.frame_239.setObjectName(u"frame_239")
        self.frame_239.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_239.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_123 = QHBoxLayout(self.frame_239)
        self.horizontalLayout_123.setSpacing(0)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.frame_240 = QFrame(self.frame_239)
        self.frame_240.setObjectName(u"frame_240")
        self.frame_240.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_240.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.frame_240)
        self.verticalLayout_156.setSpacing(0)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.verticalLayout_156.setContentsMargins(0, -1, 12, -1)
        self.frame_241 = QFrame(self.frame_240)
        self.frame_241.setObjectName(u"frame_241")
        self.frame_241.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_241.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_124 = QHBoxLayout(self.frame_241)
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(20, -1, 0, -1)
        self.frame_242 = QFrame(self.frame_241)
        self.frame_242.setObjectName(u"frame_242")
        sizePolicy1.setHeightForWidth(self.frame_242.sizePolicy().hasHeightForWidth())
        self.frame_242.setSizePolicy(sizePolicy1)
        self.frame_242.setMaximumSize(QSize(180, 16777215))
        self.frame_242.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_242.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.frame_242)
        self.verticalLayout_157.setSpacing(7)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.verticalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.label_186 = QLabel(self.frame_242)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setMinimumSize(QSize(0, 20))
        self.label_186.setMaximumSize(QSize(16777215, 20))
        self.label_186.setFont(font3)
        self.label_186.setStyleSheet(u"")

        self.verticalLayout_157.addWidget(self.label_186)

        self.label_187 = QLabel(self.frame_242)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setMinimumSize(QSize(0, 20))
        self.label_187.setMaximumSize(QSize(16777215, 20))
        self.label_187.setFont(font3)
        self.label_187.setStyleSheet(u"")

        self.verticalLayout_157.addWidget(self.label_187)

        self.label_188 = QLabel(self.frame_242)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setMinimumSize(QSize(0, 20))
        self.label_188.setMaximumSize(QSize(16777215, 20))
        self.label_188.setFont(font3)
        self.label_188.setStyleSheet(u"")

        self.verticalLayout_157.addWidget(self.label_188)

        self.label_189 = QLabel(self.frame_242)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setMinimumSize(QSize(0, 20))
        self.label_189.setMaximumSize(QSize(16777215, 20))
        self.label_189.setFont(font3)
        self.label_189.setStyleSheet(u"")

        self.verticalLayout_157.addWidget(self.label_189)


        self.horizontalLayout_124.addWidget(self.frame_242)

        self.frame_243 = QFrame(self.frame_241)
        self.frame_243.setObjectName(u"frame_243")
        sizePolicy1.setHeightForWidth(self.frame_243.sizePolicy().hasHeightForWidth())
        self.frame_243.setSizePolicy(sizePolicy1)
        self.frame_243.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_243.setStyleSheet(u"")
        self.frame_243.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_243.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_158 = QVBoxLayout(self.frame_243)
        self.verticalLayout_158.setSpacing(7)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.verticalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.toolName = QLineEdit(self.frame_243)
        self.toolName.setObjectName(u"toolName")
        self.toolName.setEnabled(False)
        self.toolName.setMinimumSize(QSize(0, 20))
        self.toolName.setMaximumSize(QSize(180, 16777215))
        self.toolName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_158.addWidget(self.toolName)

        self.toolTrickness = QLineEdit(self.frame_243)
        self.toolTrickness.setObjectName(u"toolTrickness")
        self.toolTrickness.setMinimumSize(QSize(0, 20))
        self.toolTrickness.setMaximumSize(QSize(180, 16777215))
        self.toolTrickness.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_158.addWidget(self.toolTrickness)

        self.toolRakeAngle = QLineEdit(self.frame_243)
        self.toolRakeAngle.setObjectName(u"toolRakeAngle")
        self.toolRakeAngle.setMinimumSize(QSize(0, 20))
        self.toolRakeAngle.setMaximumSize(QSize(180, 16777215))
        self.toolRakeAngle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_158.addWidget(self.toolRakeAngle)

        self.toolRakeDimension = QLineEdit(self.frame_243)
        self.toolRakeDimension.setObjectName(u"toolRakeDimension")
        self.toolRakeDimension.setMinimumSize(QSize(0, 20))
        self.toolRakeDimension.setMaximumSize(QSize(180, 16777215))
        self.toolRakeDimension.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_158.addWidget(self.toolRakeDimension)


        self.horizontalLayout_124.addWidget(self.frame_243)


        self.verticalLayout_156.addWidget(self.frame_241)


        self.horizontalLayout_123.addWidget(self.frame_240)

        self.frame_244 = QFrame(self.frame_239)
        self.frame_244.setObjectName(u"frame_244")
        self.frame_244.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_244.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.frame_244)
        self.verticalLayout_159.setSpacing(0)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.frame_245 = QFrame(self.frame_244)
        self.frame_245.setObjectName(u"frame_245")
        self.frame_245.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_245.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_125 = QHBoxLayout(self.frame_245)
        self.horizontalLayout_125.setSpacing(20)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(15, -1, -1, -1)
        self.frame_246 = QFrame(self.frame_245)
        self.frame_246.setObjectName(u"frame_246")
        self.frame_246.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_246.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_127 = QHBoxLayout(self.frame_246)
        self.horizontalLayout_127.setSpacing(6)
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.horizontalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.frame_247 = QFrame(self.frame_246)
        self.frame_247.setObjectName(u"frame_247")
        sizePolicy1.setHeightForWidth(self.frame_247.sizePolicy().hasHeightForWidth())
        self.frame_247.setSizePolicy(sizePolicy1)
        self.frame_247.setMaximumSize(QSize(180, 16777215))
        self.frame_247.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_247.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.frame_247)
        self.verticalLayout_160.setSpacing(7)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.verticalLayout_160.setContentsMargins(0, 0, 0, 0)
        self.label_190 = QLabel(self.frame_247)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setMinimumSize(QSize(0, 20))
        self.label_190.setMaximumSize(QSize(16777215, 20))
        self.label_190.setFont(font3)
        self.label_190.setStyleSheet(u"")

        self.verticalLayout_160.addWidget(self.label_190)

        self.label_191 = QLabel(self.frame_247)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setMinimumSize(QSize(0, 20))
        self.label_191.setMaximumSize(QSize(16777215, 20))
        self.label_191.setFont(font3)
        self.label_191.setStyleSheet(u"")

        self.verticalLayout_160.addWidget(self.label_191)

        self.label_192 = QLabel(self.frame_247)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setMinimumSize(QSize(0, 20))
        self.label_192.setMaximumSize(QSize(16777215, 20))
        self.label_192.setFont(font3)
        self.label_192.setStyleSheet(u"")

        self.verticalLayout_160.addWidget(self.label_192)

        self.label_193 = QLabel(self.frame_247)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setMinimumSize(QSize(0, 18))
        self.label_193.setMaximumSize(QSize(16777215, 18))
        self.label_193.setFont(font3)
        self.label_193.setStyleSheet(u"")

        self.verticalLayout_160.addWidget(self.label_193)


        self.horizontalLayout_127.addWidget(self.frame_247)

        self.frame_248 = QFrame(self.frame_246)
        self.frame_248.setObjectName(u"frame_248")
        sizePolicy1.setHeightForWidth(self.frame_248.sizePolicy().hasHeightForWidth())
        self.frame_248.setSizePolicy(sizePolicy1)
        self.frame_248.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_248.setStyleSheet(u"")
        self.frame_248.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_248.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.frame_248)
        self.verticalLayout_161.setSpacing(7)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.toolClearanceAngle = QLineEdit(self.frame_248)
        self.toolClearanceAngle.setObjectName(u"toolClearanceAngle")
        self.toolClearanceAngle.setMinimumSize(QSize(0, 20))
        self.toolClearanceAngle.setMaximumSize(QSize(189, 16777215))
        self.toolClearanceAngle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_161.addWidget(self.toolClearanceAngle)

        self.toolClearanceDimension = QLineEdit(self.frame_248)
        self.toolClearanceDimension.setObjectName(u"toolClearanceDimension")
        self.toolClearanceDimension.setMinimumSize(QSize(0, 20))
        self.toolClearanceDimension.setMaximumSize(QSize(189, 16777215))
        self.toolClearanceDimension.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_161.addWidget(self.toolClearanceDimension)

        self.toolRadius = QLineEdit(self.frame_248)
        self.toolRadius.setObjectName(u"toolRadius")
        self.toolRadius.setMinimumSize(QSize(0, 20))
        self.toolRadius.setMaximumSize(QSize(189, 16777215))
        self.toolRadius.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_161.addWidget(self.toolRadius)

        self.label_194 = QLabel(self.frame_248)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setMinimumSize(QSize(0, 18))
        self.label_194.setMaximumSize(QSize(16777215, 18))
        self.label_194.setFont(font3)
        self.label_194.setStyleSheet(u"")

        self.verticalLayout_161.addWidget(self.label_194)


        self.horizontalLayout_127.addWidget(self.frame_248)


        self.horizontalLayout_125.addWidget(self.frame_246)


        self.verticalLayout_159.addWidget(self.frame_245)


        self.horizontalLayout_123.addWidget(self.frame_244)


        self.verticalLayout_154.addWidget(self.frame_239)


        self.verticalLayout_153.addWidget(self.frame_237)


        self.verticalLayout_152.addWidget(self.frame_236)

        self.verticalSpacer_20 = QSpacerItem(20, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_152.addItem(self.verticalSpacer_20)

        self.frame_249 = QFrame(self.frame_235)
        self.frame_249.setObjectName(u"frame_249")
        self.frame_249.setMinimumSize(QSize(0, 0))
        self.frame_249.setMaximumSize(QSize(16777215, 100))
        self.frame_249.setStyleSheet(u"")
        self.frame_249.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_249.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.frame_249)
        self.verticalLayout_162.setSpacing(0)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(9, 0, 0, 0)
        self.frame_250 = QFrame(self.frame_249)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.frame_250)
        self.verticalLayout_163.setSpacing(0)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, -1)
        self.frame_251 = QFrame(self.frame_250)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setMinimumSize(QSize(0, 35))
        self.frame_251.setMaximumSize(QSize(16777215, 35))
        self.frame_251.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_128 = QHBoxLayout(self.frame_251)
        self.horizontalLayout_128.setSpacing(0)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.frame_251)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(0, 35))
        self.label_84.setMaximumSize(QSize(16777215, 35))
        self.label_84.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_128.addWidget(self.label_84)


        self.verticalLayout_163.addWidget(self.frame_251)

        self.frame_252 = QFrame(self.frame_250)
        self.frame_252.setObjectName(u"frame_252")
        self.frame_252.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_252.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_129 = QHBoxLayout(self.frame_252)
        self.horizontalLayout_129.setSpacing(0)
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.frame_253 = QFrame(self.frame_252)
        self.frame_253.setObjectName(u"frame_253")
        self.frame_253.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_253.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_201 = QVBoxLayout(self.frame_253)
        self.verticalLayout_201.setSpacing(0)
        self.verticalLayout_201.setObjectName(u"verticalLayout_201")
        self.verticalLayout_201.setContentsMargins(0, 0, 12, 0)
        self.frame_254 = QFrame(self.frame_253)
        self.frame_254.setObjectName(u"frame_254")
        self.frame_254.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_254.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_130 = QHBoxLayout(self.frame_254)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(20, -1, 0, -1)
        self.frame_255 = QFrame(self.frame_254)
        self.frame_255.setObjectName(u"frame_255")
        sizePolicy1.setHeightForWidth(self.frame_255.sizePolicy().hasHeightForWidth())
        self.frame_255.setSizePolicy(sizePolicy1)
        self.frame_255.setMinimumSize(QSize(180, 0))
        self.frame_255.setMaximumSize(QSize(140, 16777215))
        self.frame_255.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_202 = QVBoxLayout(self.frame_255)
        self.verticalLayout_202.setSpacing(7)
        self.verticalLayout_202.setObjectName(u"verticalLayout_202")
        self.verticalLayout_202.setContentsMargins(0, 0, 0, 0)
        self.label_195 = QLabel(self.frame_255)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setMinimumSize(QSize(180, 0))
        self.label_195.setMaximumSize(QSize(180, 20))
        self.label_195.setFont(font3)
        self.label_195.setStyleSheet(u"")

        self.verticalLayout_202.addWidget(self.label_195)


        self.horizontalLayout_130.addWidget(self.frame_255)

        self.frame_256 = QFrame(self.frame_254)
        self.frame_256.setObjectName(u"frame_256")
        sizePolicy1.setHeightForWidth(self.frame_256.sizePolicy().hasHeightForWidth())
        self.frame_256.setSizePolicy(sizePolicy1)
        self.frame_256.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_256.setStyleSheet(u"")
        self.frame_256.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_203 = QVBoxLayout(self.frame_256)
        self.verticalLayout_203.setSpacing(7)
        self.verticalLayout_203.setObjectName(u"verticalLayout_203")
        self.verticalLayout_203.setContentsMargins(0, 0, 0, 0)
        self.toolPartition01 = QLineEdit(self.frame_256)
        self.toolPartition01.setObjectName(u"toolPartition01")
        self.toolPartition01.setMinimumSize(QSize(0, 20))
        self.toolPartition01.setMaximumSize(QSize(180, 16777215))
        self.toolPartition01.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toolPartition01.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_203.addWidget(self.toolPartition01)


        self.horizontalLayout_130.addWidget(self.frame_256)


        self.verticalLayout_201.addWidget(self.frame_254)


        self.horizontalLayout_129.addWidget(self.frame_253)

        self.frame_257 = QFrame(self.frame_252)
        self.frame_257.setObjectName(u"frame_257")
        self.frame_257.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_257.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_204 = QVBoxLayout(self.frame_257)
        self.verticalLayout_204.setSpacing(0)
        self.verticalLayout_204.setObjectName(u"verticalLayout_204")
        self.verticalLayout_204.setContentsMargins(-1, 0, -1, 0)
        self.frame_258 = QFrame(self.frame_257)
        self.frame_258.setObjectName(u"frame_258")
        self.frame_258.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_258.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_131 = QHBoxLayout(self.frame_258)
        self.horizontalLayout_131.setSpacing(20)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(15, -1, -1, -1)
        self.frame_316 = QFrame(self.frame_258)
        self.frame_316.setObjectName(u"frame_316")
        self.frame_316.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_316.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.frame_316)
        self.horizontalLayout_132.setSpacing(6)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.frame_317 = QFrame(self.frame_316)
        self.frame_317.setObjectName(u"frame_317")
        sizePolicy1.setHeightForWidth(self.frame_317.sizePolicy().hasHeightForWidth())
        self.frame_317.setSizePolicy(sizePolicy1)
        self.frame_317.setMinimumSize(QSize(180, 0))
        self.frame_317.setMaximumSize(QSize(140, 16777215))
        self.frame_317.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_317.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_205 = QVBoxLayout(self.frame_317)
        self.verticalLayout_205.setSpacing(7)
        self.verticalLayout_205.setObjectName(u"verticalLayout_205")
        self.verticalLayout_205.setContentsMargins(0, 0, 0, 0)
        self.label_196 = QLabel(self.frame_317)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setMinimumSize(QSize(180, 0))
        self.label_196.setMaximumSize(QSize(180, 20))
        self.label_196.setFont(font3)
        self.label_196.setStyleSheet(u"")

        self.verticalLayout_205.addWidget(self.label_196)


        self.horizontalLayout_132.addWidget(self.frame_317)

        self.frame_318 = QFrame(self.frame_316)
        self.frame_318.setObjectName(u"frame_318")
        sizePolicy1.setHeightForWidth(self.frame_318.sizePolicy().hasHeightForWidth())
        self.frame_318.setSizePolicy(sizePolicy1)
        self.frame_318.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_318.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_318.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_206 = QVBoxLayout(self.frame_318)
        self.verticalLayout_206.setSpacing(7)
        self.verticalLayout_206.setObjectName(u"verticalLayout_206")
        self.verticalLayout_206.setContentsMargins(0, 0, 0, 0)
        self.toolPartition02 = QLineEdit(self.frame_318)
        self.toolPartition02.setObjectName(u"toolPartition02")
        self.toolPartition02.setMinimumSize(QSize(0, 20))
        self.toolPartition02.setMaximumSize(QSize(189, 16777215))
        self.toolPartition02.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_206.addWidget(self.toolPartition02)


        self.horizontalLayout_132.addWidget(self.frame_318)


        self.horizontalLayout_131.addWidget(self.frame_316)


        self.verticalLayout_204.addWidget(self.frame_258)


        self.horizontalLayout_129.addWidget(self.frame_257)


        self.verticalLayout_163.addWidget(self.frame_252)


        self.verticalLayout_162.addWidget(self.frame_250)


        self.verticalLayout_152.addWidget(self.frame_249)

        self.verticalSpacer_21 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_152.addItem(self.verticalSpacer_21)

        self.frame_319 = QFrame(self.frame_235)
        self.frame_319.setObjectName(u"frame_319")
        self.frame_319.setMinimumSize(QSize(0, 250))
        self.frame_319.setMaximumSize(QSize(16777215, 250))
        self.frame_319.setStyleSheet(u"")
        self.frame_319.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_319.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_207 = QVBoxLayout(self.frame_319)
        self.verticalLayout_207.setSpacing(0)
        self.verticalLayout_207.setObjectName(u"verticalLayout_207")
        self.verticalLayout_207.setContentsMargins(9, 0, 0, 0)
        self.frame_320 = QFrame(self.frame_319)
        self.frame_320.setObjectName(u"frame_320")
        self.frame_320.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_320.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_208 = QVBoxLayout(self.frame_320)
        self.verticalLayout_208.setSpacing(0)
        self.verticalLayout_208.setObjectName(u"verticalLayout_208")
        self.verticalLayout_208.setContentsMargins(0, 0, 0, -1)
        self.frame_321 = QFrame(self.frame_320)
        self.frame_321.setObjectName(u"frame_321")
        self.frame_321.setMinimumSize(QSize(0, 35))
        self.frame_321.setMaximumSize(QSize(16777215, 35))
        self.frame_321.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_321.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_321)
        self.horizontalLayout_133.setSpacing(0)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.label_85 = QLabel(self.frame_321)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(0, 35))
        self.label_85.setMaximumSize(QSize(16777215, 35))
        self.label_85.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_85.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_133.addWidget(self.label_85)


        self.verticalLayout_208.addWidget(self.frame_321)

        self.frame_322 = QFrame(self.frame_320)
        self.frame_322.setObjectName(u"frame_322")
        self.frame_322.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_322.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.frame_322)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.frame_323 = QFrame(self.frame_322)
        self.frame_323.setObjectName(u"frame_323")
        self.frame_323.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_323.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_209 = QVBoxLayout(self.frame_323)
        self.verticalLayout_209.setSpacing(0)
        self.verticalLayout_209.setObjectName(u"verticalLayout_209")
        self.verticalLayout_209.setContentsMargins(0, -1, 12, -1)
        self.frame_324 = QFrame(self.frame_323)
        self.frame_324.setObjectName(u"frame_324")
        self.frame_324.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_324.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.frame_324)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(20, -1, 0, -1)
        self.frame_325 = QFrame(self.frame_324)
        self.frame_325.setObjectName(u"frame_325")
        sizePolicy1.setHeightForWidth(self.frame_325.sizePolicy().hasHeightForWidth())
        self.frame_325.setSizePolicy(sizePolicy1)
        self.frame_325.setMaximumSize(QSize(180, 16777215))
        self.frame_325.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_325.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_210 = QVBoxLayout(self.frame_325)
        self.verticalLayout_210.setSpacing(7)
        self.verticalLayout_210.setObjectName(u"verticalLayout_210")
        self.verticalLayout_210.setContentsMargins(0, 0, 0, 0)
        self.label_197 = QLabel(self.frame_325)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setMinimumSize(QSize(0, 20))
        self.label_197.setMaximumSize(QSize(16777215, 20))
        self.label_197.setFont(font3)
        self.label_197.setStyleSheet(u"")

        self.verticalLayout_210.addWidget(self.label_197)

        self.label_198 = QLabel(self.frame_325)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setMinimumSize(QSize(0, 20))
        self.label_198.setMaximumSize(QSize(16777215, 20))
        self.label_198.setFont(font3)
        self.label_198.setStyleSheet(u"")

        self.verticalLayout_210.addWidget(self.label_198)

        self.label_199 = QLabel(self.frame_325)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setMinimumSize(QSize(0, 20))
        self.label_199.setMaximumSize(QSize(16777215, 20))
        self.label_199.setFont(font3)
        self.label_199.setStyleSheet(u"")

        self.verticalLayout_210.addWidget(self.label_199)

        self.label_200 = QLabel(self.frame_325)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setMinimumSize(QSize(0, 20))
        self.label_200.setMaximumSize(QSize(16777215, 20))
        self.label_200.setFont(font3)
        self.label_200.setStyleSheet(u"")

        self.verticalLayout_210.addWidget(self.label_200)


        self.horizontalLayout_139.addWidget(self.frame_325)

        self.frame_326 = QFrame(self.frame_324)
        self.frame_326.setObjectName(u"frame_326")
        sizePolicy1.setHeightForWidth(self.frame_326.sizePolicy().hasHeightForWidth())
        self.frame_326.setSizePolicy(sizePolicy1)
        self.frame_326.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_326.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_326.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_211 = QVBoxLayout(self.frame_326)
        self.verticalLayout_211.setSpacing(7)
        self.verticalLayout_211.setObjectName(u"verticalLayout_211")
        self.verticalLayout_211.setContentsMargins(0, 0, 0, 0)
        self.toolGlobalSize = QLineEdit(self.frame_326)
        self.toolGlobalSize.setObjectName(u"toolGlobalSize")
        self.toolGlobalSize.setMinimumSize(QSize(0, 20))
        self.toolGlobalSize.setMaximumSize(QSize(180, 16777215))
        self.toolGlobalSize.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_211.addWidget(self.toolGlobalSize)

        self.toolDeviationFactor = QLineEdit(self.frame_326)
        self.toolDeviationFactor.setObjectName(u"toolDeviationFactor")
        self.toolDeviationFactor.setMinimumSize(QSize(0, 20))
        self.toolDeviationFactor.setMaximumSize(QSize(180, 16777215))
        self.toolDeviationFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_211.addWidget(self.toolDeviationFactor)

        self.toolMinimumFactor = QLineEdit(self.frame_326)
        self.toolMinimumFactor.setObjectName(u"toolMinimumFactor")
        self.toolMinimumFactor.setMinimumSize(QSize(0, 20))
        self.toolMinimumFactor.setMaximumSize(QSize(180, 16777215))
        self.toolMinimumFactor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_211.addWidget(self.toolMinimumFactor)

        self.toolOthersInfo = QLineEdit(self.frame_326)
        self.toolOthersInfo.setObjectName(u"toolOthersInfo")
        self.toolOthersInfo.setMinimumSize(QSize(0, 20))
        self.toolOthersInfo.setMaximumSize(QSize(180, 16777215))
        self.toolOthersInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_211.addWidget(self.toolOthersInfo)


        self.horizontalLayout_139.addWidget(self.frame_326)


        self.verticalLayout_209.addWidget(self.frame_324)


        self.horizontalLayout_138.addWidget(self.frame_323)

        self.frame_327 = QFrame(self.frame_322)
        self.frame_327.setObjectName(u"frame_327")
        self.frame_327.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_327.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_212 = QVBoxLayout(self.frame_327)
        self.verticalLayout_212.setSpacing(0)
        self.verticalLayout_212.setObjectName(u"verticalLayout_212")
        self.frame_328 = QFrame(self.frame_327)
        self.frame_328.setObjectName(u"frame_328")
        self.frame_328.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_328.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.frame_328)
        self.horizontalLayout_140.setSpacing(20)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(15, -1, -1, -1)
        self.frame_329 = QFrame(self.frame_328)
        self.frame_329.setObjectName(u"frame_329")
        self.frame_329.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_329.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.frame_329)
        self.horizontalLayout_141.setSpacing(6)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.frame_330 = QFrame(self.frame_329)
        self.frame_330.setObjectName(u"frame_330")
        sizePolicy1.setHeightForWidth(self.frame_330.sizePolicy().hasHeightForWidth())
        self.frame_330.setSizePolicy(sizePolicy1)
        self.frame_330.setMaximumSize(QSize(180, 16777215))
        self.frame_330.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_330.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_213 = QVBoxLayout(self.frame_330)
        self.verticalLayout_213.setSpacing(7)
        self.verticalLayout_213.setObjectName(u"verticalLayout_213")
        self.verticalLayout_213.setContentsMargins(0, 0, 0, 0)
        self.label_201 = QLabel(self.frame_330)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setMinimumSize(QSize(0, 20))
        self.label_201.setMaximumSize(QSize(16777215, 20))
        self.label_201.setFont(font3)
        self.label_201.setStyleSheet(u"")

        self.verticalLayout_213.addWidget(self.label_201)

        self.label_202 = QLabel(self.frame_330)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setMinimumSize(QSize(0, 20))
        self.label_202.setMaximumSize(QSize(16777215, 20))
        self.label_202.setFont(font3)
        self.label_202.setStyleSheet(u"")

        self.verticalLayout_213.addWidget(self.label_202)

        self.label_203 = QLabel(self.frame_330)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setMinimumSize(QSize(0, 20))
        self.label_203.setMaximumSize(QSize(16777215, 20))
        self.label_203.setFont(font3)
        self.label_203.setStyleSheet(u"")

        self.verticalLayout_213.addWidget(self.label_203)

        self.label_204 = QLabel(self.frame_330)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setMinimumSize(QSize(0, 20))
        self.label_204.setMaximumSize(QSize(16777215, 20))
        self.label_204.setFont(font3)
        self.label_204.setStyleSheet(u"")

        self.verticalLayout_213.addWidget(self.label_204)


        self.horizontalLayout_141.addWidget(self.frame_330)

        self.frame_331 = QFrame(self.frame_329)
        self.frame_331.setObjectName(u"frame_331")
        sizePolicy1.setHeightForWidth(self.frame_331.sizePolicy().hasHeightForWidth())
        self.frame_331.setSizePolicy(sizePolicy1)
        self.frame_331.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_331.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_331.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_214 = QVBoxLayout(self.frame_331)
        self.verticalLayout_214.setSpacing(7)
        self.verticalLayout_214.setObjectName(u"verticalLayout_214")
        self.verticalLayout_214.setContentsMargins(0, 0, 0, 0)
        self.toolOthersInfo_7 = QLineEdit(self.frame_331)
        self.toolOthersInfo_7.setObjectName(u"toolOthersInfo_7")
        self.toolOthersInfo_7.setMinimumSize(QSize(0, 20))
        self.toolOthersInfo_7.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_214.addWidget(self.toolOthersInfo_7)

        self.toolOthersInfo_8 = QLineEdit(self.frame_331)
        self.toolOthersInfo_8.setObjectName(u"toolOthersInfo_8")
        self.toolOthersInfo_8.setMinimumSize(QSize(0, 20))
        self.toolOthersInfo_8.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_214.addWidget(self.toolOthersInfo_8)

        self.toolOthersInfo_9 = QLineEdit(self.frame_331)
        self.toolOthersInfo_9.setObjectName(u"toolOthersInfo_9")
        self.toolOthersInfo_9.setMinimumSize(QSize(0, 20))
        self.toolOthersInfo_9.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_214.addWidget(self.toolOthersInfo_9)

        self.toolOthersInfo_10 = QLineEdit(self.frame_331)
        self.toolOthersInfo_10.setObjectName(u"toolOthersInfo_10")
        self.toolOthersInfo_10.setMinimumSize(QSize(0, 20))
        self.toolOthersInfo_10.setMaximumSize(QSize(189, 16777215))
        self.toolOthersInfo_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_214.addWidget(self.toolOthersInfo_10)


        self.horizontalLayout_141.addWidget(self.frame_331)


        self.horizontalLayout_140.addWidget(self.frame_329)


        self.verticalLayout_212.addWidget(self.frame_328)


        self.horizontalLayout_138.addWidget(self.frame_327)


        self.verticalLayout_208.addWidget(self.frame_322)


        self.verticalLayout_207.addWidget(self.frame_320)


        self.verticalLayout_152.addWidget(self.frame_319)

        self.verticalSpacer_27 = QSpacerItem(20, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_152.addItem(self.verticalSpacer_27)

        self.toolWarning = QLabel(self.frame_235)
        self.toolWarning.setObjectName(u"toolWarning")
        self.toolWarning.setFont(font4)
        self.toolWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toolWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.toolWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toolWarning.setWordWrap(True)

        self.verticalLayout_152.addWidget(self.toolWarning)

        self.verticalSpacer_28 = QSpacerItem(20, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_152.addItem(self.verticalSpacer_28)


        self.verticalLayout_215.addWidget(self.frame_235)

        self.tabWidget.addTab(self.toolTab, "")
        self.assemblyTab = QWidget()
        self.assemblyTab.setObjectName(u"assemblyTab")
        self.assemblyTab.setEnabled(True)
        self.assemblyTab.setStyleSheet(u"")
        self.verticalLayout_200 = QVBoxLayout(self.assemblyTab)
        self.verticalLayout_200.setSpacing(0)
        self.verticalLayout_200.setObjectName(u"verticalLayout_200")
        self.verticalLayout_200.setContentsMargins(0, 0, 0, 0)
        self.frame_263 = QFrame(self.assemblyTab)
        self.frame_263.setObjectName(u"frame_263")
        self.frame_263.setEnabled(True)
        self.frame_263.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(182, 182, 182);\n"
"    border-radius: 15px; \n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_263.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_263.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_167 = QVBoxLayout(self.frame_263)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.verticalLayout_167.setContentsMargins(18, -1, 18, -1)
        self.frame_264 = QFrame(self.frame_263)
        self.frame_264.setObjectName(u"frame_264")
        self.frame_264.setMinimumSize(QSize(0, 0))
        self.frame_264.setMaximumSize(QSize(16777215, 100))
        self.frame_264.setStyleSheet(u"")
        self.frame_264.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_264.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.frame_264)
        self.verticalLayout_168.setSpacing(0)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.frame_265 = QFrame(self.frame_264)
        self.frame_265.setObjectName(u"frame_265")
        self.frame_265.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_265.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_265)
        self.verticalLayout_169.setSpacing(0)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.verticalLayout_169.setContentsMargins(0, 0, 0, -1)
        self.frame_266 = QFrame(self.frame_265)
        self.frame_266.setObjectName(u"frame_266")
        self.frame_266.setMinimumSize(QSize(0, 35))
        self.frame_266.setMaximumSize(QSize(16777215, 35))
        self.frame_266.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_266.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.frame_266)
        self.horizontalLayout_142.setSpacing(0)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.frame_266)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(0, 35))
        self.label_86.setMaximumSize(QSize(16777215, 35))
        self.label_86.setStyleSheet(u"QLabel {\n"
"    font-size: 24px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_86.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_142.addWidget(self.label_86)


        self.verticalLayout_169.addWidget(self.frame_266)

        self.frame_267 = QFrame(self.frame_265)
        self.frame_267.setObjectName(u"frame_267")
        self.frame_267.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_267.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.frame_267)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.frame_268 = QFrame(self.frame_267)
        self.frame_268.setObjectName(u"frame_268")
        self.frame_268.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_268.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_268)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.frame_269 = QFrame(self.frame_268)
        self.frame_269.setObjectName(u"frame_269")
        self.frame_269.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_269.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.frame_269)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(20, -1, 0, -1)
        self.frame_270 = QFrame(self.frame_269)
        self.frame_270.setObjectName(u"frame_270")
        sizePolicy.setHeightForWidth(self.frame_270.sizePolicy().hasHeightForWidth())
        self.frame_270.setSizePolicy(sizePolicy)
        self.frame_270.setMinimumSize(QSize(40, 0))
        self.frame_270.setMaximumSize(QSize(140, 16777215))
        self.frame_270.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_270.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_270)
        self.verticalLayout_171.setSpacing(7)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.label_179 = QLabel(self.frame_270)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setMinimumSize(QSize(30, 20))
        self.label_179.setMaximumSize(QSize(16777215, 18))
        self.label_179.setFont(font3)
        self.label_179.setStyleSheet(u"")

        self.verticalLayout_171.addWidget(self.label_179)


        self.horizontalLayout_144.addWidget(self.frame_270)

        self.frame_271 = QFrame(self.frame_269)
        self.frame_271.setObjectName(u"frame_271")
        sizePolicy1.setHeightForWidth(self.frame_271.sizePolicy().hasHeightForWidth())
        self.frame_271.setSizePolicy(sizePolicy1)
        self.frame_271.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_271.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_271.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_172 = QVBoxLayout(self.frame_271)
        self.verticalLayout_172.setSpacing(7)
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.verticalLayout_172.setContentsMargins(0, 0, 0, 0)
        self.xEulerian = QLineEdit(self.frame_271)
        self.xEulerian.setObjectName(u"xEulerian")
        self.xEulerian.setEnabled(False)
        self.xEulerian.setMinimumSize(QSize(160, 20))
        self.xEulerian.setMaximumSize(QSize(180, 16777215))
        self.xEulerian.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_172.addWidget(self.xEulerian)


        self.horizontalLayout_144.addWidget(self.frame_271)


        self.verticalLayout_170.addWidget(self.frame_269)


        self.horizontalLayout_143.addWidget(self.frame_268)

        self.frame_272 = QFrame(self.frame_267)
        self.frame_272.setObjectName(u"frame_272")
        self.frame_272.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_272.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_173 = QVBoxLayout(self.frame_272)
        self.verticalLayout_173.setSpacing(0)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.verticalLayout_173.setContentsMargins(-1, 0, -1, 0)
        self.frame_273 = QFrame(self.frame_272)
        self.frame_273.setObjectName(u"frame_273")
        self.frame_273.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_273.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_145 = QHBoxLayout(self.frame_273)
        self.horizontalLayout_145.setSpacing(20)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(15, -1, 0, -1)
        self.frame_274 = QFrame(self.frame_273)
        self.frame_274.setObjectName(u"frame_274")
        self.frame_274.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_274.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_146 = QHBoxLayout(self.frame_274)
        self.horizontalLayout_146.setSpacing(6)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.frame_275 = QFrame(self.frame_274)
        self.frame_275.setObjectName(u"frame_275")
        sizePolicy.setHeightForWidth(self.frame_275.sizePolicy().hasHeightForWidth())
        self.frame_275.setSizePolicy(sizePolicy)
        self.frame_275.setMinimumSize(QSize(40, 0))
        self.frame_275.setMaximumSize(QSize(140, 16777215))
        self.frame_275.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_275.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_174 = QVBoxLayout(self.frame_275)
        self.verticalLayout_174.setSpacing(7)
        self.verticalLayout_174.setObjectName(u"verticalLayout_174")
        self.verticalLayout_174.setContentsMargins(0, 0, 0, 0)
        self.label_180 = QLabel(self.frame_275)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setMinimumSize(QSize(0, 20))
        self.label_180.setMaximumSize(QSize(16777215, 18))
        self.label_180.setFont(font3)
        self.label_180.setStyleSheet(u"")

        self.verticalLayout_174.addWidget(self.label_180)


        self.horizontalLayout_146.addWidget(self.frame_275)

        self.frame_276 = QFrame(self.frame_274)
        self.frame_276.setObjectName(u"frame_276")
        sizePolicy1.setHeightForWidth(self.frame_276.sizePolicy().hasHeightForWidth())
        self.frame_276.setSizePolicy(sizePolicy1)
        self.frame_276.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_276.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_276.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_175 = QVBoxLayout(self.frame_276)
        self.verticalLayout_175.setSpacing(7)
        self.verticalLayout_175.setObjectName(u"verticalLayout_175")
        self.verticalLayout_175.setContentsMargins(0, 0, 0, 0)
        self.yEulerian = QLineEdit(self.frame_276)
        self.yEulerian.setObjectName(u"yEulerian")
        self.yEulerian.setEnabled(False)
        self.yEulerian.setMinimumSize(QSize(160, 20))
        self.yEulerian.setMaximumSize(QSize(189, 16777215))
        self.yEulerian.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_175.addWidget(self.yEulerian)


        self.horizontalLayout_146.addWidget(self.frame_276)


        self.horizontalLayout_145.addWidget(self.frame_274)


        self.verticalLayout_173.addWidget(self.frame_273)


        self.horizontalLayout_143.addWidget(self.frame_272)


        self.verticalLayout_169.addWidget(self.frame_267)


        self.verticalLayout_168.addWidget(self.frame_265)


        self.verticalLayout_167.addWidget(self.frame_264)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_22)

        self.frame_277 = QFrame(self.frame_263)
        self.frame_277.setObjectName(u"frame_277")
        self.frame_277.setMinimumSize(QSize(0, 0))
        self.frame_277.setMaximumSize(QSize(16777215, 100))
        self.frame_277.setStyleSheet(u"")
        self.frame_277.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_277.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_176 = QVBoxLayout(self.frame_277)
        self.verticalLayout_176.setSpacing(0)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.verticalLayout_176.setContentsMargins(0, 0, 0, 0)
        self.frame_278 = QFrame(self.frame_277)
        self.frame_278.setObjectName(u"frame_278")
        self.frame_278.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_278.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_177 = QVBoxLayout(self.frame_278)
        self.verticalLayout_177.setSpacing(0)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.verticalLayout_177.setContentsMargins(0, 0, 0, -1)
        self.frame_279 = QFrame(self.frame_278)
        self.frame_279.setObjectName(u"frame_279")
        self.frame_279.setMinimumSize(QSize(0, 35))
        self.frame_279.setMaximumSize(QSize(16777215, 35))
        self.frame_279.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_279.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_147 = QHBoxLayout(self.frame_279)
        self.horizontalLayout_147.setSpacing(0)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.label_87 = QLabel(self.frame_279)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(0, 20))
        self.label_87.setMaximumSize(QSize(16777215, 35))
        self.label_87.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_87.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_147.addWidget(self.label_87)


        self.verticalLayout_177.addWidget(self.frame_279)

        self.frame_280 = QFrame(self.frame_278)
        self.frame_280.setObjectName(u"frame_280")
        self.frame_280.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_280.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_148 = QHBoxLayout(self.frame_280)
        self.horizontalLayout_148.setSpacing(0)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalLayout_148.setContentsMargins(0, 0, 0, 0)
        self.frame_281 = QFrame(self.frame_280)
        self.frame_281.setObjectName(u"frame_281")
        self.frame_281.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_281.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_178 = QVBoxLayout(self.frame_281)
        self.verticalLayout_178.setSpacing(0)
        self.verticalLayout_178.setObjectName(u"verticalLayout_178")
        self.verticalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.frame_282 = QFrame(self.frame_281)
        self.frame_282.setObjectName(u"frame_282")
        self.frame_282.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_282.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_149 = QHBoxLayout(self.frame_282)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_149.setContentsMargins(20, -1, 0, -1)
        self.frame_283 = QFrame(self.frame_282)
        self.frame_283.setObjectName(u"frame_283")
        sizePolicy.setHeightForWidth(self.frame_283.sizePolicy().hasHeightForWidth())
        self.frame_283.setSizePolicy(sizePolicy)
        self.frame_283.setMinimumSize(QSize(40, 0))
        self.frame_283.setMaximumSize(QSize(140, 16777215))
        self.frame_283.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_283.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_179 = QVBoxLayout(self.frame_283)
        self.verticalLayout_179.setSpacing(7)
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.verticalLayout_179.setContentsMargins(0, 0, 0, 0)
        self.label_172 = QLabel(self.frame_283)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setMinimumSize(QSize(0, 20))
        self.label_172.setMaximumSize(QSize(16777215, 18))
        self.label_172.setFont(font3)
        self.label_172.setStyleSheet(u"")

        self.verticalLayout_179.addWidget(self.label_172)


        self.horizontalLayout_149.addWidget(self.frame_283)

        self.frame_284 = QFrame(self.frame_282)
        self.frame_284.setObjectName(u"frame_284")
        sizePolicy1.setHeightForWidth(self.frame_284.sizePolicy().hasHeightForWidth())
        self.frame_284.setSizePolicy(sizePolicy1)
        self.frame_284.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_284.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_284.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_180 = QVBoxLayout(self.frame_284)
        self.verticalLayout_180.setSpacing(7)
        self.verticalLayout_180.setObjectName(u"verticalLayout_180")
        self.verticalLayout_180.setContentsMargins(0, 0, 0, 0)
        self.xTool = QLineEdit(self.frame_284)
        self.xTool.setObjectName(u"xTool")
        self.xTool.setEnabled(False)
        self.xTool.setMinimumSize(QSize(160, 20))
        self.xTool.setMaximumSize(QSize(180, 16777215))
        self.xTool.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_180.addWidget(self.xTool)


        self.horizontalLayout_149.addWidget(self.frame_284)


        self.verticalLayout_178.addWidget(self.frame_282)


        self.horizontalLayout_148.addWidget(self.frame_281)

        self.frame_285 = QFrame(self.frame_280)
        self.frame_285.setObjectName(u"frame_285")
        self.frame_285.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_285.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_181 = QVBoxLayout(self.frame_285)
        self.verticalLayout_181.setSpacing(0)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.verticalLayout_181.setContentsMargins(-1, 0, -1, 0)
        self.frame_286 = QFrame(self.frame_285)
        self.frame_286.setObjectName(u"frame_286")
        self.frame_286.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_286.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_150 = QHBoxLayout(self.frame_286)
        self.horizontalLayout_150.setSpacing(20)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(15, -1, 0, -1)
        self.frame_287 = QFrame(self.frame_286)
        self.frame_287.setObjectName(u"frame_287")
        self.frame_287.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_287.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_151 = QHBoxLayout(self.frame_287)
        self.horizontalLayout_151.setSpacing(6)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.frame_288 = QFrame(self.frame_287)
        self.frame_288.setObjectName(u"frame_288")
        sizePolicy.setHeightForWidth(self.frame_288.sizePolicy().hasHeightForWidth())
        self.frame_288.setSizePolicy(sizePolicy)
        self.frame_288.setMinimumSize(QSize(40, 0))
        self.frame_288.setMaximumSize(QSize(140, 16777215))
        self.frame_288.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_288.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_182 = QVBoxLayout(self.frame_288)
        self.verticalLayout_182.setSpacing(7)
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.verticalLayout_182.setContentsMargins(0, 0, 0, 0)
        self.label_173 = QLabel(self.frame_288)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setMinimumSize(QSize(0, 20))
        self.label_173.setMaximumSize(QSize(16777215, 18))
        self.label_173.setFont(font3)
        self.label_173.setStyleSheet(u"")

        self.verticalLayout_182.addWidget(self.label_173)


        self.horizontalLayout_151.addWidget(self.frame_288)

        self.frame_289 = QFrame(self.frame_287)
        self.frame_289.setObjectName(u"frame_289")
        sizePolicy1.setHeightForWidth(self.frame_289.sizePolicy().hasHeightForWidth())
        self.frame_289.setSizePolicy(sizePolicy1)
        self.frame_289.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_289.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_289.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_183 = QVBoxLayout(self.frame_289)
        self.verticalLayout_183.setSpacing(7)
        self.verticalLayout_183.setObjectName(u"verticalLayout_183")
        self.verticalLayout_183.setContentsMargins(0, 0, 0, 0)
        self.yTool = QLineEdit(self.frame_289)
        self.yTool.setObjectName(u"yTool")
        self.yTool.setEnabled(False)
        self.yTool.setMinimumSize(QSize(160, 20))
        self.yTool.setMaximumSize(QSize(189, 16777215))
        self.yTool.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_183.addWidget(self.yTool)


        self.horizontalLayout_151.addWidget(self.frame_289)


        self.horizontalLayout_150.addWidget(self.frame_287)


        self.verticalLayout_181.addWidget(self.frame_286)


        self.horizontalLayout_148.addWidget(self.frame_285)


        self.verticalLayout_177.addWidget(self.frame_280)


        self.verticalLayout_176.addWidget(self.frame_278)


        self.verticalLayout_167.addWidget(self.frame_277)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_23)

        self.frame_290 = QFrame(self.frame_263)
        self.frame_290.setObjectName(u"frame_290")
        self.frame_290.setMinimumSize(QSize(0, 0))
        self.frame_290.setMaximumSize(QSize(16777215, 100))
        self.frame_290.setStyleSheet(u"")
        self.frame_290.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_290.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_184 = QVBoxLayout(self.frame_290)
        self.verticalLayout_184.setSpacing(0)
        self.verticalLayout_184.setObjectName(u"verticalLayout_184")
        self.verticalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.frame_291 = QFrame(self.frame_290)
        self.frame_291.setObjectName(u"frame_291")
        self.frame_291.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_291.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_185 = QVBoxLayout(self.frame_291)
        self.verticalLayout_185.setSpacing(0)
        self.verticalLayout_185.setObjectName(u"verticalLayout_185")
        self.verticalLayout_185.setContentsMargins(0, 0, 0, -1)
        self.frame_292 = QFrame(self.frame_291)
        self.frame_292.setObjectName(u"frame_292")
        self.frame_292.setMinimumSize(QSize(0, 35))
        self.frame_292.setMaximumSize(QSize(16777215, 35))
        self.frame_292.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_292.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_152 = QHBoxLayout(self.frame_292)
        self.horizontalLayout_152.setSpacing(0)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalLayout_152.setContentsMargins(0, 0, 0, 0)
        self.label_88 = QLabel(self.frame_292)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(0, 35))
        self.label_88.setMaximumSize(QSize(16777215, 35))
        self.label_88.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_88.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_152.addWidget(self.label_88)


        self.verticalLayout_185.addWidget(self.frame_292)

        self.frame_293 = QFrame(self.frame_291)
        self.frame_293.setObjectName(u"frame_293")
        self.frame_293.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_293.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_153 = QHBoxLayout(self.frame_293)
        self.horizontalLayout_153.setSpacing(0)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.frame_294 = QFrame(self.frame_293)
        self.frame_294.setObjectName(u"frame_294")
        self.frame_294.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_294.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_186 = QVBoxLayout(self.frame_294)
        self.verticalLayout_186.setSpacing(0)
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.verticalLayout_186.setContentsMargins(0, 0, 0, 0)
        self.frame_295 = QFrame(self.frame_294)
        self.frame_295.setObjectName(u"frame_295")
        self.frame_295.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_295.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_154 = QHBoxLayout(self.frame_295)
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(20, -1, 0, -1)
        self.frame_296 = QFrame(self.frame_295)
        self.frame_296.setObjectName(u"frame_296")
        sizePolicy1.setHeightForWidth(self.frame_296.sizePolicy().hasHeightForWidth())
        self.frame_296.setSizePolicy(sizePolicy1)
        self.frame_296.setMaximumSize(QSize(220, 16777215))
        self.frame_296.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_296.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_187 = QVBoxLayout(self.frame_296)
        self.verticalLayout_187.setSpacing(7)
        self.verticalLayout_187.setObjectName(u"verticalLayout_187")
        self.verticalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.label_159 = QLabel(self.frame_296)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setMinimumSize(QSize(0, 20))
        self.label_159.setMaximumSize(QSize(16777215, 18))
        self.label_159.setFont(font3)
        self.label_159.setStyleSheet(u"")

        self.verticalLayout_187.addWidget(self.label_159)


        self.horizontalLayout_154.addWidget(self.frame_296)

        self.frame_297 = QFrame(self.frame_295)
        self.frame_297.setObjectName(u"frame_297")
        sizePolicy.setHeightForWidth(self.frame_297.sizePolicy().hasHeightForWidth())
        self.frame_297.setSizePolicy(sizePolicy)
        self.frame_297.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.frame_297.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_297.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_297.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_188 = QVBoxLayout(self.frame_297)
        self.verticalLayout_188.setSpacing(7)
        self.verticalLayout_188.setObjectName(u"verticalLayout_188")
        self.verticalLayout_188.setContentsMargins(0, 0, 0, 0)
        self.overWorkpiece = QLineEdit(self.frame_297)
        self.overWorkpiece.setObjectName(u"overWorkpiece")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.overWorkpiece.sizePolicy().hasHeightForWidth())
        self.overWorkpiece.setSizePolicy(sizePolicy3)
        self.overWorkpiece.setMinimumSize(QSize(160, 20))
        self.overWorkpiece.setMaximumSize(QSize(180, 16777215))
        self.overWorkpiece.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_188.addWidget(self.overWorkpiece)


        self.horizontalLayout_154.addWidget(self.frame_297)


        self.verticalLayout_186.addWidget(self.frame_295)


        self.horizontalLayout_153.addWidget(self.frame_294)

        self.frame_298 = QFrame(self.frame_293)
        self.frame_298.setObjectName(u"frame_298")
        self.frame_298.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_298.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_189 = QVBoxLayout(self.frame_298)
        self.verticalLayout_189.setSpacing(0)
        self.verticalLayout_189.setObjectName(u"verticalLayout_189")
        self.verticalLayout_189.setContentsMargins(-1, 0, -1, 0)
        self.frame_299 = QFrame(self.frame_298)
        self.frame_299.setObjectName(u"frame_299")
        self.frame_299.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_299.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_155 = QHBoxLayout(self.frame_299)
        self.horizontalLayout_155.setSpacing(20)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(15, -1, 0, -1)
        self.frame_300 = QFrame(self.frame_299)
        self.frame_300.setObjectName(u"frame_300")
        self.frame_300.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_300.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_156 = QHBoxLayout(self.frame_300)
        self.horizontalLayout_156.setSpacing(6)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.frame_301 = QFrame(self.frame_300)
        self.frame_301.setObjectName(u"frame_301")
        sizePolicy1.setHeightForWidth(self.frame_301.sizePolicy().hasHeightForWidth())
        self.frame_301.setSizePolicy(sizePolicy1)
        self.frame_301.setMaximumSize(QSize(170, 16777215))
        self.frame_301.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_301.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_190 = QVBoxLayout(self.frame_301)
        self.verticalLayout_190.setSpacing(7)
        self.verticalLayout_190.setObjectName(u"verticalLayout_190")
        self.verticalLayout_190.setContentsMargins(0, 0, 0, 0)
        self.label_160 = QLabel(self.frame_301)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setMinimumSize(QSize(220, 20))
        self.label_160.setMaximumSize(QSize(16777215, 18))
        self.label_160.setFont(font3)
        self.label_160.setStyleSheet(u"")

        self.verticalLayout_190.addWidget(self.label_160)


        self.horizontalLayout_156.addWidget(self.frame_301)

        self.frame_302 = QFrame(self.frame_300)
        self.frame_302.setObjectName(u"frame_302")
        sizePolicy1.setHeightForWidth(self.frame_302.sizePolicy().hasHeightForWidth())
        self.frame_302.setSizePolicy(sizePolicy1)
        self.frame_302.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_302.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_302.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_191 = QVBoxLayout(self.frame_302)
        self.verticalLayout_191.setSpacing(7)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.verticalLayout_191.setContentsMargins(0, 0, 0, 0)
        self.fromTool = QLineEdit(self.frame_302)
        self.fromTool.setObjectName(u"fromTool")
        self.fromTool.setMinimumSize(QSize(160, 20))
        self.fromTool.setMaximumSize(QSize(189, 16777215))
        self.fromTool.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_191.addWidget(self.fromTool)


        self.horizontalLayout_156.addWidget(self.frame_302)


        self.horizontalLayout_155.addWidget(self.frame_300)


        self.verticalLayout_189.addWidget(self.frame_299)


        self.horizontalLayout_153.addWidget(self.frame_298)


        self.verticalLayout_185.addWidget(self.frame_293)


        self.verticalLayout_184.addWidget(self.frame_291)


        self.verticalLayout_167.addWidget(self.frame_290)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_24)

        self.frame_303 = QFrame(self.frame_263)
        self.frame_303.setObjectName(u"frame_303")
        self.frame_303.setMinimumSize(QSize(0, 0))
        self.frame_303.setMaximumSize(QSize(16777215, 100))
        self.frame_303.setStyleSheet(u"")
        self.frame_303.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_303.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_192 = QVBoxLayout(self.frame_303)
        self.verticalLayout_192.setSpacing(0)
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.verticalLayout_192.setContentsMargins(0, 0, 0, 0)
        self.frame_304 = QFrame(self.frame_303)
        self.frame_304.setObjectName(u"frame_304")
        self.frame_304.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_304.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_193 = QVBoxLayout(self.frame_304)
        self.verticalLayout_193.setSpacing(0)
        self.verticalLayout_193.setObjectName(u"verticalLayout_193")
        self.verticalLayout_193.setContentsMargins(0, 0, 0, -1)
        self.frame_305 = QFrame(self.frame_304)
        self.frame_305.setObjectName(u"frame_305")
        self.frame_305.setMinimumSize(QSize(0, 35))
        self.frame_305.setMaximumSize(QSize(16777215, 35))
        self.frame_305.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_305.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_157 = QHBoxLayout(self.frame_305)
        self.horizontalLayout_157.setSpacing(0)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.label_89 = QLabel(self.frame_305)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(0, 35))
        self.label_89.setMaximumSize(QSize(16777215, 35))
        self.label_89.setStyleSheet(u"QLabel {\n"
"    font-size: 20px; /* Tamanho da fonte */\n"
"	font-family: \"Yu Gothic UI Semibold\"; /* Fam\u00edlia da fonte */\n"
"}\n"
"")
        self.label_89.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_157.addWidget(self.label_89)


        self.verticalLayout_193.addWidget(self.frame_305)

        self.frame_306 = QFrame(self.frame_304)
        self.frame_306.setObjectName(u"frame_306")
        self.frame_306.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_306.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_158 = QHBoxLayout(self.frame_306)
        self.horizontalLayout_158.setSpacing(0)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.horizontalLayout_158.setContentsMargins(0, 0, 0, 0)
        self.frame_307 = QFrame(self.frame_306)
        self.frame_307.setObjectName(u"frame_307")
        self.frame_307.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_307.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_194 = QVBoxLayout(self.frame_307)
        self.verticalLayout_194.setSpacing(0)
        self.verticalLayout_194.setObjectName(u"verticalLayout_194")
        self.verticalLayout_194.setContentsMargins(0, 0, 0, 0)
        self.frame_308 = QFrame(self.frame_307)
        self.frame_308.setObjectName(u"frame_308")
        self.frame_308.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_308.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_159 = QHBoxLayout(self.frame_308)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(20, -1, 0, -1)
        self.frame_309 = QFrame(self.frame_308)
        self.frame_309.setObjectName(u"frame_309")
        sizePolicy1.setHeightForWidth(self.frame_309.sizePolicy().hasHeightForWidth())
        self.frame_309.setSizePolicy(sizePolicy1)
        self.frame_309.setMaximumSize(QSize(140, 16777215))
        self.frame_309.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_309.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_195 = QVBoxLayout(self.frame_309)
        self.verticalLayout_195.setSpacing(7)
        self.verticalLayout_195.setObjectName(u"verticalLayout_195")
        self.verticalLayout_195.setContentsMargins(0, 0, 0, 0)
        self.label_174 = QLabel(self.frame_309)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setMinimumSize(QSize(0, 20))
        self.label_174.setMaximumSize(QSize(16777215, 18))
        self.label_174.setFont(font3)
        self.label_174.setStyleSheet(u"")

        self.verticalLayout_195.addWidget(self.label_174)


        self.horizontalLayout_159.addWidget(self.frame_309)

        self.frame_310 = QFrame(self.frame_308)
        self.frame_310.setObjectName(u"frame_310")
        sizePolicy1.setHeightForWidth(self.frame_310.sizePolicy().hasHeightForWidth())
        self.frame_310.setSizePolicy(sizePolicy1)
        self.frame_310.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_310.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_310.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_196 = QVBoxLayout(self.frame_310)
        self.verticalLayout_196.setSpacing(7)
        self.verticalLayout_196.setObjectName(u"verticalLayout_196")
        self.verticalLayout_196.setContentsMargins(0, 0, 0, 0)
        self.feed = QLineEdit(self.frame_310)
        self.feed.setObjectName(u"feed")
        self.feed.setMinimumSize(QSize(160, 20))
        self.feed.setMaximumSize(QSize(180, 16777215))
        self.feed.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_196.addWidget(self.feed)


        self.horizontalLayout_159.addWidget(self.frame_310)


        self.verticalLayout_194.addWidget(self.frame_308)


        self.horizontalLayout_158.addWidget(self.frame_307)

        self.frame_311 = QFrame(self.frame_306)
        self.frame_311.setObjectName(u"frame_311")
        self.frame_311.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_311.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_197 = QVBoxLayout(self.frame_311)
        self.verticalLayout_197.setSpacing(0)
        self.verticalLayout_197.setObjectName(u"verticalLayout_197")
        self.verticalLayout_197.setContentsMargins(-1, 0, -1, 0)
        self.frame_312 = QFrame(self.frame_311)
        self.frame_312.setObjectName(u"frame_312")
        self.frame_312.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_312.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_160 = QHBoxLayout(self.frame_312)
        self.horizontalLayout_160.setSpacing(20)
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalLayout_160.setContentsMargins(15, -1, 0, -1)
        self.frame_313 = QFrame(self.frame_312)
        self.frame_313.setObjectName(u"frame_313")
        self.frame_313.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_313.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_161 = QHBoxLayout(self.frame_313)
        self.horizontalLayout_161.setSpacing(6)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.horizontalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.frame_314 = QFrame(self.frame_313)
        self.frame_314.setObjectName(u"frame_314")
        sizePolicy1.setHeightForWidth(self.frame_314.sizePolicy().hasHeightForWidth())
        self.frame_314.setSizePolicy(sizePolicy1)
        self.frame_314.setMaximumSize(QSize(140, 16777215))
        self.frame_314.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_314.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_198 = QVBoxLayout(self.frame_314)
        self.verticalLayout_198.setSpacing(7)
        self.verticalLayout_198.setObjectName(u"verticalLayout_198")
        self.verticalLayout_198.setContentsMargins(0, 0, 0, 0)
        self.label_90 = QLabel(self.frame_314)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMinimumSize(QSize(0, 20))

        self.verticalLayout_198.addWidget(self.label_90)


        self.horizontalLayout_161.addWidget(self.frame_314)

        self.frame_315 = QFrame(self.frame_313)
        self.frame_315.setObjectName(u"frame_315")
        sizePolicy1.setHeightForWidth(self.frame_315.sizePolicy().hasHeightForWidth())
        self.frame_315.setSizePolicy(sizePolicy1)
        self.frame_315.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frame_315.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_315.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_199 = QVBoxLayout(self.frame_315)
        self.verticalLayout_199.setSpacing(7)
        self.verticalLayout_199.setObjectName(u"verticalLayout_199")
        self.verticalLayout_199.setContentsMargins(0, 0, 0, 0)
        self.timePeriod = QLineEdit(self.frame_315)
        self.timePeriod.setObjectName(u"timePeriod")
        self.timePeriod.setMinimumSize(QSize(160, 20))
        self.timePeriod.setMaximumSize(QSize(180, 16777215))
        self.timePeriod.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_199.addWidget(self.timePeriod)


        self.horizontalLayout_161.addWidget(self.frame_315)


        self.horizontalLayout_160.addWidget(self.frame_313)


        self.verticalLayout_197.addWidget(self.frame_312)


        self.horizontalLayout_158.addWidget(self.frame_311)


        self.verticalLayout_193.addWidget(self.frame_306)


        self.verticalLayout_192.addWidget(self.frame_304)


        self.verticalLayout_167.addWidget(self.frame_303)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_25)

        self.assemblyWarning = QLabel(self.frame_263)
        self.assemblyWarning.setObjectName(u"assemblyWarning")
        self.assemblyWarning.setFont(font4)
        self.assemblyWarning.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.assemblyWarning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.assemblyWarning.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_167.addWidget(self.assemblyWarning)

        self.verticalSpacer_26 = QSpacerItem(20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_167.addItem(self.verticalSpacer_26)


        self.verticalLayout_200.addWidget(self.frame_263)

        self.tabWidget.addTab(self.assemblyTab, "")

        self.verticalLayout_84.addWidget(self.tabWidget)


        self.verticalLayout_77.addWidget(self.frame_127)

        self.frame_136 = QFrame(self.frame_96)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setMinimumSize(QSize(0, 60))
        self.frame_136.setMaximumSize(QSize(16777215, 60))
        self.frame_136.setStyleSheet(u"#frame_136{\n"
"background-color: #b6b6b6;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"")
        self.frame_136.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_136.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_163 = QHBoxLayout(self.frame_136)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.button_create_geometry_back = QPushButton(self.frame_136)
        self.button_create_geometry_back.setObjectName(u"button_create_geometry_back")
        self.button_create_geometry_back.setMinimumSize(QSize(100, 38))
        self.button_create_geometry_back.setMaximumSize(QSize(100, 38))
        self.button_create_geometry_back.setStyleSheet(u"")

        self.horizontalLayout_163.addWidget(self.button_create_geometry_back)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_163.addItem(self.horizontalSpacer_7)

        self.button_create_geometry_apply = QPushButton(self.frame_136)
        self.button_create_geometry_apply.setObjectName(u"button_create_geometry_apply")
        self.button_create_geometry_apply.setEnabled(True)
        self.button_create_geometry_apply.setMinimumSize(QSize(100, 38))
        self.button_create_geometry_apply.setMaximumSize(QSize(100, 38))
        self.button_create_geometry_apply.setStyleSheet(u"")

        self.horizontalLayout_163.addWidget(self.button_create_geometry_apply)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_163.addItem(self.horizontalSpacer_6)

        self.button_create_geometry_next = QPushButton(self.frame_136)
        self.button_create_geometry_next.setObjectName(u"button_create_geometry_next")
        self.button_create_geometry_next.setEnabled(False)
        self.button_create_geometry_next.setMinimumSize(QSize(100, 38))
        self.button_create_geometry_next.setMaximumSize(QSize(100, 38))
        self.button_create_geometry_next.setStyleSheet(u"")

        self.horizontalLayout_163.addWidget(self.button_create_geometry_next)


        self.verticalLayout_77.addWidget(self.frame_136)


        self.horizontalLayout_113.addWidget(self.frame_96)

        self.frame_262 = QFrame(self.frame_95)
        self.frame_262.setObjectName(u"frame_262")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_262.sizePolicy().hasHeightForWidth())
        self.frame_262.setSizePolicy(sizePolicy4)
        self.frame_262.setStyleSheet(u"")
        self.frame_262.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_262.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_162 = QHBoxLayout(self.frame_262)
        self.horizontalLayout_162.setSpacing(0)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalLayout_162.setContentsMargins(9, 0, -1, 1)
        self.plot_geometry_frame = QFrame(self.frame_262)
        self.plot_geometry_frame.setObjectName(u"plot_geometry_frame")
        self.plot_geometry_frame.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.plot_geometry_frame.sizePolicy().hasHeightForWidth())
        self.plot_geometry_frame.setSizePolicy(sizePolicy4)
        self.plot_geometry_frame.setMinimumSize(QSize(0, 600))
        self.plot_geometry_frame.setStyleSheet(u"QFrame {\n"
"     border-radius: 0 px; \n"
"	 border: 0px solid #3498db;\n"
"}")
        self.plot_geometry_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.plot_geometry_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.plot_geometry_frame)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")

        self.horizontalLayout_162.addWidget(self.plot_geometry_frame)


        self.horizontalLayout_113.addWidget(self.frame_262)


        self.verticalLayout_89.addWidget(self.frame_95)

        self.label_83 = QLabel(self.geometryPage)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_89.addWidget(self.label_83)

        self.pages.addWidget(self.geometryPage)
        self.page_conditions = QWidget()
        self.page_conditions.setObjectName(u"page_conditions")
        self.page_conditions.setStyleSheet(u"/* QLabel and QLineEdit*/\n"
"#label_input {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}\n"
"\n"
"QLineEdit {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}\n"
"\n"
"/* QPushButton*/\n"
"#button_input_file {\n"
"background-color: rgb(248, 248, 248);\n"
"border-radius: 10px;}\n"
"\n"
"#button_conditions_next_page, #button_conditions_back, #button_newCondition {\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_conditions_next_page:hover,  #button_conditions_back:hover, #button_newCondition:hover, #button_input_file:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_conditions_next_page:pressed, #button_conditions_back:pressed,  #button_newCondition:pressed, #b"
                        "utton_input_file:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_13 = QVBoxLayout(self.page_conditions)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page_conditions)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 70))
        self.frame_9.setMaximumSize(QSize(16777215, 70))
        self.frame_9.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_interface_2 = QLabel(self.frame_9)
        self.icon_interface_2.setObjectName(u"icon_interface_2")
        self.icon_interface_2.setMinimumSize(QSize(50, 50))
        self.icon_interface_2.setMaximumSize(QSize(50, 50))
        self.icon_interface_2.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.icon_interface_2)

        self.interface_name_2 = QLabel(self.frame_9)
        self.interface_name_2.setObjectName(u"interface_name_2")
        self.interface_name_2.setFont(font)
        self.interface_name_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.interface_name_2)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.page_conditions)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_10.setLineWidth(0)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(850, 500))
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 210))
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 30))
        self.frame_19.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.comboBox_condition = QComboBox(self.frame_19)
        self.comboBox_condition.setObjectName(u"comboBox_condition")
        self.comboBox_condition.setMinimumSize(QSize(0, 20))
        self.comboBox_condition.setMaximumSize(QSize(150, 16777215))
        self.comboBox_condition.setIconSize(QSize(10, 10))

        self.verticalLayout_11.addWidget(self.comboBox_condition)


        self.verticalLayout_9.addWidget(self.frame_19)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 30))
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(150, 0))
        self.label_8.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_6.addWidget(self.label_8)

        self.lineEdit_velocity = QLineEdit(self.frame_14)
        self.lineEdit_velocity.setObjectName(u"lineEdit_velocity")
        self.lineEdit_velocity.setMinimumSize(QSize(0, 20))
        self.lineEdit_velocity.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_velocity.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lineEdit_velocity)

        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(35, 22))
        self.label_5.setMaximumSize(QSize(35, 22))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_9.addWidget(self.frame_14)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 30))
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(150, 0))
        self.label_11.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_9.addWidget(self.label_11)

        self.lineEdit_deepCuth = QLineEdit(self.frame_18)
        self.lineEdit_deepCuth.setObjectName(u"lineEdit_deepCuth")
        self.lineEdit_deepCuth.setMinimumSize(QSize(0, 20))
        self.lineEdit_deepCuth.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_deepCuth.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lineEdit_deepCuth)

        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(35, 22))
        self.label_7.setMaximumSize(QSize(35, 22))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_7)


        self.verticalLayout_9.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 30))
        self.frame_17.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 0))
        self.label_9.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_8.addWidget(self.label_9)

        self.lineEdit_rakeAngle = QLineEdit(self.frame_17)
        self.lineEdit_rakeAngle.setObjectName(u"lineEdit_rakeAngle")
        self.lineEdit_rakeAngle.setMinimumSize(QSize(0, 20))
        self.lineEdit_rakeAngle.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_rakeAngle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lineEdit_rakeAngle)

        self.label_12 = QLabel(self.frame_17)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(35, 22))
        self.label_12.setMaximumSize(QSize(35, 22))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_12)


        self.verticalLayout_9.addWidget(self.frame_17)

        self.frame_temperature_path = QFrame(self.frame_13)
        self.frame_temperature_path.setObjectName(u"frame_temperature_path")
        self.frame_temperature_path.setMinimumSize(QSize(0, 30))
        self.frame_temperature_path.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_temperature_path.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_temperature_path)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_13 = QLabel(self.frame_temperature_path)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 0))
        self.label_13.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_10.addWidget(self.label_13)

        self.lineEdit_tempPath = QLineEdit(self.frame_temperature_path)
        self.lineEdit_tempPath.setObjectName(u"lineEdit_tempPath")
        self.lineEdit_tempPath.setMinimumSize(QSize(0, 20))
        self.lineEdit_tempPath.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_tempPath.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_tempPath)

        self.horizontalSpacer = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addWidget(self.frame_temperature_path)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 30))
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.label_10 = QLabel(self.frame_15)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 0))
        self.label_10.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_7.addWidget(self.label_10)

        self.label_input = QLabel(self.frame_15)
        self.label_input.setObjectName(u"label_input")
        self.label_input.setMinimumSize(QSize(0, 20))
        self.label_input.setMaximumSize(QSize(16777215, 20))
        self.label_input.setStyleSheet(u"")
        self.label_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_input)

        self.horizontalSpacer_2 = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.button_input_file = QPushButton(self.frame_15)
        self.button_input_file.setObjectName(u"button_input_file")
        self.button_input_file.setMinimumSize(QSize(25, 25))
        self.button_input_file.setMaximumSize(QSize(25, 25))
        self.button_input_file.setIcon(icon1)
        self.button_input_file.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.button_input_file)


        self.verticalLayout_9.addWidget(self.frame_15)


        self.verticalLayout_10.addWidget(self.frame_13)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_8)

        self.frame_80 = QFrame(self.frame_12)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(0, 0))
        self.frame_80.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_80)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.frame_88 = QFrame(self.frame_80)
        self.frame_88.setObjectName(u"frame_88")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.frame_88.setFont(font5)
        self.frame_88.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_88)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_88)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font5)

        self.verticalLayout_63.addWidget(self.label_30)


        self.verticalLayout_62.addWidget(self.frame_88)

        self.frame_fc_result = QFrame(self.frame_80)
        self.frame_fc_result.setObjectName(u"frame_fc_result")
        self.frame_fc_result.setMinimumSize(QSize(0, 30))
        self.frame_fc_result.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_fc_result.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_fc_result)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(-1, 0, -1, 0)
        self.label_20 = QLabel(self.frame_fc_result)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(150, 0))
        self.label_20.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_102.addWidget(self.label_20)

        self.lineEdit_cutting_force = QLineEdit(self.frame_fc_result)
        self.lineEdit_cutting_force.setObjectName(u"lineEdit_cutting_force")
        self.lineEdit_cutting_force.setMinimumSize(QSize(0, 20))
        self.lineEdit_cutting_force.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_cutting_force.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_102.addWidget(self.lineEdit_cutting_force)

        self.label_21 = QLabel(self.frame_fc_result)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(35, 22))
        self.label_21.setMaximumSize(QSize(35, 22))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_102.addWidget(self.label_21)


        self.verticalLayout_62.addWidget(self.frame_fc_result)

        self.frame_fn_result = QFrame(self.frame_80)
        self.frame_fn_result.setObjectName(u"frame_fn_result")
        self.frame_fn_result.setMinimumSize(QSize(0, 30))
        self.frame_fn_result.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_fn_result.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_fn_result)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(-1, 0, -1, 0)
        self.label_24 = QLabel(self.frame_fn_result)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(150, 0))
        self.label_24.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_104.addWidget(self.label_24)

        self.lineEdit_normal_force = QLineEdit(self.frame_fn_result)
        self.lineEdit_normal_force.setObjectName(u"lineEdit_normal_force")
        self.lineEdit_normal_force.setMinimumSize(QSize(0, 20))
        self.lineEdit_normal_force.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_normal_force.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_104.addWidget(self.lineEdit_normal_force)

        self.label_25 = QLabel(self.frame_fn_result)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(35, 22))
        self.label_25.setMaximumSize(QSize(35, 22))
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_104.addWidget(self.label_25)


        self.verticalLayout_62.addWidget(self.frame_fn_result)

        self.frame_temperature_result = QFrame(self.frame_80)
        self.frame_temperature_result.setObjectName(u"frame_temperature_result")
        self.frame_temperature_result.setMinimumSize(QSize(0, 30))
        self.frame_temperature_result.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_temperature_result.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_temperature_result)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(-1, 0, -1, 0)
        self.label_22 = QLabel(self.frame_temperature_result)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(150, 0))
        self.label_22.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_103.addWidget(self.label_22)

        self.lineEdit_temperature = QLineEdit(self.frame_temperature_result)
        self.lineEdit_temperature.setObjectName(u"lineEdit_temperature")
        self.lineEdit_temperature.setMinimumSize(QSize(0, 20))
        self.lineEdit_temperature.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_temperature.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_103.addWidget(self.lineEdit_temperature)

        self.label_23 = QLabel(self.frame_temperature_result)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(35, 22))
        self.label_23.setMaximumSize(QSize(35, 22))
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_103.addWidget(self.label_23)


        self.verticalLayout_62.addWidget(self.frame_temperature_result)

        self.frame_csr_result = QFrame(self.frame_80)
        self.frame_csr_result.setObjectName(u"frame_csr_result")
        self.frame_csr_result.setMinimumSize(QSize(0, 30))
        self.frame_csr_result.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_csr_result.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_csr_result)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalLayout_107.setContentsMargins(-1, 0, -1, 0)
        self.label_28 = QLabel(self.frame_csr_result)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(150, 0))
        self.label_28.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_107.addWidget(self.label_28)

        self.lineEdit_CSR = QLineEdit(self.frame_csr_result)
        self.lineEdit_CSR.setObjectName(u"lineEdit_CSR")
        self.lineEdit_CSR.setMinimumSize(QSize(0, 20))
        self.lineEdit_CSR.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_CSR.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_107.addWidget(self.lineEdit_CSR)

        self.label_29 = QLabel(self.frame_csr_result)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(35, 22))
        self.label_29.setMaximumSize(QSize(35, 22))
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_107.addWidget(self.label_29)


        self.verticalLayout_62.addWidget(self.frame_csr_result)

        self.frame_ccr_result = QFrame(self.frame_80)
        self.frame_ccr_result.setObjectName(u"frame_ccr_result")
        self.frame_ccr_result.setMinimumSize(QSize(0, 30))
        self.frame_ccr_result.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_ccr_result.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_ccr_result)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(-1, 0, -1, 0)
        self.label_26 = QLabel(self.frame_ccr_result)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(150, 0))
        self.label_26.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_106.addWidget(self.label_26)

        self.lineEdit_CCR = QLineEdit(self.frame_ccr_result)
        self.lineEdit_CCR.setObjectName(u"lineEdit_CCR")
        self.lineEdit_CCR.setMinimumSize(QSize(0, 20))
        self.lineEdit_CCR.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_CCR.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_106.addWidget(self.lineEdit_CCR)

        self.label_27 = QLabel(self.frame_ccr_result)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(35, 22))
        self.label_27.setMaximumSize(QSize(35, 22))
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_106.addWidget(self.label_27)


        self.verticalLayout_62.addWidget(self.frame_ccr_result)


        self.verticalLayout_10.addWidget(self.frame_80)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_11)

        self.frame_21 = QFrame(self.frame_12)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 60))
        self.frame_21.setMaximumSize(QSize(16777215, 60))
        self.frame_21.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setSpacing(30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, -1, 9, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.button_conditions_back = QPushButton(self.frame_21)
        self.button_conditions_back.setObjectName(u"button_conditions_back")
        self.button_conditions_back.setMinimumSize(QSize(90, 38))
        self.button_conditions_back.setMaximumSize(QSize(90, 38))

        self.horizontalLayout_12.addWidget(self.button_conditions_back)

        self.button_newCondition = QPushButton(self.frame_21)
        self.button_newCondition.setObjectName(u"button_newCondition")
        self.button_newCondition.setMinimumSize(QSize(90, 38))
        self.button_newCondition.setMaximumSize(QSize(90, 38))

        self.horizontalLayout_12.addWidget(self.button_newCondition)

        self.button_conditions_next_page = QPushButton(self.frame_21)
        self.button_conditions_next_page.setObjectName(u"button_conditions_next_page")
        self.button_conditions_next_page.setMinimumSize(QSize(90, 38))
        self.button_conditions_next_page.setMaximumSize(QSize(90, 38))

        self.horizontalLayout_12.addWidget(self.button_conditions_next_page)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_10.addWidget(self.frame_21)


        self.horizontalLayout_66.addWidget(self.frame_12)


        self.verticalLayout_13.addWidget(self.frame_10)

        self.frame_16 = QFrame(self.page_conditions)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 20))
        self.frame_16.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_16.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6)


        self.verticalLayout_13.addWidget(self.frame_16)

        self.pages.addWidget(self.page_conditions)
        self.page_parameter_selection = QWidget()
        self.page_parameter_selection.setObjectName(u"page_parameter_selection")
        self.page_parameter_selection.setStyleSheet(u"/* QPushButton*/\n"
"#button_parameter_selection_next_page, #button_parameter_selection_back {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_parameter_selection_next_page:hover, #button_parameter_selection_back:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_parameter_selection_next_page:pressed, #button_parameter_selection_back:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"")
        self.verticalLayout_27 = QVBoxLayout(self.page_parameter_selection)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.page_parameter_selection)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 70))
        self.frame_41.setMaximumSize(QSize(16777215, 70))
        self.frame_41.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_41.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.icon_interface_5 = QLabel(self.frame_41)
        self.icon_interface_5.setObjectName(u"icon_interface_5")
        self.icon_interface_5.setMinimumSize(QSize(50, 50))
        self.icon_interface_5.setMaximumSize(QSize(50, 50))
        self.icon_interface_5.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_5.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.icon_interface_5)

        self.interface_name_5 = QLabel(self.frame_41)
        self.interface_name_5.setObjectName(u"interface_name_5")
        self.interface_name_5.setFont(font)
        self.interface_name_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.interface_name_5)


        self.verticalLayout_27.addWidget(self.frame_41)

        self.frame_35 = QFrame(self.page_parameter_selection)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_35.setLineWidth(0)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(800, 16777215))
        self.frame_36.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_36)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_4)

        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_37)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 40))
        self.frame_39.setMaximumSize(QSize(16777215, 40))
        self.frame_39.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_39)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.comboBox_material = QComboBox(self.frame_39)
        self.comboBox_material.setObjectName(u"comboBox_material")
        self.comboBox_material.setMinimumSize(QSize(0, 20))
        self.comboBox_material.setMaximumSize(QSize(150, 16777215))
        self.comboBox_material.setIconSize(QSize(10, 10))

        self.verticalLayout_26.addWidget(self.comboBox_material)


        self.verticalLayout_38.addWidget(self.frame_39)

        self.frame_material_model = QFrame(self.frame_37)
        self.frame_material_model.setObjectName(u"frame_material_model")
        self.frame_material_model.setEnabled(True)
        self.frame_material_model.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_material_model.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_material_model)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_material_model)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_43)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(10, -1, -1, -1)
        self.label_3 = QLabel(self.frame_43)
        self.label_3.setObjectName(u"label_3")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_3.setFont(font6)

        self.verticalLayout_29.addWidget(self.label_3)


        self.verticalLayout_28.addWidget(self.frame_43)

        self.frame_plastic_properties = QFrame(self.frame_material_model)
        self.frame_plastic_properties.setObjectName(u"frame_plastic_properties")
        self.frame_plastic_properties.setEnabled(True)
        self.frame_plastic_properties.setStyleSheet(u"/* QLabel*/\n"
"QLabel{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}")
        self.frame_plastic_properties.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_plastic_properties.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_plastic_properties)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, -1)
        self.frame_46 = QFrame(self.frame_plastic_properties)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_46)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_46)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.checkBox_param_A = QCheckBox(self.frame_49)
        self.checkBox_param_A.setObjectName(u"checkBox_param_A")
        self.checkBox_param_A.setMinimumSize(QSize(0, 0))
        self.checkBox_param_A.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_21.addWidget(self.checkBox_param_A)

        self.label_param_A = QLabel(self.frame_49)
        self.label_param_A.setObjectName(u"label_param_A")
        self.label_param_A.setMinimumSize(QSize(50, 20))
        self.label_param_A.setMaximumSize(QSize(50, 20))
        self.label_param_A.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_param_A)


        self.verticalLayout_30.addWidget(self.frame_49)

        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.checkBox_param_B = QCheckBox(self.frame_47)
        self.checkBox_param_B.setObjectName(u"checkBox_param_B")
        self.checkBox_param_B.setMinimumSize(QSize(0, 0))
        self.checkBox_param_B.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_19.addWidget(self.checkBox_param_B)

        self.label_param_B = QLabel(self.frame_47)
        self.label_param_B.setObjectName(u"label_param_B")
        self.label_param_B.setMinimumSize(QSize(50, 20))
        self.label_param_B.setMaximumSize(QSize(50, 20))
        self.label_param_B.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_param_B)


        self.verticalLayout_30.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.checkBox_param_n = QCheckBox(self.frame_48)
        self.checkBox_param_n.setObjectName(u"checkBox_param_n")
        self.checkBox_param_n.setMinimumSize(QSize(0, 0))
        self.checkBox_param_n.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_20.addWidget(self.checkBox_param_n)

        self.label_param_n = QLabel(self.frame_48)
        self.label_param_n.setObjectName(u"label_param_n")
        self.label_param_n.setMinimumSize(QSize(50, 20))
        self.label_param_n.setMaximumSize(QSize(50, 20))
        self.label_param_n.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_param_n)


        self.verticalLayout_30.addWidget(self.frame_48)


        self.horizontalLayout_18.addWidget(self.frame_46)

        self.frame_50 = QFrame(self.frame_plastic_properties)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_50)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.checkBox_param_C1 = QCheckBox(self.frame_51)
        self.checkBox_param_C1.setObjectName(u"checkBox_param_C1")
        self.checkBox_param_C1.setMinimumSize(QSize(0, 0))
        self.checkBox_param_C1.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_24.addWidget(self.checkBox_param_C1)

        self.label_param_C1 = QLabel(self.frame_51)
        self.label_param_C1.setObjectName(u"label_param_C1")
        self.label_param_C1.setMinimumSize(QSize(50, 20))
        self.label_param_C1.setMaximumSize(QSize(50, 20))
        self.label_param_C1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_param_C1)


        self.verticalLayout_31.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_50)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.checkBox_param_C2 = QCheckBox(self.frame_52)
        self.checkBox_param_C2.setObjectName(u"checkBox_param_C2")
        self.checkBox_param_C2.setMinimumSize(QSize(0, 0))
        self.checkBox_param_C2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_25.addWidget(self.checkBox_param_C2)

        self.label_param_C2 = QLabel(self.frame_52)
        self.label_param_C2.setObjectName(u"label_param_C2")
        self.label_param_C2.setMinimumSize(QSize(50, 20))
        self.label_param_C2.setMaximumSize(QSize(50, 20))
        self.label_param_C2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_param_C2)


        self.verticalLayout_31.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_50)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.checkBox_param_C3 = QCheckBox(self.frame_53)
        self.checkBox_param_C3.setObjectName(u"checkBox_param_C3")
        self.checkBox_param_C3.setMinimumSize(QSize(0, 0))
        self.checkBox_param_C3.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_26.addWidget(self.checkBox_param_C3)

        self.label_param_C3 = QLabel(self.frame_53)
        self.label_param_C3.setObjectName(u"label_param_C3")
        self.label_param_C3.setMinimumSize(QSize(50, 20))
        self.label_param_C3.setMaximumSize(QSize(50, 20))
        self.label_param_C3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_param_C3)


        self.verticalLayout_31.addWidget(self.frame_53)


        self.horizontalLayout_18.addWidget(self.frame_50)

        self.frame_54 = QFrame(self.frame_plastic_properties)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_54)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.checkBox_param_e = QCheckBox(self.frame_55)
        self.checkBox_param_e.setObjectName(u"checkBox_param_e")
        self.checkBox_param_e.setMinimumSize(QSize(0, 0))
        self.checkBox_param_e.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_27.addWidget(self.checkBox_param_e)

        self.label_param_e = QLabel(self.frame_55)
        self.label_param_e.setObjectName(u"label_param_e")
        self.label_param_e.setMinimumSize(QSize(50, 20))
        self.label_param_e.setMaximumSize(QSize(50, 20))
        self.label_param_e.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_param_e)


        self.verticalLayout_32.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_54)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.checkBox_param_k = QCheckBox(self.frame_56)
        self.checkBox_param_k.setObjectName(u"checkBox_param_k")
        self.checkBox_param_k.setMinimumSize(QSize(0, 0))
        self.checkBox_param_k.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_28.addWidget(self.checkBox_param_k)

        self.label_param_k = QLabel(self.frame_56)
        self.label_param_k.setObjectName(u"label_param_k")
        self.label_param_k.setMinimumSize(QSize(50, 20))
        self.label_param_k.setMaximumSize(QSize(50, 20))
        self.label_param_k.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_param_k)


        self.verticalLayout_32.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.frame_54)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.checkBox_param_Ts = QCheckBox(self.frame_57)
        self.checkBox_param_Ts.setObjectName(u"checkBox_param_Ts")
        self.checkBox_param_Ts.setMinimumSize(QSize(0, 0))
        self.checkBox_param_Ts.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_29.addWidget(self.checkBox_param_Ts)

        self.label_param_Ts = QLabel(self.frame_57)
        self.label_param_Ts.setObjectName(u"label_param_Ts")
        self.label_param_Ts.setMinimumSize(QSize(50, 20))
        self.label_param_Ts.setMaximumSize(QSize(50, 20))
        self.label_param_Ts.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_param_Ts)


        self.verticalLayout_32.addWidget(self.frame_57)


        self.horizontalLayout_18.addWidget(self.frame_54)


        self.verticalLayout_28.addWidget(self.frame_plastic_properties)


        self.verticalLayout_38.addWidget(self.frame_material_model)

        self.frame_damage_model = QFrame(self.frame_37)
        self.frame_damage_model.setObjectName(u"frame_damage_model")
        self.frame_damage_model.setEnabled(True)
        self.frame_damage_model.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_damage_model.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_damage_model)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.frame_damage_model)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_58)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(10, -1, -1, -1)
        self.label_19 = QLabel(self.frame_58)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font6)

        self.verticalLayout_34.addWidget(self.label_19)


        self.verticalLayout_33.addWidget(self.frame_58)

        self.frame_damage_properties = QFrame(self.frame_damage_model)
        self.frame_damage_properties.setObjectName(u"frame_damage_properties")
        self.frame_damage_properties.setEnabled(True)
        self.frame_damage_properties.setStyleSheet(u"/* QLabel*/\n"
"QLabel{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}")
        self.frame_damage_properties.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_damage_properties.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_damage_properties)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_60 = QFrame(self.frame_damage_properties)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_60)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_61 = QFrame(self.frame_60)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.checkBox_param_D1 = QCheckBox(self.frame_61)
        self.checkBox_param_D1.setObjectName(u"checkBox_param_D1")
        self.checkBox_param_D1.setMinimumSize(QSize(0, 0))
        self.checkBox_param_D1.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_31.addWidget(self.checkBox_param_D1)

        self.label_param_D1 = QLabel(self.frame_61)
        self.label_param_D1.setObjectName(u"label_param_D1")
        self.label_param_D1.setMinimumSize(QSize(50, 20))
        self.label_param_D1.setMaximumSize(QSize(50, 20))
        self.label_param_D1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_param_D1)


        self.verticalLayout_35.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_60)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.checkBox_param_D2 = QCheckBox(self.frame_62)
        self.checkBox_param_D2.setObjectName(u"checkBox_param_D2")
        self.checkBox_param_D2.setMinimumSize(QSize(0, 0))
        self.checkBox_param_D2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_32.addWidget(self.checkBox_param_D2)

        self.label_param_D2 = QLabel(self.frame_62)
        self.label_param_D2.setObjectName(u"label_param_D2")
        self.label_param_D2.setMinimumSize(QSize(50, 20))
        self.label_param_D2.setMaximumSize(QSize(50, 20))
        self.label_param_D2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_param_D2)


        self.verticalLayout_35.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_60)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.checkBox_param_D3 = QCheckBox(self.frame_63)
        self.checkBox_param_D3.setObjectName(u"checkBox_param_D3")
        self.checkBox_param_D3.setMinimumSize(QSize(0, 0))
        self.checkBox_param_D3.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_33.addWidget(self.checkBox_param_D3)

        self.label_param_D3 = QLabel(self.frame_63)
        self.label_param_D3.setObjectName(u"label_param_D3")
        self.label_param_D3.setMinimumSize(QSize(50, 20))
        self.label_param_D3.setMaximumSize(QSize(50, 20))
        self.label_param_D3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_param_D3)


        self.verticalLayout_35.addWidget(self.frame_63)


        self.horizontalLayout_30.addWidget(self.frame_60)

        self.frame_64 = QFrame(self.frame_damage_properties)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_64)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.checkBox_param_D4 = QCheckBox(self.frame_65)
        self.checkBox_param_D4.setObjectName(u"checkBox_param_D4")
        self.checkBox_param_D4.setMinimumSize(QSize(0, 0))
        self.checkBox_param_D4.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_34.addWidget(self.checkBox_param_D4)

        self.label_param_D4 = QLabel(self.frame_65)
        self.label_param_D4.setObjectName(u"label_param_D4")
        self.label_param_D4.setMinimumSize(QSize(50, 20))
        self.label_param_D4.setMaximumSize(QSize(50, 20))
        self.label_param_D4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_param_D4)


        self.verticalLayout_36.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.frame_64)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.checkBox_param_D5 = QCheckBox(self.frame_66)
        self.checkBox_param_D5.setObjectName(u"checkBox_param_D5")
        self.checkBox_param_D5.setMinimumSize(QSize(0, 0))
        self.checkBox_param_D5.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_35.addWidget(self.checkBox_param_D5)

        self.label_param_D5 = QLabel(self.frame_66)
        self.label_param_D5.setObjectName(u"label_param_D5")
        self.label_param_D5.setMinimumSize(QSize(50, 20))
        self.label_param_D5.setMaximumSize(QSize(50, 20))
        self.label_param_D5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_param_D5)


        self.verticalLayout_36.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_64)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.checkBox_param_Tm = QCheckBox(self.frame_67)
        self.checkBox_param_Tm.setObjectName(u"checkBox_param_Tm")
        self.checkBox_param_Tm.setMinimumSize(QSize(0, 0))
        self.checkBox_param_Tm.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_36.addWidget(self.checkBox_param_Tm)

        self.label_param_Tm = QLabel(self.frame_67)
        self.label_param_Tm.setObjectName(u"label_param_Tm")
        self.label_param_Tm.setMinimumSize(QSize(50, 20))
        self.label_param_Tm.setMaximumSize(QSize(50, 20))
        self.label_param_Tm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_param_Tm)


        self.verticalLayout_36.addWidget(self.frame_67)


        self.horizontalLayout_30.addWidget(self.frame_64)

        self.frame_68 = QFrame(self.frame_damage_properties)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_68.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_68)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.frame_68)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.checkBox_param_Tt = QCheckBox(self.frame_69)
        self.checkBox_param_Tt.setObjectName(u"checkBox_param_Tt")
        self.checkBox_param_Tt.setMinimumSize(QSize(0, 0))
        self.checkBox_param_Tt.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_37.addWidget(self.checkBox_param_Tt)

        self.label_param_Tt = QLabel(self.frame_69)
        self.label_param_Tt.setObjectName(u"label_param_Tt")
        self.label_param_Tt.setMinimumSize(QSize(50, 20))
        self.label_param_Tt.setMaximumSize(QSize(50, 20))
        self.label_param_Tt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_param_Tt)


        self.verticalLayout_37.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_68)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.checkBox_param_e_damage = QCheckBox(self.frame_70)
        self.checkBox_param_e_damage.setObjectName(u"checkBox_param_e_damage")
        self.checkBox_param_e_damage.setMinimumSize(QSize(0, 0))
        self.checkBox_param_e_damage.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_38.addWidget(self.checkBox_param_e_damage)

        self.label_param_e_damage = QLabel(self.frame_70)
        self.label_param_e_damage.setObjectName(u"label_param_e_damage")
        self.label_param_e_damage.setMinimumSize(QSize(50, 20))
        self.label_param_e_damage.setMaximumSize(QSize(50, 20))
        self.label_param_e_damage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_param_e_damage)


        self.verticalLayout_37.addWidget(self.frame_70)

        self.frame_71 = QFrame(self.frame_68)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.checkBox_param_p = QCheckBox(self.frame_71)
        self.checkBox_param_p.setObjectName(u"checkBox_param_p")
        self.checkBox_param_p.setMinimumSize(QSize(0, 0))
        self.checkBox_param_p.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_39.addWidget(self.checkBox_param_p)

        self.label_param_p = QLabel(self.frame_71)
        self.label_param_p.setObjectName(u"label_param_p")
        self.label_param_p.setMinimumSize(QSize(50, 20))
        self.label_param_p.setMaximumSize(QSize(50, 20))
        self.label_param_p.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_param_p)


        self.verticalLayout_37.addWidget(self.frame_71)


        self.horizontalLayout_30.addWidget(self.frame_68)


        self.verticalLayout_33.addWidget(self.frame_damage_properties)


        self.verticalLayout_38.addWidget(self.frame_damage_model)


        self.verticalLayout_25.addWidget(self.frame_37)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_5)

        self.frame_38 = QFrame(self.frame_36)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 60))
        self.frame_38.setMaximumSize(QSize(16777215, 60))
        self.frame_38.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.button_parameter_selection_back = QPushButton(self.frame_38)
        self.button_parameter_selection_back.setObjectName(u"button_parameter_selection_back")
        self.button_parameter_selection_back.setMinimumSize(QSize(100, 38))
        self.button_parameter_selection_back.setMaximumSize(QSize(100, 38))
        self.button_parameter_selection_back.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.button_parameter_selection_back)

        self.button_parameter_selection_next_page = QPushButton(self.frame_38)
        self.button_parameter_selection_next_page.setObjectName(u"button_parameter_selection_next_page")
        self.button_parameter_selection_next_page.setMinimumSize(QSize(100, 38))
        self.button_parameter_selection_next_page.setMaximumSize(QSize(100, 38))
        self.button_parameter_selection_next_page.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.button_parameter_selection_next_page)


        self.verticalLayout_25.addWidget(self.frame_38)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_6)


        self.horizontalLayout_67.addWidget(self.frame_36)


        self.verticalLayout_27.addWidget(self.frame_35)

        self.frame_34 = QFrame(self.page_parameter_selection)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 20))
        self.frame_34.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_34.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_34)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_34)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_18)


        self.verticalLayout_27.addWidget(self.frame_34)

        self.pages.addWidget(self.page_parameter_selection)
        self.page_parameter_definition = QWidget()
        self.page_parameter_definition.setObjectName(u"page_parameter_definition")
        self.page_parameter_definition.setStyleSheet(u"/* QLabel and QLineEdit*/\n"
"QLineEdit {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}\n"
"\n"
"\n"
"/* QPushButton*/\n"
"#button_parameter_limits_next_page, #button_parameter_limits_back {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_parameter_limits_next_page:hover, #button_parameter_limits_back:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_parameter_limits_next_page:pressed, #button_parameter_limits_back:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"")
        self.verticalLayout_54 = QVBoxLayout(self.page_parameter_definition)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.page_parameter_definition)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 70))
        self.frame_45.setMaximumSize(QSize(16777215, 70))
        self.frame_45.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_45.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.icon_interface_6 = QLabel(self.frame_45)
        self.icon_interface_6.setObjectName(u"icon_interface_6")
        self.icon_interface_6.setMinimumSize(QSize(50, 50))
        self.icon_interface_6.setMaximumSize(QSize(50, 50))
        self.icon_interface_6.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_6.setScaledContents(True)

        self.horizontalLayout_40.addWidget(self.icon_interface_6)

        self.interface_name_6 = QLabel(self.frame_45)
        self.interface_name_6.setObjectName(u"interface_name_6")
        self.interface_name_6.setFont(font)
        self.interface_name_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.interface_name_6)


        self.verticalLayout_54.addWidget(self.frame_45)

        self.frame_72 = QFrame(self.page_parameter_definition)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_72.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_72.setLineWidth(0)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.frame_73 = QFrame(self.frame_72)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMaximumSize(QSize(400, 16777215))
        self.frame_73.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_73.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_73)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 10)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_9)

        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_74.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_74)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_75 = QFrame(self.frame_74)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 40))
        self.frame_75.setMaximumSize(QSize(16777215, 40))
        self.frame_75.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_75.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_75)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.comboBox_material_limits = QComboBox(self.frame_75)
        self.comboBox_material_limits.setObjectName(u"comboBox_material_limits")
        self.comboBox_material_limits.setMinimumSize(QSize(0, 20))
        self.comboBox_material_limits.setMaximumSize(QSize(150, 16777215))
        self.comboBox_material_limits.setIconSize(QSize(10, 10))

        self.verticalLayout_43.addWidget(self.comboBox_material_limits)


        self.verticalLayout_42.addWidget(self.frame_75)

        self.frame_105 = QFrame(self.frame_74)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_105)
        self.verticalLayout_61.setSpacing(20)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(-1, 0, -1, -1)
        self.frame_91 = QFrame(self.frame_105)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setEnabled(True)
        self.frame_91.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_91)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_76 = QFrame(self.frame_91)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMaximumSize(QSize(16777215, 40))
        self.frame_76.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_76)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, -1, -1, -1)
        self.label_39 = QLabel(self.frame_76)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font6)

        self.verticalLayout_45.addWidget(self.label_39)


        self.verticalLayout_44.addWidget(self.frame_76)

        self.frame_limits_plastic = QFrame(self.frame_91)
        self.frame_limits_plastic.setObjectName(u"frame_limits_plastic")
        self.frame_limits_plastic.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_plastic.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_limits_plastic)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_limits_param_A = QFrame(self.frame_limits_plastic)
        self.frame_limits_param_A.setObjectName(u"frame_limits_param_A")
        self.frame_limits_param_A.setEnabled(True)
        self.frame_limits_param_A.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_A.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_A.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_A.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_limits_param_A)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_limits_param_A)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_42.addWidget(self.label_40)

        self.lineEdit_min_param_A = QLineEdit(self.frame_limits_param_A)
        self.lineEdit_min_param_A.setObjectName(u"lineEdit_min_param_A")
        self.lineEdit_min_param_A.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_A.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_A.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_42.addWidget(self.lineEdit_min_param_A)

        self.lineEdit_max_param_A = QLineEdit(self.frame_limits_param_A)
        self.lineEdit_max_param_A.setObjectName(u"lineEdit_max_param_A")
        self.lineEdit_max_param_A.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_A.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_A.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_42.addWidget(self.lineEdit_max_param_A)


        self.verticalLayout_46.addWidget(self.frame_limits_param_A)

        self.frame_limits_param_B = QFrame(self.frame_limits_plastic)
        self.frame_limits_param_B.setObjectName(u"frame_limits_param_B")
        self.frame_limits_param_B.setEnabled(True)
        self.frame_limits_param_B.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_B.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_B.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_B.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_limits_param_B)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.frame_limits_param_B)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_50.addWidget(self.label_66)

        self.lineEdit_min_param_B = QLineEdit(self.frame_limits_param_B)
        self.lineEdit_min_param_B.setObjectName(u"lineEdit_min_param_B")
        self.lineEdit_min_param_B.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_B.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_B.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_50.addWidget(self.lineEdit_min_param_B)

        self.lineEdit_max_param_B = QLineEdit(self.frame_limits_param_B)
        self.lineEdit_max_param_B.setObjectName(u"lineEdit_max_param_B")
        self.lineEdit_max_param_B.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_B.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_B.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_50.addWidget(self.lineEdit_max_param_B)


        self.verticalLayout_46.addWidget(self.frame_limits_param_B)

        self.frame_limits_param_n = QFrame(self.frame_limits_plastic)
        self.frame_limits_param_n.setObjectName(u"frame_limits_param_n")
        self.frame_limits_param_n.setEnabled(True)
        self.frame_limits_param_n.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_n.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_n.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_n.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_limits_param_n)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.frame_limits_param_n)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_49.addWidget(self.label_64)

        self.lineEdit_min_param_n = QLineEdit(self.frame_limits_param_n)
        self.lineEdit_min_param_n.setObjectName(u"lineEdit_min_param_n")
        self.lineEdit_min_param_n.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_n.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_n.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_49.addWidget(self.lineEdit_min_param_n)

        self.lineEdit_max_param_n = QLineEdit(self.frame_limits_param_n)
        self.lineEdit_max_param_n.setObjectName(u"lineEdit_max_param_n")
        self.lineEdit_max_param_n.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_n.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_n.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_49.addWidget(self.lineEdit_max_param_n)


        self.verticalLayout_46.addWidget(self.frame_limits_param_n)

        self.frame_limits_param_C1 = QFrame(self.frame_limits_plastic)
        self.frame_limits_param_C1.setObjectName(u"frame_limits_param_C1")
        self.frame_limits_param_C1.setEnabled(True)
        self.frame_limits_param_C1.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_C1.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_C1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_C1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_limits_param_C1)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.frame_limits_param_C1)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_48.addWidget(self.label_62)

        self.lineEdit_min_param_C1 = QLineEdit(self.frame_limits_param_C1)
        self.lineEdit_min_param_C1.setObjectName(u"lineEdit_min_param_C1")
        self.lineEdit_min_param_C1.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_C1.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_C1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_48.addWidget(self.lineEdit_min_param_C1)

        self.lineEdit_max_param_C1 = QLineEdit(self.frame_limits_param_C1)
        self.lineEdit_max_param_C1.setObjectName(u"lineEdit_max_param_C1")
        self.lineEdit_max_param_C1.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_C1.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_C1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_48.addWidget(self.lineEdit_max_param_C1)


        self.verticalLayout_46.addWidget(self.frame_limits_param_C1)

        self.frame_limits_param_C2 = QFrame(self.frame_limits_plastic)
        self.frame_limits_param_C2.setObjectName(u"frame_limits_param_C2")
        self.frame_limits_param_C2.setEnabled(True)
        self.frame_limits_param_C2.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_C2.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_C2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_C2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_limits_param_C2)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.frame_limits_param_C2)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_47.addWidget(self.label_60)

        self.lineEdit_min_param_C2 = QLineEdit(self.frame_limits_param_C2)
        self.lineEdit_min_param_C2.setObjectName(u"lineEdit_min_param_C2")
        self.lineEdit_min_param_C2.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_C2.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_C2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_47.addWidget(self.lineEdit_min_param_C2)

        self.lineEdit_max_param_C2 = QLineEdit(self.frame_limits_param_C2)
        self.lineEdit_max_param_C2.setObjectName(u"lineEdit_max_param_C2")
        self.lineEdit_max_param_C2.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_C2.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_C2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_47.addWidget(self.lineEdit_max_param_C2)


        self.verticalLayout_46.addWidget(self.frame_limits_param_C2)

        self.frame_limits_param_C3 = QFrame(self.frame_limits_plastic)
        self.frame_limits_param_C3.setObjectName(u"frame_limits_param_C3")
        self.frame_limits_param_C3.setEnabled(True)
        self.frame_limits_param_C3.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_C3.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_C3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_C3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_limits_param_C3)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_limits_param_C3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_46.addWidget(self.label_48)

        self.lineEdit_min_param_C3 = QLineEdit(self.frame_limits_param_C3)
        self.lineEdit_min_param_C3.setObjectName(u"lineEdit_min_param_C3")
        self.lineEdit_min_param_C3.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_C3.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_C3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_46.addWidget(self.lineEdit_min_param_C3)

        self.lineEdit_max_param_C3 = QLineEdit(self.frame_limits_param_C3)
        self.lineEdit_max_param_C3.setObjectName(u"lineEdit_max_param_C3")
        self.lineEdit_max_param_C3.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_C3.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_C3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_46.addWidget(self.lineEdit_max_param_C3)


        self.verticalLayout_46.addWidget(self.frame_limits_param_C3)

        self.frame_limits_param_e = QFrame(self.frame_limits_plastic)
        self.frame_limits_param_e.setObjectName(u"frame_limits_param_e")
        self.frame_limits_param_e.setEnabled(True)
        self.frame_limits_param_e.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_e.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_e.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_e.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_limits_param_e)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_limits_param_e)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_45.addWidget(self.label_46)

        self.lineEdit_min_param_e = QLineEdit(self.frame_limits_param_e)
        self.lineEdit_min_param_e.setObjectName(u"lineEdit_min_param_e")
        self.lineEdit_min_param_e.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_e.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_e.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_45.addWidget(self.lineEdit_min_param_e)

        self.lineEdit_max_param_e = QLineEdit(self.frame_limits_param_e)
        self.lineEdit_max_param_e.setObjectName(u"lineEdit_max_param_e")
        self.lineEdit_max_param_e.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_e.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_e.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_45.addWidget(self.lineEdit_max_param_e)


        self.verticalLayout_46.addWidget(self.frame_limits_param_e)

        self.frame_limits_param_k = QFrame(self.frame_limits_plastic)
        self.frame_limits_param_k.setObjectName(u"frame_limits_param_k")
        self.frame_limits_param_k.setEnabled(True)
        self.frame_limits_param_k.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_k.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_k.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_k.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_limits_param_k)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_limits_param_k)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_44.addWidget(self.label_44)

        self.lineEdit_min_param_k = QLineEdit(self.frame_limits_param_k)
        self.lineEdit_min_param_k.setObjectName(u"lineEdit_min_param_k")
        self.lineEdit_min_param_k.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_k.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_k.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_44.addWidget(self.lineEdit_min_param_k)

        self.lineEdit_max_param_k = QLineEdit(self.frame_limits_param_k)
        self.lineEdit_max_param_k.setObjectName(u"lineEdit_max_param_k")
        self.lineEdit_max_param_k.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_k.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_k.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_44.addWidget(self.lineEdit_max_param_k)


        self.verticalLayout_46.addWidget(self.frame_limits_param_k)

        self.frame_limits_param_Ts = QFrame(self.frame_limits_plastic)
        self.frame_limits_param_Ts.setObjectName(u"frame_limits_param_Ts")
        self.frame_limits_param_Ts.setEnabled(True)
        self.frame_limits_param_Ts.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_Ts.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_Ts.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_Ts.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_limits_param_Ts)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_limits_param_Ts)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_43.addWidget(self.label_42)

        self.lineEdit_min_param_Ts = QLineEdit(self.frame_limits_param_Ts)
        self.lineEdit_min_param_Ts.setObjectName(u"lineEdit_min_param_Ts")
        self.lineEdit_min_param_Ts.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_Ts.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_Ts.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_43.addWidget(self.lineEdit_min_param_Ts)

        self.lineEdit_max_param_Ts = QLineEdit(self.frame_limits_param_Ts)
        self.lineEdit_max_param_Ts.setObjectName(u"lineEdit_max_param_Ts")
        self.lineEdit_max_param_Ts.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_Ts.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_Ts.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_43.addWidget(self.lineEdit_max_param_Ts)


        self.verticalLayout_46.addWidget(self.frame_limits_param_Ts)


        self.verticalLayout_44.addWidget(self.frame_limits_plastic)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_3)


        self.verticalLayout_61.addWidget(self.frame_91)

        self.frame_77 = QFrame(self.frame_105)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setEnabled(True)
        self.frame_77.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_77)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_90 = QFrame(self.frame_77)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(16777215, 40))
        self.frame_90.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_90)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, -1, -1, -1)
        self.label_49 = QLabel(self.frame_90)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font6)

        self.verticalLayout_50.addWidget(self.label_49)


        self.verticalLayout_49.addWidget(self.frame_90)

        self.frame_limits_damage = QFrame(self.frame_77)
        self.frame_limits_damage.setObjectName(u"frame_limits_damage")
        self.frame_limits_damage.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_damage.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_limits_damage)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_limits_param_D1 = QFrame(self.frame_limits_damage)
        self.frame_limits_param_D1.setObjectName(u"frame_limits_param_D1")
        self.frame_limits_param_D1.setEnabled(True)
        self.frame_limits_param_D1.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_D1.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_D1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_D1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_limits_param_D1)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_limits_param_D1)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_51.addWidget(self.label_50)

        self.lineEdit_min_param_D1 = QLineEdit(self.frame_limits_param_D1)
        self.lineEdit_min_param_D1.setObjectName(u"lineEdit_min_param_D1")
        self.lineEdit_min_param_D1.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_D1.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_D1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_51.addWidget(self.lineEdit_min_param_D1)

        self.lineEdit_max_param_D1 = QLineEdit(self.frame_limits_param_D1)
        self.lineEdit_max_param_D1.setObjectName(u"lineEdit_max_param_D1")
        self.lineEdit_max_param_D1.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_D1.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_D1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_51.addWidget(self.lineEdit_max_param_D1)


        self.verticalLayout_47.addWidget(self.frame_limits_param_D1)

        self.frame_limits_param_D2 = QFrame(self.frame_limits_damage)
        self.frame_limits_param_D2.setObjectName(u"frame_limits_param_D2")
        self.frame_limits_param_D2.setEnabled(True)
        self.frame_limits_param_D2.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_D2.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_D2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_D2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_limits_param_D2)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_limits_param_D2)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_52.addWidget(self.label_52)

        self.lineEdit_min_param_D2 = QLineEdit(self.frame_limits_param_D2)
        self.lineEdit_min_param_D2.setObjectName(u"lineEdit_min_param_D2")
        self.lineEdit_min_param_D2.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_D2.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_D2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_52.addWidget(self.lineEdit_min_param_D2)

        self.lineEdit_max_param_D2 = QLineEdit(self.frame_limits_param_D2)
        self.lineEdit_max_param_D2.setObjectName(u"lineEdit_max_param_D2")
        self.lineEdit_max_param_D2.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_D2.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_D2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_52.addWidget(self.lineEdit_max_param_D2)


        self.verticalLayout_47.addWidget(self.frame_limits_param_D2)

        self.frame_limits_param_D3 = QFrame(self.frame_limits_damage)
        self.frame_limits_param_D3.setObjectName(u"frame_limits_param_D3")
        self.frame_limits_param_D3.setEnabled(True)
        self.frame_limits_param_D3.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_D3.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_D3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_D3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_limits_param_D3)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.frame_limits_param_D3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_54.addWidget(self.label_56)

        self.lineEdit_min_param_D3 = QLineEdit(self.frame_limits_param_D3)
        self.lineEdit_min_param_D3.setObjectName(u"lineEdit_min_param_D3")
        self.lineEdit_min_param_D3.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_D3.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_D3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_54.addWidget(self.lineEdit_min_param_D3)

        self.lineEdit_max_param_D3 = QLineEdit(self.frame_limits_param_D3)
        self.lineEdit_max_param_D3.setObjectName(u"lineEdit_max_param_D3")
        self.lineEdit_max_param_D3.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_D3.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_D3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_54.addWidget(self.lineEdit_max_param_D3)


        self.verticalLayout_47.addWidget(self.frame_limits_param_D3)

        self.frame_limits_param_D4 = QFrame(self.frame_limits_damage)
        self.frame_limits_param_D4.setObjectName(u"frame_limits_param_D4")
        self.frame_limits_param_D4.setEnabled(True)
        self.frame_limits_param_D4.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_D4.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_D4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_D4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_limits_param_D4)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.frame_limits_param_D4)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_55.addWidget(self.label_58)

        self.lineEdit_min_param_D4 = QLineEdit(self.frame_limits_param_D4)
        self.lineEdit_min_param_D4.setObjectName(u"lineEdit_min_param_D4")
        self.lineEdit_min_param_D4.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_D4.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_D4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_55.addWidget(self.lineEdit_min_param_D4)

        self.lineEdit_max_param_D4 = QLineEdit(self.frame_limits_param_D4)
        self.lineEdit_max_param_D4.setObjectName(u"lineEdit_max_param_D4")
        self.lineEdit_max_param_D4.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_D4.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_D4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_55.addWidget(self.lineEdit_max_param_D4)


        self.verticalLayout_47.addWidget(self.frame_limits_param_D4)

        self.frame_limits_param_D5 = QFrame(self.frame_limits_damage)
        self.frame_limits_param_D5.setObjectName(u"frame_limits_param_D5")
        self.frame_limits_param_D5.setEnabled(True)
        self.frame_limits_param_D5.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_D5.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_D5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_D5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_limits_param_D5)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_limits_param_D5)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_53.addWidget(self.label_54)

        self.lineEdit_min_param_D5 = QLineEdit(self.frame_limits_param_D5)
        self.lineEdit_min_param_D5.setObjectName(u"lineEdit_min_param_D5")
        self.lineEdit_min_param_D5.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_D5.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_D5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_53.addWidget(self.lineEdit_min_param_D5)

        self.lineEdit_max_param_D5 = QLineEdit(self.frame_limits_param_D5)
        self.lineEdit_max_param_D5.setObjectName(u"lineEdit_max_param_D5")
        self.lineEdit_max_param_D5.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_D5.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_D5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_53.addWidget(self.lineEdit_max_param_D5)


        self.verticalLayout_47.addWidget(self.frame_limits_param_D5)

        self.frame_limits_param_Tm = QFrame(self.frame_limits_damage)
        self.frame_limits_param_Tm.setObjectName(u"frame_limits_param_Tm")
        self.frame_limits_param_Tm.setEnabled(True)
        self.frame_limits_param_Tm.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_Tm.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_Tm.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_Tm.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_limits_param_Tm)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.frame_limits_param_Tm)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_56.addWidget(self.label_69)

        self.lineEdit_min_param_Tm = QLineEdit(self.frame_limits_param_Tm)
        self.lineEdit_min_param_Tm.setObjectName(u"lineEdit_min_param_Tm")
        self.lineEdit_min_param_Tm.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_Tm.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_Tm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_56.addWidget(self.lineEdit_min_param_Tm)

        self.lineEdit_max_param_Tm = QLineEdit(self.frame_limits_param_Tm)
        self.lineEdit_max_param_Tm.setObjectName(u"lineEdit_max_param_Tm")
        self.lineEdit_max_param_Tm.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_Tm.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_Tm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_56.addWidget(self.lineEdit_max_param_Tm)


        self.verticalLayout_47.addWidget(self.frame_limits_param_Tm)

        self.frame_limits_param_Tt = QFrame(self.frame_limits_damage)
        self.frame_limits_param_Tt.setObjectName(u"frame_limits_param_Tt")
        self.frame_limits_param_Tt.setEnabled(True)
        self.frame_limits_param_Tt.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_Tt.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_Tt.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_Tt.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_limits_param_Tt)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_71 = QLabel(self.frame_limits_param_Tt)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_57.addWidget(self.label_71)

        self.lineEdit_min_param_Tt = QLineEdit(self.frame_limits_param_Tt)
        self.lineEdit_min_param_Tt.setObjectName(u"lineEdit_min_param_Tt")
        self.lineEdit_min_param_Tt.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_Tt.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_Tt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_57.addWidget(self.lineEdit_min_param_Tt)

        self.lineEdit_max_param_Tt = QLineEdit(self.frame_limits_param_Tt)
        self.lineEdit_max_param_Tt.setObjectName(u"lineEdit_max_param_Tt")
        self.lineEdit_max_param_Tt.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_Tt.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_Tt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_57.addWidget(self.lineEdit_max_param_Tt)


        self.verticalLayout_47.addWidget(self.frame_limits_param_Tt)

        self.frame_limits_param_e_damage = QFrame(self.frame_limits_damage)
        self.frame_limits_param_e_damage.setObjectName(u"frame_limits_param_e_damage")
        self.frame_limits_param_e_damage.setEnabled(True)
        self.frame_limits_param_e_damage.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_e_damage.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_e_damage.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_e_damage.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_limits_param_e_damage)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.frame_limits_param_e_damage)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_58.addWidget(self.label_73)

        self.lineEdit_min_param_e_damage = QLineEdit(self.frame_limits_param_e_damage)
        self.lineEdit_min_param_e_damage.setObjectName(u"lineEdit_min_param_e_damage")
        self.lineEdit_min_param_e_damage.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_e_damage.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_e_damage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_58.addWidget(self.lineEdit_min_param_e_damage)

        self.lineEdit_max_param_e_damage = QLineEdit(self.frame_limits_param_e_damage)
        self.lineEdit_max_param_e_damage.setObjectName(u"lineEdit_max_param_e_damage")
        self.lineEdit_max_param_e_damage.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_e_damage.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_e_damage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_58.addWidget(self.lineEdit_max_param_e_damage)


        self.verticalLayout_47.addWidget(self.frame_limits_param_e_damage)

        self.frame_limits_param_p = QFrame(self.frame_limits_damage)
        self.frame_limits_param_p.setObjectName(u"frame_limits_param_p")
        self.frame_limits_param_p.setEnabled(True)
        self.frame_limits_param_p.setMinimumSize(QSize(0, 35))
        self.frame_limits_param_p.setMaximumSize(QSize(16777215, 35))
        self.frame_limits_param_p.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_limits_param_p.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_limits_param_p)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_75 = QLabel(self.frame_limits_param_p)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_59.addWidget(self.label_75)

        self.lineEdit_min_param_p = QLineEdit(self.frame_limits_param_p)
        self.lineEdit_min_param_p.setObjectName(u"lineEdit_min_param_p")
        self.lineEdit_min_param_p.setMinimumSize(QSize(40, 0))
        self.lineEdit_min_param_p.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_min_param_p.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_59.addWidget(self.lineEdit_min_param_p)

        self.lineEdit_max_param_p = QLineEdit(self.frame_limits_param_p)
        self.lineEdit_max_param_p.setObjectName(u"lineEdit_max_param_p")
        self.lineEdit_max_param_p.setMinimumSize(QSize(40, 0))
        self.lineEdit_max_param_p.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_max_param_p.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_59.addWidget(self.lineEdit_max_param_p)


        self.verticalLayout_47.addWidget(self.frame_limits_param_p)


        self.verticalLayout_49.addWidget(self.frame_limits_damage)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer)


        self.verticalLayout_61.addWidget(self.frame_77)


        self.verticalLayout_42.addWidget(self.frame_105)


        self.verticalLayout_41.addWidget(self.frame_74)

        self.frame_104 = QFrame(self.frame_73)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(0, 60))
        self.frame_104.setMaximumSize(QSize(16777215, 60))
        self.frame_104.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_104.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.button_parameter_limits_back = QPushButton(self.frame_104)
        self.button_parameter_limits_back.setObjectName(u"button_parameter_limits_back")
        self.button_parameter_limits_back.setMinimumSize(QSize(100, 38))
        self.button_parameter_limits_back.setMaximumSize(QSize(100, 38))
        self.button_parameter_limits_back.setStyleSheet(u"")

        self.horizontalLayout_61.addWidget(self.button_parameter_limits_back)

        self.button_parameter_limits_next_page = QPushButton(self.frame_104)
        self.button_parameter_limits_next_page.setObjectName(u"button_parameter_limits_next_page")
        self.button_parameter_limits_next_page.setMinimumSize(QSize(100, 38))
        self.button_parameter_limits_next_page.setMaximumSize(QSize(100, 38))
        self.button_parameter_limits_next_page.setStyleSheet(u"")

        self.horizontalLayout_61.addWidget(self.button_parameter_limits_next_page)


        self.verticalLayout_41.addWidget(self.frame_104)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_7)


        self.horizontalLayout_60.addWidget(self.frame_73)


        self.verticalLayout_54.addWidget(self.frame_72)

        self.frame_42 = QFrame(self.page_parameter_definition)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(16777215, 20))
        self.frame_42.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_42.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_42)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_42)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_38)


        self.verticalLayout_54.addWidget(self.frame_42)

        self.pages.addWidget(self.page_parameter_definition)
        self.page_pso_explanation = QWidget()
        self.page_pso_explanation.setObjectName(u"page_pso_explanation")
        self.page_pso_explanation.setStyleSheet(u"/* QPushButton*/\n"
"#button_pso_explanation_back, #button_pso_explanation_next_page {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_ps_explanationo_back:hover, #button_pso_explanation_next_page:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_pso_explanation_back:pressed, #button_ps_explanationo_next_page:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.page_pso_explanation)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_115 = QFrame(self.page_pso_explanation)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(0, 70))
        self.frame_115.setMaximumSize(QSize(16777215, 70))
        self.frame_115.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_115.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_115.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.icon_interface_8 = QLabel(self.frame_115)
        self.icon_interface_8.setObjectName(u"icon_interface_8")
        self.icon_interface_8.setMinimumSize(QSize(50, 50))
        self.icon_interface_8.setMaximumSize(QSize(50, 50))
        self.icon_interface_8.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_8.setScaledContents(True)

        self.horizontalLayout_78.addWidget(self.icon_interface_8)

        self.interface_name_8 = QLabel(self.frame_115)
        self.interface_name_8.setObjectName(u"interface_name_8")
        self.interface_name_8.setFont(font)
        self.interface_name_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_78.addWidget(self.interface_name_8)


        self.verticalLayout_8.addWidget(self.frame_115)

        self.frame_109 = QFrame(self.page_pso_explanation)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_109.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_109.setLineWidth(0)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.frame_110 = QFrame(self.frame_109)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMaximumSize(QSize(500, 480))
        self.frame_110.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_111 = QFrame(self.frame_110)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMaximumSize(QSize(16777215, 16777215))
        self.frame_111.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_111.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_111)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_112 = QFrame(self.frame_111)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMaximumSize(QSize(16777215, 16777215))
        self.frame_112.setStyleSheet(u"")
        self.frame_112.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_112.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_45 = QLabel(self.frame_112)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(16777215, 520))
        self.label_45.setTextFormat(Qt.TextFormat.AutoText)
        self.label_45.setScaledContents(False)
        self.label_45.setWordWrap(True)

        self.horizontalLayout_76.addWidget(self.label_45)


        self.verticalLayout_24.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.frame_111)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMinimumSize(QSize(0, 60))
        self.frame_113.setMaximumSize(QSize(16777215, 60))
        self.frame_113.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_113.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.button_pso_explanation_back = QPushButton(self.frame_113)
        self.button_pso_explanation_back.setObjectName(u"button_pso_explanation_back")
        self.button_pso_explanation_back.setMinimumSize(QSize(100, 38))
        self.button_pso_explanation_back.setMaximumSize(QSize(100, 38))
        self.button_pso_explanation_back.setStyleSheet(u"")

        self.horizontalLayout_77.addWidget(self.button_pso_explanation_back)

        self.button_pso_explanation_next_page = QPushButton(self.frame_113)
        self.button_pso_explanation_next_page.setObjectName(u"button_pso_explanation_next_page")
        self.button_pso_explanation_next_page.setMinimumSize(QSize(100, 38))
        self.button_pso_explanation_next_page.setMaximumSize(QSize(100, 38))
        self.button_pso_explanation_next_page.setStyleSheet(u"")

        self.horizontalLayout_77.addWidget(self.button_pso_explanation_next_page)


        self.verticalLayout_24.addWidget(self.frame_113)


        self.horizontalLayout_75.addWidget(self.frame_111)


        self.horizontalLayout_74.addWidget(self.frame_110)


        self.verticalLayout_8.addWidget(self.frame_109)

        self.frame_114 = QFrame(self.page_pso_explanation)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(0, 20))
        self.frame_114.setMaximumSize(QSize(16777215, 20))
        self.frame_114.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_114.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_114.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_114)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_114)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_48.addWidget(self.label_47)


        self.verticalLayout_8.addWidget(self.frame_114)

        self.pages.addWidget(self.page_pso_explanation)
        self.page_pso = QWidget()
        self.page_pso.setObjectName(u"page_pso")
        self.page_pso.setStyleSheet(u"/* QLabel and QLineEdit*/\n"
"#label_cores, #label_number_conditions, #lineEdit_number_iteration, #lineEdit_number_particles, #lineEdit_var1, #lineEdit_var2, #lineEdit_var3 {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}\n"
"\n"
"\n"
"/* QPushButton*/\n"
"#button_pso_back, #button_pso_next_page {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_pso_back:hover, #button_pso_next_page:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_pso_back:pressed, #button_pso_next_page:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.page_pso)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.page_pso)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(0, 70))
        self.frame_100.setMaximumSize(QSize(16777215, 70))
        self.frame_100.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_100.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_100.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.icon_interface_7 = QLabel(self.frame_100)
        self.icon_interface_7.setObjectName(u"icon_interface_7")
        self.icon_interface_7.setMinimumSize(QSize(50, 50))
        self.icon_interface_7.setMaximumSize(QSize(50, 50))
        self.icon_interface_7.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_7.setScaledContents(True)

        self.horizontalLayout_69.addWidget(self.icon_interface_7)

        self.interface_name_7 = QLabel(self.frame_100)
        self.interface_name_7.setObjectName(u"interface_name_7")
        self.interface_name_7.setFont(font)
        self.interface_name_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_69.addWidget(self.interface_name_7)


        self.verticalLayout_2.addWidget(self.frame_100)

        self.frame_102 = QFrame(self.page_pso)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_102.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_102.setLineWidth(0)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.frame_103 = QFrame(self.frame_102)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMaximumSize(QSize(600, 550))
        self.frame_103.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.frame_106 = QFrame(self.frame_103)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMaximumSize(QSize(16777215, 16777215))
        self.frame_106.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_106.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_106)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_107 = QFrame(self.frame_106)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMaximumSize(QSize(16777215, 16777215))
        self.frame_107.setStyleSheet(u"")
        self.frame_107.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_107.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_107)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_116 = QFrame(self.frame_107)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_116)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_122 = QFrame(self.frame_116)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMaximumSize(QSize(16777215, 50))
        self.frame_122.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_122)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_122)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 200))
        self.label_43.setTextFormat(Qt.TextFormat.AutoText)
        self.label_43.setScaledContents(False)
        self.label_43.setWordWrap(True)

        self.verticalLayout_53.addWidget(self.label_43)


        self.verticalLayout_56.addWidget(self.frame_122)

        self.frame_117 = QFrame(self.frame_116)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_117)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_140 = QFrame(self.frame_117)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setMinimumSize(QSize(0, 40))
        self.frame_140.setMaximumSize(QSize(16777215, 40))
        self.frame_140.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_140)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(9, 0, 9, 0)
        self.label_129 = QLabel(self.frame_140)
        self.label_129.setObjectName(u"label_129")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(11)
        font7.setBold(False)
        self.label_129.setFont(font7)

        self.horizontalLayout_82.addWidget(self.label_129)

        self.label_number_conditions = QLabel(self.frame_140)
        self.label_number_conditions.setObjectName(u"label_number_conditions")
        self.label_number_conditions.setMinimumSize(QSize(65, 20))
        self.label_number_conditions.setMaximumSize(QSize(65, 20))
        self.label_number_conditions.setStyleSheet(u"")
        self.label_number_conditions.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_82.addWidget(self.label_number_conditions)


        self.verticalLayout_55.addWidget(self.frame_140)

        self.frame_142 = QFrame(self.frame_117)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setMinimumSize(QSize(0, 40))
        self.frame_142.setMaximumSize(QSize(16777215, 40))
        self.frame_142.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_142)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(9, 0, 9, 0)
        self.label_131 = QLabel(self.frame_142)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setFont(font7)

        self.horizontalLayout_84.addWidget(self.label_131)

        self.lineEdit_number_iteration = QLineEdit(self.frame_142)
        self.lineEdit_number_iteration.setObjectName(u"lineEdit_number_iteration")
        self.lineEdit_number_iteration.setMinimumSize(QSize(65, 20))
        self.lineEdit_number_iteration.setMaximumSize(QSize(65, 20))
        self.lineEdit_number_iteration.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_84.addWidget(self.lineEdit_number_iteration)


        self.verticalLayout_55.addWidget(self.frame_142)

        self.frame_141 = QFrame(self.frame_117)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setMinimumSize(QSize(0, 40))
        self.frame_141.setMaximumSize(QSize(16777215, 40))
        self.frame_141.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_141)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(9, 0, 9, 0)
        self.label_130 = QLabel(self.frame_141)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setFont(font7)

        self.horizontalLayout_83.addWidget(self.label_130)

        self.lineEdit_number_particles = QLineEdit(self.frame_141)
        self.lineEdit_number_particles.setObjectName(u"lineEdit_number_particles")
        self.lineEdit_number_particles.setMinimumSize(QSize(65, 20))
        self.lineEdit_number_particles.setMaximumSize(QSize(65, 20))
        self.lineEdit_number_particles.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_83.addWidget(self.lineEdit_number_particles)


        self.verticalLayout_55.addWidget(self.frame_141)

        self.frame_144 = QFrame(self.frame_117)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setMinimumSize(QSize(0, 40))
        self.frame_144.setMaximumSize(QSize(16777215, 40))
        self.frame_144.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_144)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(9, 0, 9, 0)
        self.label_133 = QLabel(self.frame_144)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font7)

        self.horizontalLayout_86.addWidget(self.label_133)

        self.lineEdit_var2 = QLineEdit(self.frame_144)
        self.lineEdit_var2.setObjectName(u"lineEdit_var2")
        self.lineEdit_var2.setMinimumSize(QSize(65, 20))
        self.lineEdit_var2.setMaximumSize(QSize(65, 20))
        self.lineEdit_var2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_86.addWidget(self.lineEdit_var2)


        self.verticalLayout_55.addWidget(self.frame_144)

        self.frame_143 = QFrame(self.frame_117)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setMinimumSize(QSize(0, 40))
        self.frame_143.setMaximumSize(QSize(16777215, 40))
        self.frame_143.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_143)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(9, 0, 9, 0)
        self.label_132 = QLabel(self.frame_143)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setFont(font7)

        self.horizontalLayout_85.addWidget(self.label_132)

        self.lineEdit_var3 = QLineEdit(self.frame_143)
        self.lineEdit_var3.setObjectName(u"lineEdit_var3")
        self.lineEdit_var3.setMinimumSize(QSize(65, 20))
        self.lineEdit_var3.setMaximumSize(QSize(65, 20))
        self.lineEdit_var3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_85.addWidget(self.lineEdit_var3)


        self.verticalLayout_55.addWidget(self.frame_143)

        self.frame_145 = QFrame(self.frame_117)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setMinimumSize(QSize(0, 40))
        self.frame_145.setMaximumSize(QSize(16777215, 40))
        self.frame_145.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_145)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(9, 0, 9, 0)
        self.label_134 = QLabel(self.frame_145)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setFont(font7)

        self.horizontalLayout_87.addWidget(self.label_134)

        self.lineEdit_var1 = QLineEdit(self.frame_145)
        self.lineEdit_var1.setObjectName(u"lineEdit_var1")
        self.lineEdit_var1.setMinimumSize(QSize(65, 20))
        self.lineEdit_var1.setMaximumSize(QSize(65, 20))
        self.lineEdit_var1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_87.addWidget(self.lineEdit_var1)


        self.verticalLayout_55.addWidget(self.frame_145)


        self.verticalLayout_56.addWidget(self.frame_117)


        self.verticalLayout_57.addWidget(self.frame_116)

        self.frame_118 = QFrame(self.frame_107)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_118)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_120 = QFrame(self.frame_118)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMaximumSize(QSize(16777215, 50))
        self.frame_120.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_120)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.frame_120)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 200))
        self.label_51.setTextFormat(Qt.TextFormat.AutoText)
        self.label_51.setScaledContents(False)
        self.label_51.setWordWrap(True)

        self.verticalLayout_52.addWidget(self.label_51)


        self.verticalLayout_51.addWidget(self.frame_120)

        self.frame_119 = QFrame(self.frame_118)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_119)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_138 = QFrame(self.frame_119)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setMinimumSize(QSize(0, 40))
        self.frame_138.setMaximumSize(QSize(16777215, 40))
        self.frame_138.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(9, 0, 9, 0)
        self.label_128 = QLabel(self.frame_138)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setFont(font7)

        self.horizontalLayout_79.addWidget(self.label_128)

        self.label_cores = QLabel(self.frame_138)
        self.label_cores.setObjectName(u"label_cores")
        self.label_cores.setMinimumSize(QSize(65, 20))
        self.label_cores.setMaximumSize(QSize(65, 20))
        self.label_cores.setStyleSheet(u"")
        self.label_cores.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_79.addWidget(self.label_cores)


        self.verticalLayout_14.addWidget(self.frame_138)

        self.frame_139 = QFrame(self.frame_119)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setMinimumSize(QSize(0, 40))
        self.frame_139.setMaximumSize(QSize(16777215, 40))
        font8 = QFont()
        font8.setBold(False)
        self.frame_139.setFont(font8)
        self.frame_139.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_72 = QLabel(self.frame_139)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font7)

        self.horizontalLayout_81.addWidget(self.label_72)

        self.combobox_core_by_simulation = QComboBox(self.frame_139)
        self.combobox_core_by_simulation.addItem("")
        self.combobox_core_by_simulation.addItem("")
        self.combobox_core_by_simulation.addItem("")
        self.combobox_core_by_simulation.addItem("")
        self.combobox_core_by_simulation.addItem("")
        self.combobox_core_by_simulation.addItem("")
        self.combobox_core_by_simulation.addItem("")
        self.combobox_core_by_simulation.addItem("")
        self.combobox_core_by_simulation.addItem("")
        self.combobox_core_by_simulation.setObjectName(u"combobox_core_by_simulation")
        self.combobox_core_by_simulation.setMinimumSize(QSize(65, 20))
        self.combobox_core_by_simulation.setMaximumSize(QSize(65, 20))
        self.combobox_core_by_simulation.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.combobox_core_by_simulation.setStyleSheet(u"")
        self.combobox_core_by_simulation.setInsertPolicy(QComboBox.InsertPolicy.InsertAtCurrent)
        self.combobox_core_by_simulation.setFrame(True)

        self.horizontalLayout_81.addWidget(self.combobox_core_by_simulation)


        self.verticalLayout_14.addWidget(self.frame_139)

        self.frame_345 = QFrame(self.frame_119)
        self.frame_345.setObjectName(u"frame_345")
        self.frame_345.setMinimumSize(QSize(0, 40))
        self.frame_345.setMaximumSize(QSize(16777215, 40))
        self.frame_345.setStyleSheet(u"")
        self.frame_345.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_345.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_345)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.label_76 = QLabel(self.frame_345)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font7)

        self.horizontalLayout_90.addWidget(self.label_76)

        self.combobox_number_computer = QComboBox(self.frame_345)
        self.combobox_number_computer.addItem("")
        self.combobox_number_computer.addItem("")
        self.combobox_number_computer.addItem("")
        self.combobox_number_computer.addItem("")
        self.combobox_number_computer.addItem("")
        self.combobox_number_computer.addItem("")
        self.combobox_number_computer.setObjectName(u"combobox_number_computer")
        self.combobox_number_computer.setMinimumSize(QSize(65, 20))
        self.combobox_number_computer.setMaximumSize(QSize(65, 20))
        self.combobox_number_computer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.combobox_number_computer.setStyleSheet(u"QComboBox{\n"
"text-align: center;}")
        self.combobox_number_computer.setInsertPolicy(QComboBox.InsertPolicy.InsertAtCurrent)
        self.combobox_number_computer.setFrame(True)

        self.horizontalLayout_90.addWidget(self.combobox_number_computer)


        self.verticalLayout_14.addWidget(self.frame_345)

        self.frame_344 = QFrame(self.frame_119)
        self.frame_344.setObjectName(u"frame_344")
        self.frame_344.setMinimumSize(QSize(0, 40))
        self.frame_344.setMaximumSize(QSize(16777215, 40))
        self.frame_344.setStyleSheet(u"")
        self.frame_344.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_344.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_344)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_74 = QLabel(self.frame_344)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font7)

        self.horizontalLayout_88.addWidget(self.label_74)

        self.combobox_main_computer = QComboBox(self.frame_344)
        self.combobox_main_computer.addItem("")
        self.combobox_main_computer.addItem("")
        self.combobox_main_computer.setObjectName(u"combobox_main_computer")
        self.combobox_main_computer.setMinimumSize(QSize(65, 20))
        self.combobox_main_computer.setMaximumSize(QSize(65, 20))
        self.combobox_main_computer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.combobox_main_computer.setStyleSheet(u"")
        self.combobox_main_computer.setInsertPolicy(QComboBox.InsertPolicy.InsertAtCurrent)
        self.combobox_main_computer.setFrame(True)

        self.horizontalLayout_88.addWidget(self.combobox_main_computer)


        self.verticalLayout_14.addWidget(self.frame_344)


        self.verticalLayout_51.addWidget(self.frame_119)


        self.verticalLayout_57.addWidget(self.frame_118)


        self.verticalLayout_21.addWidget(self.frame_107)

        self.frame_108 = QFrame(self.frame_106)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(0, 60))
        self.frame_108.setMaximumSize(QSize(16777215, 60))
        self.frame_108.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_108.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.button_pso_back = QPushButton(self.frame_108)
        self.button_pso_back.setObjectName(u"button_pso_back")
        self.button_pso_back.setMinimumSize(QSize(100, 38))
        self.button_pso_back.setMaximumSize(QSize(100, 38))
        self.button_pso_back.setStyleSheet(u"")

        self.horizontalLayout_73.addWidget(self.button_pso_back)

        self.button_pso_next_page = QPushButton(self.frame_108)
        self.button_pso_next_page.setObjectName(u"button_pso_next_page")
        self.button_pso_next_page.setMinimumSize(QSize(100, 38))
        self.button_pso_next_page.setMaximumSize(QSize(100, 38))
        self.button_pso_next_page.setStyleSheet(u"")

        self.horizontalLayout_73.addWidget(self.button_pso_next_page)


        self.verticalLayout_21.addWidget(self.frame_108)


        self.horizontalLayout_71.addWidget(self.frame_106)


        self.horizontalLayout_70.addWidget(self.frame_103)


        self.verticalLayout_2.addWidget(self.frame_102)

        self.frame_101 = QFrame(self.page_pso)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(0, 20))
        self.frame_101.setMaximumSize(QSize(16777215, 20))
        self.frame_101.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_101.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_101.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_101)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_101)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_41)


        self.verticalLayout_2.addWidget(self.frame_101)

        self.pages.addWidget(self.page_pso)
        self.page_calibration_status = QWidget()
        self.page_calibration_status.setObjectName(u"page_calibration_status")
        self.page_calibration_status.setStyleSheet(u"#frame_status {\n"
"background-color: rgb(245, 245, 245);\n"
"border-radius: 20px;\n"
"border: 2px solid rgb(156, 156, 156); /* Definindo a cor e espessura da borda */}\n"
"\n"
"/* QPushButton*/\n"
"#button_code_tracking_back, #button_code_tracking_next_page {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_code_tracking_back:hover, #button_code_tracking_next_page:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_code_tracking_back:pressed, #button_code_tracking_next_page:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"")
        self.verticalLayout_67 = QVBoxLayout(self.page_calibration_status)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_134 = QFrame(self.page_calibration_status)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setMinimumSize(QSize(0, 70))
        self.frame_134.setMaximumSize(QSize(16777215, 70))
        self.frame_134.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_134.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_134.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_134)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.icon_interface_9 = QLabel(self.frame_134)
        self.icon_interface_9.setObjectName(u"icon_interface_9")
        self.icon_interface_9.setMinimumSize(QSize(50, 50))
        self.icon_interface_9.setMaximumSize(QSize(50, 50))
        self.icon_interface_9.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_9.setScaledContents(True)

        self.horizontalLayout_101.addWidget(self.icon_interface_9)

        self.interface_name_9 = QLabel(self.frame_134)
        self.interface_name_9.setObjectName(u"interface_name_9")
        self.interface_name_9.setFont(font)
        self.interface_name_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_101.addWidget(self.interface_name_9)


        self.verticalLayout_67.addWidget(self.frame_134)

        self.frame_121 = QFrame(self.page_calibration_status)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_121.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_121.setLineWidth(0)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.frame_123 = QFrame(self.frame_121)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMaximumSize(QSize(16777215, 16777215))
        self.frame_123.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.frame_124 = QFrame(self.frame_123)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMaximumSize(QSize(16777215, 16777215))
        self.frame_124.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_124.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_124)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_status = QFrame(self.frame_124)
        self.frame_status.setObjectName(u"frame_status")
        self.frame_status.setMaximumSize(QSize(16777215, 16777215))
        self.frame_status.setStyleSheet(u"")
        self.frame_status.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_status.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_status)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.frame_status)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 819, 925))
        self.verticalLayout_60 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_code_status = QLabel(self.scrollAreaWidgetContents)
        self.label_code_status.setObjectName(u"label_code_status")
        self.label_code_status.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_60.addWidget(self.label_code_status)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_59.addWidget(self.scrollArea)


        self.verticalLayout_58.addWidget(self.frame_status)

        self.frame_132 = QFrame(self.frame_124)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMinimumSize(QSize(0, 60))
        self.frame_132.setMaximumSize(QSize(16777215, 60))
        self.frame_132.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_132.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_132)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.button_code_tracking_back = QPushButton(self.frame_132)
        self.button_code_tracking_back.setObjectName(u"button_code_tracking_back")
        self.button_code_tracking_back.setMinimumSize(QSize(100, 38))
        self.button_code_tracking_back.setMaximumSize(QSize(100, 38))
        self.button_code_tracking_back.setStyleSheet(u"")

        self.horizontalLayout_100.addWidget(self.button_code_tracking_back)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_5)

        self.button_code_tracking_next_page = QPushButton(self.frame_132)
        self.button_code_tracking_next_page.setObjectName(u"button_code_tracking_next_page")
        self.button_code_tracking_next_page.setMinimumSize(QSize(100, 38))
        self.button_code_tracking_next_page.setMaximumSize(QSize(100, 38))
        self.button_code_tracking_next_page.setStyleSheet(u"")

        self.horizontalLayout_100.addWidget(self.button_code_tracking_next_page)


        self.verticalLayout_58.addWidget(self.frame_132)


        self.horizontalLayout_89.addWidget(self.frame_124)


        self.horizontalLayout_72.addWidget(self.frame_123)


        self.verticalLayout_67.addWidget(self.frame_121)

        self.frame_133 = QFrame(self.page_calibration_status)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setMinimumSize(QSize(0, 20))
        self.frame_133.setMaximumSize(QSize(16777215, 20))
        self.frame_133.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_133.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_133.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_133)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_133)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_66.addWidget(self.label_57)


        self.verticalLayout_67.addWidget(self.frame_133)

        self.pages.addWidget(self.page_calibration_status)
        self.page_results = QWidget()
        self.page_results.setObjectName(u"page_results")
        self.page_results.setStyleSheet(u"/*QFrame*/\n"
"#frame_results_graph {\n"
"background-color: rgb(245, 245, 245);\n"
"border-radius: 20px;\n"
"border: 2px solid rgb(156, 156, 156);}\n"
"\n"
"\n"
"/* QPushButton*/\n"
"#button_result_next_page, #button_result_back {\n"
"background-color: rgb(248, 248, 248);\n"
"border: 1px solid rgb(182, 182, 182);\n"
"border-radius: 5px}\n"
"\n"
"#button_result_next_page:hover, #button_result_back:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(60, 130, 240, 255), stop:1 rgba(70, 110, 187, 255));}\n"
"\n"
"#button_result_next_page:pressed, #button_result_back:pressed {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
"\n"
"\n"
"/* QLabel and QLineEdit*/\n"
"#label_steady_fc, #label_steady_fn, #label_steady_temp, #label_steady_ccr, #label_steady_csr {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-r"
                        "adius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}\n"
"\n"
"\n"
"")
        self.verticalLayout_71 = QVBoxLayout(self.page_results)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.frame_146 = QFrame(self.page_results)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setMinimumSize(QSize(0, 70))
        self.frame_146.setMaximumSize(QSize(16777215, 70))
        self.frame_146.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_146.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_146.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.icon_interface_11 = QLabel(self.frame_146)
        self.icon_interface_11.setObjectName(u"icon_interface_11")
        self.icon_interface_11.setMinimumSize(QSize(50, 50))
        self.icon_interface_11.setMaximumSize(QSize(50, 50))
        self.icon_interface_11.setPixmap(QPixmap(u":/folder1/Icons/programmer.png"))
        self.icon_interface_11.setScaledContents(True)

        self.horizontalLayout_105.addWidget(self.icon_interface_11)

        self.interface_name_11 = QLabel(self.frame_146)
        self.interface_name_11.setObjectName(u"interface_name_11")
        self.interface_name_11.setFont(font)
        self.interface_name_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.interface_name_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_105.addWidget(self.interface_name_11)


        self.verticalLayout_71.addWidget(self.frame_146)

        self.frame_125 = QFrame(self.page_results)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_125.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_125.setLineWidth(0)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_125)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.frame_128 = QFrame(self.frame_125)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMaximumSize(QSize(16777215, 16777215))
        self.frame_128.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_128)
        self.horizontalLayout_93.setSpacing(10)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.frame_129 = QFrame(self.frame_128)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setMaximumSize(QSize(16777215, 16777215))
        self.frame_129.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_129.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_129)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.frame_results_graph = QFrame(self.frame_129)
        self.frame_results_graph.setObjectName(u"frame_results_graph")
        self.frame_results_graph.setMinimumSize(QSize(0, 0))
        self.frame_results_graph.setMaximumSize(QSize(16777215, 16777215))
        self.frame_results_graph.setStyleSheet(u"")
        self.frame_results_graph.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_results_graph.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_results_graph)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(5, 5, 5, 5)
        self.frame_20 = QFrame(self.frame_results_graph)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_65.addWidget(self.frame_20)


        self.verticalLayout_64.addWidget(self.frame_results_graph)


        self.horizontalLayout_93.addWidget(self.frame_129)

        self.frame_137 = QFrame(self.frame_128)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setMinimumSize(QSize(0, 0))
        self.frame_137.setMaximumSize(QSize(500, 16777215))
        self.frame_137.setStyleSheet(u"")
        self.frame_137.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_137.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_137)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_161 = QFrame(self.frame_137)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMaximumSize(QSize(16777215, 16777215))
        self.frame_161.setStyleSheet(u"")
        self.frame_161.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_161.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_161)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(15, -1, 15, 9)
        self.frame_131 = QFrame(self.frame_161)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setStyleSheet(u"")
        self.frame_131.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_131)
        self.verticalLayout_73.setSpacing(15)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.frame_150 = QFrame(self.frame_131)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setMinimumSize(QSize(0, 80))
        self.frame_150.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_150)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.frame_151 = QFrame(self.frame_150)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_151)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(1, 0, 0, 0)
        self.label_142 = QLabel(self.frame_151)
        self.label_142.setObjectName(u"label_142")
        font9 = QFont()
        font9.setFamilies([u"Yu Gothic UI Semilight"])
        font9.setPointSize(14)
        font9.setBold(True)
        self.label_142.setFont(font9)
        self.label_142.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_82.addWidget(self.label_142)


        self.verticalLayout_81.addWidget(self.frame_151)

        self.frame_152 = QFrame(self.frame_150)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_152)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.combobox_analysis_type = QComboBox(self.frame_152)
        self.combobox_analysis_type.addItem("")
        self.combobox_analysis_type.addItem("")
        self.combobox_analysis_type.addItem("")
        self.combobox_analysis_type.addItem("")
        self.combobox_analysis_type.addItem("")
        self.combobox_analysis_type.setObjectName(u"combobox_analysis_type")
        self.combobox_analysis_type.setEnabled(True)
        self.combobox_analysis_type.setMinimumSize(QSize(0, 20))
        self.combobox_analysis_type.setMaximumSize(QSize(16777215, 20))
        self.combobox_analysis_type.setStyleSheet(u"")

        self.verticalLayout_83.addWidget(self.combobox_analysis_type)


        self.verticalLayout_81.addWidget(self.frame_152)


        self.verticalLayout_73.addWidget(self.frame_150)

        self.frame_148 = QFrame(self.frame_131)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setMinimumSize(QSize(0, 80))
        self.frame_148.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_148)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.frame_147 = QFrame(self.frame_148)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_147)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(1, 0, 0, 0)
        self.label_141 = QLabel(self.frame_147)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setFont(font9)
        self.label_141.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_78.addWidget(self.label_141)


        self.verticalLayout_79.addWidget(self.frame_147)

        self.frame_149 = QFrame(self.frame_148)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_149)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.combobox_file = QComboBox(self.frame_149)
        self.combobox_file.addItem("")
        self.combobox_file.setObjectName(u"combobox_file")
        self.combobox_file.setEnabled(True)
        self.combobox_file.setMinimumSize(QSize(0, 20))
        self.combobox_file.setMaximumSize(QSize(16777215, 20))
        self.combobox_file.setStyleSheet(u"")

        self.verticalLayout_80.addWidget(self.combobox_file)


        self.verticalLayout_79.addWidget(self.frame_149)


        self.verticalLayout_73.addWidget(self.frame_148)

        self.verticalSpacer_12 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_73.addItem(self.verticalSpacer_12)

        self.frame_156 = QFrame(self.frame_131)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setMinimumSize(QSize(0, 150))
        self.frame_156.setStyleSheet(u"")
        self.frame_156.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_156)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.frame_157 = QFrame(self.frame_156)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_157)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(1, -1, -1, -1)
        self.label_144 = QLabel(self.frame_157)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setFont(font9)
        self.label_144.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_88.addWidget(self.label_144)


        self.verticalLayout_87.addWidget(self.frame_157)

        self.results_fc = QFrame(self.frame_156)
        self.results_fc.setObjectName(u"results_fc")
        font10 = QFont()
        font10.setPointSize(10)
        self.results_fc.setFont(font10)
        self.results_fc.setFrameShape(QFrame.Shape.StyledPanel)
        self.results_fc.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.results_fc)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.label_150 = QLabel(self.results_fc)
        self.label_150.setObjectName(u"label_150")

        self.horizontalLayout_96.addWidget(self.label_150)

        self.label_steady_fc = QLabel(self.results_fc)
        self.label_steady_fc.setObjectName(u"label_steady_fc")
        self.label_steady_fc.setMinimumSize(QSize(65, 20))
        self.label_steady_fc.setMaximumSize(QSize(65, 20))
        self.label_steady_fc.setStyleSheet(u"")
        self.label_steady_fc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_96.addWidget(self.label_steady_fc)


        self.verticalLayout_87.addWidget(self.results_fc)

        self.results_fn = QFrame(self.frame_156)
        self.results_fn.setObjectName(u"results_fn")
        self.results_fn.setFrameShape(QFrame.Shape.StyledPanel)
        self.results_fn.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.results_fn)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.label_151 = QLabel(self.results_fn)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font10)

        self.horizontalLayout_97.addWidget(self.label_151)

        self.label_steady_fn = QLabel(self.results_fn)
        self.label_steady_fn.setObjectName(u"label_steady_fn")
        self.label_steady_fn.setMinimumSize(QSize(65, 20))
        self.label_steady_fn.setMaximumSize(QSize(65, 20))
        self.label_steady_fn.setStyleSheet(u"")
        self.label_steady_fn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_97.addWidget(self.label_steady_fn)


        self.verticalLayout_87.addWidget(self.results_fn)

        self.results_temp = QFrame(self.frame_156)
        self.results_temp.setObjectName(u"results_temp")
        self.results_temp.setFrameShape(QFrame.Shape.StyledPanel)
        self.results_temp.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.results_temp)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.label_152 = QLabel(self.results_temp)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setFont(font10)

        self.horizontalLayout_98.addWidget(self.label_152)

        self.label_steady_temp = QLabel(self.results_temp)
        self.label_steady_temp.setObjectName(u"label_steady_temp")
        self.label_steady_temp.setMinimumSize(QSize(65, 20))
        self.label_steady_temp.setMaximumSize(QSize(65, 20))
        self.label_steady_temp.setStyleSheet(u"")
        self.label_steady_temp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_98.addWidget(self.label_steady_temp)


        self.verticalLayout_87.addWidget(self.results_temp)

        self.results_ccr = QFrame(self.frame_156)
        self.results_ccr.setObjectName(u"results_ccr")
        self.results_ccr.setFrameShape(QFrame.Shape.StyledPanel)
        self.results_ccr.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_164 = QHBoxLayout(self.results_ccr)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.label_155 = QLabel(self.results_ccr)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setFont(font10)

        self.horizontalLayout_164.addWidget(self.label_155)

        self.label_steady_ccr = QLabel(self.results_ccr)
        self.label_steady_ccr.setObjectName(u"label_steady_ccr")
        self.label_steady_ccr.setMinimumSize(QSize(65, 20))
        self.label_steady_ccr.setMaximumSize(QSize(65, 20))
        self.label_steady_ccr.setStyleSheet(u"")
        self.label_steady_ccr.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_164.addWidget(self.label_steady_ccr)


        self.verticalLayout_87.addWidget(self.results_ccr)

        self.results_csr = QFrame(self.frame_156)
        self.results_csr.setObjectName(u"results_csr")
        self.results_csr.setFrameShape(QFrame.Shape.StyledPanel)
        self.results_csr.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_165 = QHBoxLayout(self.results_csr)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.label_156 = QLabel(self.results_csr)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setFont(font10)

        self.horizontalLayout_165.addWidget(self.label_156)

        self.label_steady_csr = QLabel(self.results_csr)
        self.label_steady_csr.setObjectName(u"label_steady_csr")
        self.label_steady_csr.setMinimumSize(QSize(65, 20))
        self.label_steady_csr.setMaximumSize(QSize(65, 20))
        self.label_steady_csr.setStyleSheet(u"")
        self.label_steady_csr.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_165.addWidget(self.label_steady_csr)


        self.verticalLayout_87.addWidget(self.results_csr)


        self.verticalLayout_73.addWidget(self.frame_156)


        self.verticalLayout_74.addWidget(self.frame_131)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_74.addItem(self.verticalSpacer_13)

        self.frame_130 = QFrame(self.frame_161)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setMinimumSize(QSize(0, 60))
        self.frame_130.setMaximumSize(QSize(16777215, 60))
        self.frame_130.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_130)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.button_result_back = QPushButton(self.frame_130)
        self.button_result_back.setObjectName(u"button_result_back")
        self.button_result_back.setMinimumSize(QSize(100, 38))
        self.button_result_back.setMaximumSize(QSize(100, 38))
        self.button_result_back.setStyleSheet(u"")

        self.horizontalLayout_94.addWidget(self.button_result_back)


        self.verticalLayout_74.addWidget(self.frame_130)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_74.addItem(self.verticalSpacer_2)


        self.verticalLayout_72.addWidget(self.frame_161)


        self.horizontalLayout_93.addWidget(self.frame_137)


        self.horizontalLayout_92.addWidget(self.frame_128)


        self.verticalLayout_71.addWidget(self.frame_125)

        self.frame_135 = QFrame(self.page_results)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMinimumSize(QSize(0, 20))
        self.frame_135.setMaximumSize(QSize(16777215, 20))
        self.frame_135.setStyleSheet(u"color: rgb(113, 113, 113);")
        self.frame_135.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_135.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_135)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.frame_135)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_69.addWidget(self.label_61)


        self.verticalLayout_71.addWidget(self.frame_135)

        self.pages.addWidget(self.page_results)

        self.verticalLayout.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 851, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(12)
        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MMCA", None))
        self.icon_interface_3.setText("")
        self.interface_name_3.setText(QCoreApplication.translate("MainWindow", u"MATERIAL OTIMIZATION", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit_project_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.button_login_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface.setText("")
        self.interface_name.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Select Abaqus Path:", None))
        self.label_abaqus.setText("")
        self.button_abaqus.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select the result folder:", None))
        self.label_result.setText("")
        self.button_settings_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_4.setText("")
        self.interface_name_4.setText(QCoreApplication.translate("MainWindow", u"CONDITIONS", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; font-weight:700;\">Attention:</span></p><p align=\"justify\"><span style=\" font-size:11pt; color:#f5f5f5;\">. . </span><span style=\" font-size:11pt;\">The number of cutting conditions directly affects the calibration time and the convergence of the PSO algorithm. It is recommended to use four conditions, as a higher number may significantly increase processing time and hinder convergence to an optimized result. In the next step, you should choose the outputs you want to analyze and assign a respective weight to each one to calculate the error.</span></p></body></html>", None))
        self.button_conditions_limitation_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_conditions_limitation_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_13.setText("")
        self.interface_name_13.setText(QCoreApplication.translate("MainWindow", u"CONDITIONS", None))
        self.chip.setText(QCoreApplication.translate("MainWindow", u"Chip Shape", None))
        self.temperature.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.forces.setText(QCoreApplication.translate("MainWindow", u"Forces", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"<body>\n"
"    <p align=\"left\">\n"
"        <b>Error:</b><br>\n"
"        ( (w<sub>fc</sub> \u00b7 \u03b5<sub>fc</sub><sup>2</sup>) +\n"
"        (w<sub>fn</sub> \u00b7 \u03b5<sub>fn</sub><sup>2</sup>) +\n"
"        (w<sub>t</sub> \u00b7 \u03b5<sub>t</sub><sup>2</sup>) +\n"
"        (w<sub>ccr</sub> \u00b7 \u03b5<sub>ccr</sub><sup>2</sup>) +\n"
"        (w<sub>csr</sub> \u00b7 \u03b5<sub>csr</sub><sup>2</sup>) )<sup>0.5</sup>\n"
"    </p>\n"
"</body>\n"
"</html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"W_Fc", None))
        self.wfc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"W_Fn", None))
        self.wfn.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"W_CSR", None))
        self.wcsr.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"W_CCR", None))
        self.wccr.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"W_Temp", None))
        self.wt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_output_analysis_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_output_analysis_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_10.setText("")
        self.interface_name_10.setText(QCoreApplication.translate("MainWindow", u"CONDITIONS", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; font-weight:700;\">Attention:</span></p><p align=\"justify\"><span style=\" font-size:11pt; color:#f5f5f5;\">. . </span><span style=\" font-size:11pt;\">You have two options: either import your </span><span style=\" font-family:'Courier New'; font-size:11pt;\">.inp</span><span style=\" font-size:11pt;\"> file containing setup information such as geometry and meshes, or use the setup creator provided by the software.</span></p><p align=\"justify\"><span style=\" font-size:11pt;\"><br/></span><span style=\" font-size:11pt; color:#f5f5f5;\">. . </span><span style=\" font-size:11pt;\">There are some limitations when generating the setup using this software, as only basic geometry parameters can be modified.</span></p><p align=\"justify\"><span style=\" font-size:11pt;\"><br/></span><span style=\" font-size:11pt; color:#f5f5f5;\">. . </span><span style=\" font-size:11pt;\">Additionally, if you choose to import the </span><span style=\" font-fami"
                        "ly:'Courier New'; font-size:11pt;\">.inp</span><span style=\" font-size:11pt;\"> file, you must follow the guidelines defined in the document </span><span style=\" font-size:11pt; font-weight:700;\">&quot;guidelines-for-creating-setup.pdf&quot;</span><span style=\" font-size:11pt;\">.</span></p></body></html>", None))
        self.button_import_inp.setText(QCoreApplication.translate("MainWindow", u"Import .inp", None))
        self.button_create_geometry.setText(QCoreApplication.translate("MainWindow", u"Create Geometry", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_12.setText("")
        self.interface_name_12.setText(QCoreApplication.translate("MainWindow", u"GEOMETRY SETTINGS", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Part Information", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"Height (mm):", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Width (mm):", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Trickness (mm):", None))
        self.eulerianName.setText(QCoreApplication.translate("MainWindow", u"Eulerian", None))
        self.eulerianName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.eulerianHeight.setText("")
        self.eulerianHeight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.eulerianWidth.setText("")
        self.eulerianWidth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.eulerianTrickness.setText("")
        self.eulerianTrickness.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Partition Position", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"X1:", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"X2:", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"X3:", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"X4:", None))
        self.eulerianPartitionX1.setText("")
        self.eulerianPartitionX1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionX2.setText("")
        self.eulerianPartitionX2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionX3.setText("")
        self.eulerianPartitionX3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionX4.setText("")
        self.eulerianPartitionX4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Y1:", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"Y2:", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Y3:", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Y4:", None))
        self.eulerianPartitionY1.setText("")
        self.eulerianPartitionY1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionY2.setText("")
        self.eulerianPartitionY2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionY3.setText("")
        self.eulerianPartitionY3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.eulerianPartitionY4.setText("")
        self.eulerianPartitionY4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"position", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Mesh Information", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor:", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Minimum Factor:", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.eulerianGlobalSize.setText("")
        self.eulerianGlobalSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.eulerianDeviationFactor.setText("")
        self.eulerianDeviationFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.eulerianMininumFactor.setText("")
        self.eulerianMininumFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.eulerianOtherInfo.setText("")
        self.eulerianOtherInfo.setPlaceholderText("")
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.eulerianOtherInfo_7.setText("")
        self.eulerianOtherInfo_7.setPlaceholderText("")
        self.eulerianOtherInfo_8.setText("")
        self.eulerianOtherInfo_8.setPlaceholderText("")
        self.eulerianOtherInfo_9.setText("")
        self.eulerianOtherInfo_9.setPlaceholderText("")
        self.eulerianOtherInfo_10.setText("")
        self.eulerianOtherInfo_10.setPlaceholderText("")
        self.eulerianWarning.setText("")
        self.defautValues.setText(QCoreApplication.translate("MainWindow", u"Use defaut values", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eulerianTab), QCoreApplication.translate("MainWindow", u"Eulerian", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Part Information", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Height (mm):", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Width (mm):", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Trickness (mm): ", None))
        self.chipName.setText(QCoreApplication.translate("MainWindow", u"ChipPlate", None))
        self.chipName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.chipHeight.setText("")
        self.chipHeight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.chipWidth.setText("")
        self.chipWidth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.chipTrickness.setText("")
        self.chipTrickness.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a dimension", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Mesh Information", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor:", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Minimum Factor:", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.chipGlobalSize.setText("")
        self.chipGlobalSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.chipDeviationFactor.setText("")
        self.chipDeviationFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.chipMininumFactor.setText("")
        self.chipMininumFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.chipOtherInfo.setText("")
        self.chipOtherInfo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.chipWarning.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chipPlayeTab), QCoreApplication.translate("MainWindow", u"Chip Plate", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Part Information", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"Trickness (mm):", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"Rake Angle:", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Rake Dimension (mm):", None))
        self.toolName.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.toolName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a name for the part", None))
        self.toolTrickness.setText("")
        self.toolTrickness.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolRakeAngle.setText("")
        self.toolRakeAngle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolRakeDimension.setText("")
        self.toolRakeDimension.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Clerance Angle:", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"Clearance Dimension (mm):", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"Radius:", None))
        self.label_193.setText("")
        self.toolClearanceAngle.setText("")
        self.toolClearanceAngle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolClearanceDimension.setText("")
        self.toolClearanceDimension.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolRadius.setText("")
        self.toolRadius.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_194.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Partition Information", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"Size Partition 01:", None))
        self.toolPartition01.setText("")
        self.toolPartition01.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"Size Partiton 02", None))
        self.toolPartition02.setText("")
        self.toolPartition02.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Mesh Information", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Global Size:", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"Deviation Factor:", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"Minimum Factor:", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.toolGlobalSize.setText("")
        self.toolGlobalSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolDeviationFactor.setText("")
        self.toolDeviationFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolMinimumFactor.setText("")
        self.toolMinimumFactor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo.setText("")
        self.toolOthersInfo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"Others Mesh Info:", None))
        self.toolOthersInfo_7.setText("")
        self.toolOthersInfo_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo_8.setText("")
        self.toolOthersInfo_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo_9.setText("")
        self.toolOthersInfo_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolOthersInfo_10.setText("")
        self.toolOthersInfo_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.toolWarning.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.toolTab), QCoreApplication.translate("MainWindow", u"Tool", None))
#if QT_CONFIG(whatsthis)
        self.tabWidget.setTabWhatsThis(self.tabWidget.indexOf(self.toolTab), QCoreApplication.translate("MainWindow", u"yyyyyyyyyyyyyyy", None))
#endif // QT_CONFIG(whatsthis)
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Eulerian Position", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.xEulerian.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.xEulerian.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.yEulerian.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.yEulerian.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Tool Position", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.xTool.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.xTool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.yTool.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.yTool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Chip Plate Position", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Clearance Over Workpiece (mm):", None))
        self.overWorkpiece.setText("")
        self.overWorkpiece.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Distance From Tool (mm):", None))
        self.fromTool.setText("")
        self.fromTool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Others Informations", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Depth of cut (mm):", None))
        self.feed.setText("")
        self.feed.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Time Period:", None))
        self.timePeriod.setText("")
        self.timePeriod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"value", None))
        self.assemblyWarning.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.assemblyTab), QCoreApplication.translate("MainWindow", u"Assembly", None))
        self.button_create_geometry_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_create_geometry_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.button_create_geometry_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_2.setText("")
        self.interface_name_2.setText(QCoreApplication.translate("MainWindow", u"CONDITIONS", None))
        self.comboBox_condition.setCurrentText("")
        self.comboBox_condition.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select the Condition", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"mm/s", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Deep of Cuth", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Rake Angle", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Temperature path", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Input File", None))
        self.label_input.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Experimental Values", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Cutting Force", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Normal Cutting Force", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Chip Segmentation Ratio", None))
        self.label_29.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Chip Compression Rate", None))
        self.label_27.setText("")
        self.button_conditions_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_newCondition.setText(QCoreApplication.translate("MainWindow", u"New Condition", None))
        self.button_conditions_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_5.setText("")
        self.interface_name_5.setText(QCoreApplication.translate("MainWindow", u"PARAMETER SELECTION", None))
        self.comboBox_material.setCurrentText("")
        self.comboBox_material.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select the Material", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Plastic", None))
        self.checkBox_param_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_param_A.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_param_B.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_n.setText(QCoreApplication.translate("MainWindow", u"n", None))
        self.label_param_n.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_C1.setText(QCoreApplication.translate("MainWindow", u"C1", None))
        self.label_param_C1.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_C2.setText(QCoreApplication.translate("MainWindow", u"C2", None))
        self.label_param_C2.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_C3.setText(QCoreApplication.translate("MainWindow", u"C3", None))
        self.label_param_C3.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_e.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.label_param_e.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_k.setText(QCoreApplication.translate("MainWindow", u"k", None))
        self.label_param_k.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_Ts.setText(QCoreApplication.translate("MainWindow", u"Ts", None))
        self.label_param_Ts.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Damage", None))
        self.checkBox_param_D1.setText(QCoreApplication.translate("MainWindow", u"D1", None))
        self.label_param_D1.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_D2.setText(QCoreApplication.translate("MainWindow", u"D2", None))
        self.label_param_D2.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_D3.setText(QCoreApplication.translate("MainWindow", u"D3", None))
        self.label_param_D3.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_D4.setText(QCoreApplication.translate("MainWindow", u"D4", None))
        self.label_param_D4.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_D5.setText(QCoreApplication.translate("MainWindow", u"D5", None))
        self.label_param_D5.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_Tm.setText(QCoreApplication.translate("MainWindow", u"Tm", None))
        self.label_param_Tm.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_Tt.setText(QCoreApplication.translate("MainWindow", u"Tt", None))
        self.label_param_Tt.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_e_damage.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.label_param_e_damage.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.checkBox_param_p.setText(QCoreApplication.translate("MainWindow", u"p", None))
        self.label_param_p.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.button_parameter_selection_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_parameter_selection_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_6.setText("")
        self.interface_name_6.setText(QCoreApplication.translate("MainWindow", u"PARAMETER LIMITS", None))
        self.comboBox_material_limits.setCurrentText("")
        self.comboBox_material_limits.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select the Material", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Plastic", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lineEdit_min_param_A.setText("")
        self.lineEdit_min_param_A.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_A.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lineEdit_min_param_B.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_B.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"n", None))
        self.lineEdit_min_param_n.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_n.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"C1", None))
        self.lineEdit_min_param_C1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_C1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"C2", None))
        self.lineEdit_min_param_C2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_C2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"C3", None))
        self.lineEdit_min_param_C3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_C3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.lineEdit_min_param_e.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_e.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"k", None))
        self.lineEdit_min_param_k.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_k.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Ts", None))
        self.lineEdit_min_param_Ts.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_Ts.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Damage", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"D1", None))
        self.lineEdit_min_param_D1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_D1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"D2", None))
        self.lineEdit_min_param_D2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_D2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"D3", None))
        self.lineEdit_min_param_D3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_D3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"D4", None))
        self.lineEdit_min_param_D4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_D4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"D5", None))
        self.lineEdit_min_param_D5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_D5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Tm", None))
        self.lineEdit_min_param_Tm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_Tm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Tt", None))
        self.lineEdit_min_param_Tt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_Tt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.lineEdit_min_param_e_damage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_e_damage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"p", None))
        self.lineEdit_min_param_p.setPlaceholderText(QCoreApplication.translate("MainWindow", u"min", None))
        self.lineEdit_max_param_p.setPlaceholderText(QCoreApplication.translate("MainWindow", u"max", None))
        self.button_parameter_limits_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_parameter_limits_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_8.setText("")
        self.interface_name_8.setText(QCoreApplication.translate("MainWindow", u"PARTICLE SWARM OPTIMIZATION", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Particle Swarm Optimization (PSO):</span></p><p align=\"justify\"><span style=\" font-size:11pt; color:#f5f5f5;\">. . </span><span style=\" font-size:11pt;\">It's an optimization algorithm inspired by the collective behavior of organisms like birds or fish. It uses a population of particles, each representing a potential solution. Each particle updates its position based on its personal best solution and the global best. PSO is effective for material model calibration, as it explores large parameter spaces to find solutions that minimize the difference between experimental and simulated data.</span></p><p align=\"justify\"><br/><span style=\" font-size:11pt; font-weight:700;\">w (inertia)</span><span style=\" font-size:11pt;\">: Controls the tendency of particles to maintain their previous velocities, balancing global and local exploration.</span><br/></p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:700;\">c1 (cognitive "
                        "coefficient)</span><span style=\" font-size:11pt;\">: Determines the attraction of a particle to its own best-found solution, encouraging local exploration.</span></p><p align=\"justify\"><br/><span style=\" font-size:11pt; font-weight:700;\">c2 (social coefficient)</span><span style=\" font-size:11pt;\">: Controls the attraction to the global best solution, promoting collaboration between particles and global exploration.</span></p></body></html>", None))
        self.button_pso_explanation_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_pso_explanation_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_7.setText("")
        self.interface_name_7.setText(QCoreApplication.translate("MainWindow", u"PARTICLE SWARM OPTIMIZATION", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Particle Swarm Optimization</span></p></body></html>", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Number of Cutting Conditions:", None))
        self.label_number_conditions.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Number of Iterations:", None))
        self.lineEdit_number_iteration.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.lineEdit_number_iteration.setPlaceholderText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Number of Particles:", None))
        self.lineEdit_number_particles.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.lineEdit_number_particles.setPlaceholderText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"w:", None))
        self.lineEdit_var2.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.lineEdit_var2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"c1:", None))
        self.lineEdit_var3.setText(QCoreApplication.translate("MainWindow", u"2.0", None))
        self.lineEdit_var3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2.0", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"c2:", None))
        self.lineEdit_var1.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.lineEdit_var1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2.0", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Simulation</span></p></body></html>", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Cores Available:", None))
        self.label_cores.setText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Cores by simulation:", None))
        self.combobox_core_by_simulation.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.combobox_core_by_simulation.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.combobox_core_by_simulation.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.combobox_core_by_simulation.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.combobox_core_by_simulation.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.combobox_core_by_simulation.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.combobox_core_by_simulation.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.combobox_core_by_simulation.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.combobox_core_by_simulation.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))

        self.combobox_core_by_simulation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"How many computers will be used?", None))
        self.combobox_number_computer.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.combobox_number_computer.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.combobox_number_computer.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.combobox_number_computer.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.combobox_number_computer.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.combobox_number_computer.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))

        self.combobox_number_computer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Do you want to use this computer to run simulations?", None))
        self.combobox_main_computer.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.combobox_main_computer.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.combobox_main_computer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.button_pso_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_pso_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_9.setText("")
        self.interface_name_9.setText(QCoreApplication.translate("MainWindow", u"CODE TRACKING", None))
        self.label_code_status.setText("")
        self.button_code_tracking_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_code_tracking_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_11.setText("")
        self.interface_name_11.setText(QCoreApplication.translate("MainWindow", u"RESULTS", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Type of analysis:", None))
        self.combobox_analysis_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Convergence Analysis", None))
        self.combobox_analysis_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Forces", None))
        self.combobox_analysis_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Chip Format", None))
        self.combobox_analysis_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Temperature vs. Time", None))
        self.combobox_analysis_type.setItemText(4, QCoreApplication.translate("MainWindow", u"Temperature vs. Penetration Depth", None))

        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Select files", None))
        self.combobox_file.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Cutting Force:", None))
        self.label_steady_fc.setText("")
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Normal Force:", None))
        self.label_steady_fn.setText("")
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.label_steady_temp.setText("")
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Chip Compression Ratio:", None))
        self.label_steady_ccr.setText("")
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Chip Segmentation Ratio:", None))
        self.label_steady_csr.setText("")
        self.button_result_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
    # retranslateUi

