# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwhEhcj.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(1000, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(-100, -70, 1171, 781))
        self.background.setStyleSheet(u"background:rgb(255, 235, 162)")
        self.helmet_image = QLabel(self.centralwidget)
        self.helmet_image.setObjectName(u"helmet_image")
        self.helmet_image.setGeometry(QRect(770, 31, 111, 121))
        self.helmet_image.setPixmap(QPixmap(u":/helmet/helmet.png"))
        self.helmet_image.setScaledContents(True)
        self.helmet_image.setWordWrap(False)
        self.head_image = QLabel(self.centralwidget)
        self.head_image.setObjectName(u"head_image")
        self.head_image.setGeometry(QRect(770, 291, 111, 101))
        self.head_image.setPixmap(QPixmap(u":/head/man-hair.png"))
        self.head_image.setScaledContents(True)
        self.helmet_count = QLabel(self.centralwidget)
        self.helmet_count.setObjectName(u"helmet_count")
        self.helmet_count.setGeometry(QRect(790, 151, 67, 51))
        font = QFont()
        font.setPointSize(32)
        self.helmet_count.setFont(font)
        self.helmet_count.setTextFormat(Qt.AutoText)
        self.helmet_count.setScaledContents(False)
        self.helmet_count.setAlignment(Qt.AlignCenter)
        self.head_count = QLabel(self.centralwidget)
        self.head_count.setObjectName(u"head_count")
        self.head_count.setGeometry(QRect(790, 411, 67, 51))
        self.head_count.setFont(font)
        self.head_count.setTextFormat(Qt.AutoText)
        self.head_count.setScaledContents(False)
        self.head_count.setAlignment(Qt.AlignCenter)
        self.warning_label = QLabel(self.centralwidget)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setGeometry(QRect(680, 510, 291, 31))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.warning_label.setFont(font1)
        self.warning_label.setStyleSheet(u"")
        self.warning_label.setAlignment(Qt.AlignCenter)
        self.webcam_label = QLabel(self.centralwidget)
        self.webcam_label.setObjectName(u"webcam_label")
        self.webcam_label.setGeometry(QRect(30, -30, 640, 640))
        self.webcam_label.setMinimumSize(QSize(640, 640))
        self.webcam_label.setMaximumSize(QSize(640, 640))
        self.webcam_label.setScaledContents(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.background.setText("")
        self.helmet_image.setText("")
        self.head_image.setText("")
        self.helmet_count.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.head_count.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.warning_label.setText(QCoreApplication.translate("MainWindow", u"Ensure safety helmets are worn!", None))
        self.webcam_label.setText("")
    # retranslateUi

