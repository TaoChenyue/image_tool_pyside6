# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QVBoxLayout, QWidget)

from view import ImageViewer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOrigin = QAction(MainWindow)
        self.actionOrigin.setObjectName(u"actionOrigin")
        self.actionCLAHE = QAction(MainWindow)
        self.actionCLAHE.setObjectName(u"actionCLAHE")
        self.actioncut = QAction(MainWindow)
        self.actioncut.setObjectName(u"actioncut")
        self.actioncut.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.frame = QFrame(self.splitter_2)
        self.frame.setObjectName(u"frame")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame2 = QFrame(self.frame1)
        self.frame2.setObjectName(u"frame2")
        self.horizontalLayout = QHBoxLayout(self.frame2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_input = QPushButton(self.frame2)
        self.btn_input.setObjectName(u"btn_input")

        self.horizontalLayout.addWidget(self.btn_input)

        self.lb_input_nums = QLabel(self.frame2)
        self.lb_input_nums.setObjectName(u"lb_input_nums")

        self.horizontalLayout.addWidget(self.lb_input_nums)


        self.verticalLayout.addWidget(self.frame2)

        self.frame3 = QFrame(self.frame1)
        self.frame3.setObjectName(u"frame3")
        self.horizontalLayout_2 = QHBoxLayout(self.frame3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_output = QPushButton(self.frame3)
        self.btn_output.setObjectName(u"btn_output")

        self.horizontalLayout_2.addWidget(self.btn_output)

        self.lb_output_path = QLabel(self.frame3)
        self.lb_output_path.setObjectName(u"lb_output_path")

        self.horizontalLayout_2.addWidget(self.lb_output_path)


        self.verticalLayout.addWidget(self.frame3)

        self.frame_2 = QFrame(self.frame1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_last_image = QPushButton(self.frame_2)
        self.btn_last_image.setObjectName(u"btn_last_image")

        self.horizontalLayout_4.addWidget(self.btn_last_image)

        self.btn_next_image = QPushButton(self.frame_2)
        self.btn_next_image.setObjectName(u"btn_next_image")

        self.horizontalLayout_4.addWidget(self.btn_next_image)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame1)

        self.lst_files = QListWidget(self.frame)
        self.lst_files.setObjectName(u"lst_files")

        self.verticalLayout_2.addWidget(self.lst_files)

        self.splitter_2.addWidget(self.frame)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.view = ImageViewer(self.splitter)
        self.view.setObjectName(u"view")
        self.splitter.addWidget(self.view)
        self.splitter_2.addWidget(self.splitter)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionOrigin)
        self.menu.addAction(self.actionCLAHE)
        self.menu_2.addAction(self.actioncut)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5904\u7406\u5de5\u5177", None))
        self.actionOrigin.setText(QCoreApplication.translate("MainWindow", u"\u539f\u56fe", None))
        self.actionCLAHE.setText(QCoreApplication.translate("MainWindow", u"CLAHE", None))
        self.actioncut.setText(QCoreApplication.translate("MainWindow", u"\u88c1\u526a", None))
        self.btn_input.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u4ef6", None))
        self.lb_input_nums.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4e2a\u6570", None))
        self.btn_output.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u6587\u4ef6\u5939", None))
        self.lb_output_path.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.btn_last_image.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
#if QT_CONFIG(shortcut)
        self.btn_last_image.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.btn_next_image.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
#if QT_CONFIG(shortcut)
        self.btn_next_image.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u9884\u5904\u7406", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
    # retranslateUi

