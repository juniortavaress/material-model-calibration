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
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 1093)
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
        icon = QIcon()
        icon.addFile(u":/folder1/Icons/import.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_abaqus.setIcon(icon)
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
        self.button_result.setIcon(icon)
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
        self.page_conditions = QWidget()
        self.page_conditions.setObjectName(u"page_conditions")
        self.page_conditions.setStyleSheet(u"/* QLabel and QLineEdit*/\n"
"#label_input, #lineEdit_rakeAngle, #lineEdit_velocity, #lineEdit_tempPath, #lineEdit_deepCuth {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(113, 113, 113);}\n"
"\n"
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
"#button_conditions_next_page:pressed, #button_conditions_back:pressed,  #button_newCondition:pressed, #button_input_file:pressed {\n"
"background-color: qradialgradient(spread:pad,"
                        " cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(30, 166, 240, 255), stop:1 rgba(40, 122, 187, 255));}\n"
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
        self.frame_12.setMaximumSize(QSize(850, 300))
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
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setMaximumSize(QSize(100, 20))

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
        self.label_11.setMinimumSize(QSize(100, 0))
        self.label_11.setMaximumSize(QSize(100, 20))

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
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setMaximumSize(QSize(100, 20))

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

        self.frame_20 = QFrame(self.frame_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 30))
        self.frame_20.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_13 = QLabel(self.frame_20)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 0))
        self.label_13.setMaximumSize(QSize(100, 20))

        self.horizontalLayout_10.addWidget(self.label_13)

        self.lineEdit_tempPath = QLineEdit(self.frame_20)
        self.lineEdit_tempPath.setObjectName(u"lineEdit_tempPath")
        self.lineEdit_tempPath.setMinimumSize(QSize(0, 20))
        self.lineEdit_tempPath.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_tempPath.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lineEdit_tempPath)

        self.horizontalSpacer = QSpacerItem(40, 35, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addWidget(self.frame_20)

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
        self.label_10.setMinimumSize(QSize(100, 0))
        self.label_10.setMaximumSize(QSize(100, 20))

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
        self.button_input_file.setIcon(icon)
        self.button_input_file.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.button_input_file)


        self.verticalLayout_9.addWidget(self.frame_15)


        self.verticalLayout_10.addWidget(self.frame_13)

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
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_3.setFont(font3)

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
        self.label_19.setFont(font3)

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
        self.label_39.setFont(font3)

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
        self.label_49.setFont(font3)

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
        self.frame_110.setMaximumSize(QSize(500, 300))
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
        self.label_45.setMaximumSize(QSize(16777215, 200))
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
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.label_129.setFont(font4)

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
        self.label_131.setFont(font4)

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
        self.label_130.setFont(font4)

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
        self.label_133.setFont(font4)

        self.horizontalLayout_86.addWidget(self.label_133)

        self.lineEdit_var2 = QLineEdit(self.frame_144)
        self.lineEdit_var2.setObjectName(u"lineEdit_var2")
        self.lineEdit_var2.setMinimumSize(QSize(65, 20))
        self.lineEdit_var2.setMaximumSize(QSize(65, 20))
        self.lineEdit_var2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_86.addWidget(self.lineEdit_var2)


        self.verticalLayout_55.addWidget(self.frame_144)

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
        self.label_134.setFont(font4)

        self.horizontalLayout_87.addWidget(self.label_134)

        self.lineEdit_var1 = QLineEdit(self.frame_145)
        self.lineEdit_var1.setObjectName(u"lineEdit_var1")
        self.lineEdit_var1.setMinimumSize(QSize(65, 20))
        self.lineEdit_var1.setMaximumSize(QSize(65, 20))
        self.lineEdit_var1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_87.addWidget(self.lineEdit_var1)


        self.verticalLayout_55.addWidget(self.frame_145)

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
        self.label_132.setFont(font4)

        self.horizontalLayout_85.addWidget(self.label_132)

        self.lineEdit_var3 = QLineEdit(self.frame_143)
        self.lineEdit_var3.setObjectName(u"lineEdit_var3")
        self.lineEdit_var3.setMinimumSize(QSize(65, 20))
        self.lineEdit_var3.setMaximumSize(QSize(65, 20))
        self.lineEdit_var3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_85.addWidget(self.lineEdit_var3)


        self.verticalLayout_55.addWidget(self.frame_143)


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
        self.label_128.setFont(font4)

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
        font5 = QFont()
        font5.setBold(False)
        self.frame_139.setFont(font5)
        self.frame_139.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_72 = QLabel(self.frame_139)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font4)

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
        self.label_76.setFont(font4)

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
        self.label_74.setFont(font4)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 51, 18))
        self.verticalLayout_60 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
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
"#label_steady_fc, #label_steady_fn, #label_steady_temp {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb"
                        "(113, 113, 113);}\n"
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
        font6 = QFont()
        font6.setFamilies([u"Yu Gothic UI Semilight"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label_141.setFont(font6)
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
        self.combobox_file.addItem("")
        self.combobox_file.setObjectName(u"combobox_file")
        self.combobox_file.setEnabled(True)
        self.combobox_file.setMinimumSize(QSize(0, 20))
        self.combobox_file.setMaximumSize(QSize(16777215, 20))
        self.combobox_file.setStyleSheet(u"")

        self.verticalLayout_80.addWidget(self.combobox_file)


        self.verticalLayout_79.addWidget(self.frame_149)


        self.verticalLayout_73.addWidget(self.frame_148)

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
        self.label_142.setFont(font6)
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
        self.combobox_analysis_type.setObjectName(u"combobox_analysis_type")
        self.combobox_analysis_type.setEnabled(True)
        self.combobox_analysis_type.setMinimumSize(QSize(0, 20))
        self.combobox_analysis_type.setMaximumSize(QSize(16777215, 20))
        self.combobox_analysis_type.setStyleSheet(u"")

        self.verticalLayout_83.addWidget(self.combobox_analysis_type)


        self.verticalLayout_81.addWidget(self.frame_152)


        self.verticalLayout_73.addWidget(self.frame_150)

        self.frame_type_rf = QFrame(self.frame_131)
        self.frame_type_rf.setObjectName(u"frame_type_rf")
        self.frame_type_rf.setMinimumSize(QSize(0, 80))
        self.frame_type_rf.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_type_rf.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_type_rf)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.frame_154 = QFrame(self.frame_type_rf)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_154)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(1, -1, -1, -1)
        self.label_143 = QLabel(self.frame_154)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setFont(font6)
        self.label_143.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_85.addWidget(self.label_143)


        self.verticalLayout_84.addWidget(self.frame_154)

        self.frame_155 = QFrame(self.frame_type_rf)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_155)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.combobox_rf_type = QComboBox(self.frame_155)
        self.combobox_rf_type.addItem("")
        self.combobox_rf_type.addItem("")
        self.combobox_rf_type.addItem("")
        self.combobox_rf_type.setObjectName(u"combobox_rf_type")
        self.combobox_rf_type.setEnabled(True)
        self.combobox_rf_type.setMinimumSize(QSize(0, 20))
        self.combobox_rf_type.setMaximumSize(QSize(16777215, 20))
        self.combobox_rf_type.setStyleSheet(u"")

        self.verticalLayout_86.addWidget(self.combobox_rf_type)


        self.verticalLayout_84.addWidget(self.frame_155)


        self.verticalLayout_73.addWidget(self.frame_type_rf)

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
        self.label_144.setFont(font6)
        self.label_144.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_88.addWidget(self.label_144)


        self.verticalLayout_87.addWidget(self.frame_157)

        self.frame_158 = QFrame(self.frame_156)
        self.frame_158.setObjectName(u"frame_158")
        font7 = QFont()
        font7.setPointSize(10)
        self.frame_158.setFont(font7)
        self.frame_158.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_158)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.label_150 = QLabel(self.frame_158)
        self.label_150.setObjectName(u"label_150")

        self.horizontalLayout_96.addWidget(self.label_150)

        self.label_steady_fc = QLabel(self.frame_158)
        self.label_steady_fc.setObjectName(u"label_steady_fc")
        self.label_steady_fc.setMinimumSize(QSize(65, 20))
        self.label_steady_fc.setMaximumSize(QSize(65, 20))
        self.label_steady_fc.setStyleSheet(u"")
        self.label_steady_fc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_96.addWidget(self.label_steady_fc)


        self.verticalLayout_87.addWidget(self.frame_158)

        self.frame_159 = QFrame(self.frame_156)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_159)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.label_151 = QLabel(self.frame_159)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font7)

        self.horizontalLayout_97.addWidget(self.label_151)

        self.label_steady_fn = QLabel(self.frame_159)
        self.label_steady_fn.setObjectName(u"label_steady_fn")
        self.label_steady_fn.setMinimumSize(QSize(65, 20))
        self.label_steady_fn.setMaximumSize(QSize(65, 20))
        self.label_steady_fn.setStyleSheet(u"")
        self.label_steady_fn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_97.addWidget(self.label_steady_fn)


        self.verticalLayout_87.addWidget(self.frame_159)

        self.frame_160 = QFrame(self.frame_156)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.label_152 = QLabel(self.frame_160)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setFont(font7)

        self.horizontalLayout_98.addWidget(self.label_152)

        self.label_steady_temp = QLabel(self.frame_160)
        self.label_steady_temp.setObjectName(u"label_steady_temp")
        self.label_steady_temp.setMinimumSize(QSize(65, 20))
        self.label_steady_temp.setMaximumSize(QSize(65, 20))
        self.label_steady_temp.setStyleSheet(u"")
        self.label_steady_temp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_98.addWidget(self.label_steady_temp)


        self.verticalLayout_87.addWidget(self.frame_160)


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
        self.menubar.setGeometry(QRect(0, 0, 1060, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; font-weight:700;\">Attention:</span></p><p align=\"justify\"><span style=\" font-size:11pt; color:#f5f5f5;\">. . </span><span style=\" font-size:11pt;\">The number of cutting conditions directly affects the calibration time and the convergence of the PSO algorithm. It is recommended to use four conditions, as a higher number may significantly increase processing time and hinder convergence to an optimized result.</span></p></body></html>", None))
        self.button_conditions_limitation_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_conditions_limitation_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
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
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Particle Swarm Optimization (PSO):</span></p><p align=\"justify\"><span style=\" font-size:11pt; color:#f5f5f5;\">. . </span><span style=\" font-size:11pt;\">It's an optimization algorithm inspired by the collective behavior of organisms like birds or fish. It uses a population of particles, each representing a potential solution. Each particle updates its position based on its personal best solution and the global best. PSO is effective for material model calibration, as it explores large parameter spaces to find solutions that minimize the difference between experimental and simulated data.</span></p></body></html>", None))
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
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"fig:", None))
        self.lineEdit_var1.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.lineEdit_var1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2.0", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"fip:", None))
        self.lineEdit_var3.setText(QCoreApplication.translate("MainWindow", u"2.0", None))
        self.lineEdit_var3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2.0", None))
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
        self.button_code_tracking_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.button_code_tracking_next_page.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
        self.icon_interface_11.setText("")
        self.interface_name_11.setText(QCoreApplication.translate("MainWindow", u"RESULTS", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Select files", None))
        self.combobox_file.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.combobox_file.setItemText(1, QCoreApplication.translate("MainWindow", u"All", None))

        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Type of analysis:", None))
        self.combobox_analysis_type.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.combobox_analysis_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Forces", None))
        self.combobox_analysis_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.combobox_analysis_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Chip Format", None))

        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Select the RF:", None))
        self.combobox_rf_type.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.combobox_rf_type.setItemText(1, QCoreApplication.translate("MainWindow", u"RF1", None))
        self.combobox_rf_type.setItemText(2, QCoreApplication.translate("MainWindow", u"RF2", None))

        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Steady State Values", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Cutting Force:", None))
        self.label_steady_fc.setText("")
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Normal Force:", None))
        self.label_steady_fn.setText("")
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.label_steady_temp.setText("")
        self.button_result_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Developed by Junior Tavares, Severin Groh and Pascal Behrens", None))
    # retranslateUi

