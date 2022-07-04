# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apphlBjQf.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6 import QtGui
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
from PySide6 import QtWidgets

class Ui_MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(302, 272)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(10, 10, 281, 111))
        self.comboBox_selector_usb = QComboBox(self.groupBox)
        self.comboBox_selector_usb.setObjectName(u"comboBox_selector_usb")
        self.comboBox_selector_usb.setEnabled(True)
        self.comboBox_selector_usb.setGeometry(QRect(10, 30, 251, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_selector_usb.sizePolicy().hasHeightForWidth())
        self.comboBox_selector_usb.setSizePolicy(sizePolicy)
        self.pushButton_confirmation_usb = QPushButton(self.groupBox)
        self.pushButton_confirmation_usb.setObjectName(u"pushButton_confirmation_usb")
        self.pushButton_confirmation_usb.setEnabled(True)
        self.pushButton_confirmation_usb.setGeometry(QRect(190, 70, 75, 24))
        sizePolicy.setHeightForWidth(self.pushButton_confirmation_usb.sizePolicy().hasHeightForWidth())
        self.pushButton_confirmation_usb.setSizePolicy(sizePolicy)
        self.confirmation_label_usb = QLabel(self.groupBox)
        self.confirmation_label_usb.setObjectName(u"confirmation_label_usb")
        self.confirmation_label_usb.setGeometry(QRect(10, 70, 171, 21))
        self.confirmation_label_usb.setTextFormat(Qt.MarkdownText)
        self.confirmation_label_usb.setOpenExternalLinks(False)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 120, 281, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QRect(10, 140, 281, 81))
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 261, 16))
        self.comboBox_selector_usb_2 = QComboBox(self.groupBox_3)
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        # self.comboBox_selector_usb_2.addItem("")
        self.comboBox_selector_usb_2.setObjectName(u"comboBox_selector_usb_2")
        self.comboBox_selector_usb_2.setEnabled(True)
        self.comboBox_selector_usb_2.setGeometry(QRect(10, 40, 251, 21))
        sizePolicy.setHeightForWidth(self.comboBox_selector_usb_2.sizePolicy().hasHeightForWidth())
        self.comboBox_selector_usb_2.setSizePolicy(sizePolicy)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 302, 22))
        self.menuExtractor = QMenu(self.menubar)
        self.menuExtractor.setObjectName(u"menuExtractor")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuExtractor.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Extractor Data", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Location USB", None))
        self.pushButton_confirmation_usb.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.confirmation_label_usb.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Configuration Data", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mes actual", None))
        self.comboBox_selector_usb_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Enero", "enero"))
        self.comboBox_selector_usb_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Febrero", "febrero"))
        self.comboBox_selector_usb_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Marzo", "marzo"))
        self.comboBox_selector_usb_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Abril", "abril"))
        self.comboBox_selector_usb_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Mayo", "mayo"))
        self.comboBox_selector_usb_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Junio", "junio"))
        self.comboBox_selector_usb_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Julio", "julio"))
        self.comboBox_selector_usb_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Agosto", "agosto"))
        self.comboBox_selector_usb_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Septiembre", "septiembre"))
        self.comboBox_selector_usb_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Octubre", "octubre"))
        self.comboBox_selector_usb_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Noviembre", "noviembre"))
        self.comboBox_selector_usb_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Diciembre", "diciembre"))
        self.menuExtractor.setTitle(QCoreApplication.translate("MainWindow", u"Extractor", None))
# retranslateUi