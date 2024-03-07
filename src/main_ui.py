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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QSplitter, QTabWidget,
    QVBoxLayout, QWidget)

from view import ImageViewer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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

        self.btn_clearfiles = QPushButton(self.frame2)
        self.btn_clearfiles.setObjectName(u"btn_clearfiles")

        self.horizontalLayout.addWidget(self.btn_clearfiles)


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

        self.btn_origin = QPushButton(self.frame_2)
        self.btn_origin.setObjectName(u"btn_origin")

        self.horizontalLayout_4.addWidget(self.btn_origin)

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
        self.tab_transform = QTabWidget(self.splitter)
        self.tab_transform.setObjectName(u"tab_transform")
        self.tab_transform.setTabPosition(QTabWidget.North)
        self.tbw_gray = QWidget()
        self.tbw_gray.setObjectName(u"tbw_gray")
        self.gridLayout_2 = QGridLayout(self.tbw_gray)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tab_CLAHE = QTabWidget(self.tbw_gray)
        self.tab_CLAHE.setObjectName(u"tab_CLAHE")
        self.tbw_CLAHE = QWidget()
        self.tbw_CLAHE.setObjectName(u"tbw_CLAHE")
        self.horizontalLayout_5 = QHBoxLayout(self.tbw_CLAHE)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_CLAHE = QCheckBox(self.tbw_CLAHE)
        self.checkBox_CLAHE.setObjectName(u"checkBox_CLAHE")

        self.horizontalLayout_5.addWidget(self.checkBox_CLAHE)

        self.label = QLabel(self.tbw_CLAHE)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.CLAHE_clip = QDoubleSpinBox(self.tbw_CLAHE)
        self.CLAHE_clip.setObjectName(u"CLAHE_clip")
        self.CLAHE_clip.setValue(4.000000000000000)

        self.horizontalLayout_5.addWidget(self.CLAHE_clip)

        self.label_2 = QLabel(self.tbw_CLAHE)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.CLAHE_size = QSpinBox(self.tbw_CLAHE)
        self.CLAHE_size.setObjectName(u"CLAHE_size")
        self.CLAHE_size.setValue(12)

        self.horizontalLayout_5.addWidget(self.CLAHE_size)

        self.tab_CLAHE.addTab(self.tbw_CLAHE, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_CLAHE.addTab(self.tab_4, "")

        self.gridLayout_2.addWidget(self.tab_CLAHE, 0, 0, 1, 1)

        self.tab_transform.addTab(self.tbw_gray, "")
        self.tbw_size = QWidget()
        self.tbw_size.setObjectName(u"tbw_size")
        self.gridLayout_3 = QGridLayout(self.tbw_size)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tab_size = QTabWidget(self.tbw_size)
        self.tab_size.setObjectName(u"tab_size")
        self.tbw_cut = QWidget()
        self.tbw_cut.setObjectName(u"tbw_cut")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbw_cut.sizePolicy().hasHeightForWidth())
        self.tbw_cut.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.tbw_cut)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_cut = QCheckBox(self.tbw_cut)
        self.checkBox_cut.setObjectName(u"checkBox_cut")

        self.horizontalLayout_3.addWidget(self.checkBox_cut)

        self.checkBox_cut_origin = QCheckBox(self.tbw_cut)
        self.checkBox_cut_origin.setObjectName(u"checkBox_cut_origin")

        self.horizontalLayout_3.addWidget(self.checkBox_cut_origin)

        self.label_3 = QLabel(self.tbw_cut)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.cut_width = QSpinBox(self.tbw_cut)
        self.cut_width.setObjectName(u"cut_width")
        self.cut_width.setMaximum(10000)
        self.cut_width.setValue(128)

        self.horizontalLayout_3.addWidget(self.cut_width)

        self.label_4 = QLabel(self.tbw_cut)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.cut_height = QSpinBox(self.tbw_cut)
        self.cut_height.setObjectName(u"cut_height")
        self.cut_height.setMaximum(10000)
        self.cut_height.setValue(128)

        self.horizontalLayout_3.addWidget(self.cut_height)

        self.tab_size.addTab(self.tbw_cut, "")
        self.tbw_rotate = QWidget()
        self.tbw_rotate.setObjectName(u"tbw_rotate")
        self.horizontalLayout_6 = QHBoxLayout(self.tbw_rotate)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.rotate_angle = QLabel(self.tbw_rotate)
        self.rotate_angle.setObjectName(u"rotate_angle")

        self.horizontalLayout_6.addWidget(self.rotate_angle)

        self.slider_rotate = QSlider(self.tbw_rotate)
        self.slider_rotate.setObjectName(u"slider_rotate")
        self.slider_rotate.setMaximum(360)
        self.slider_rotate.setValue(180)
        self.slider_rotate.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.slider_rotate)

        self.tab_size.addTab(self.tbw_rotate, "")

        self.gridLayout_3.addWidget(self.tab_size, 0, 0, 1, 1)

        self.tab_transform.addTab(self.tbw_size, "")
        self.splitter.addWidget(self.tab_transform)
        self.view = ImageViewer(self.splitter)
        self.view.setObjectName(u"view")
        self.view.setMinimumSize(QSize(256, 256))
        self.splitter.addWidget(self.view)
        self.splitter_2.addWidget(self.splitter)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_transform.setCurrentIndex(1)
        self.tab_CLAHE.setCurrentIndex(0)
        self.tab_size.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5904\u7406\u5de5\u5177", None))
        self.btn_input.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u4ef6", None))
        self.lb_input_nums.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4e2a\u6570", None))
        self.btn_clearfiles.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6587\u4ef6", None))
        self.btn_output.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u6587\u4ef6\u5939", None))
        self.lb_output_path.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.btn_last_image.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20(A)", None))
#if QT_CONFIG(shortcut)
        self.btn_last_image.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.btn_origin.setText(QCoreApplication.translate("MainWindow", u"\u539f\u56fe", None))
        self.btn_next_image.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20(D)", None))
#if QT_CONFIG(shortcut)
        self.btn_next_image.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.checkBox_CLAHE.setText(QCoreApplication.translate("MainWindow", u"CLAHE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9650\u5236\u5bf9\u6bd4\u5ea6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u9002\u5e94\u5c3a\u5bf8", None))
        self.tab_CLAHE.setTabText(self.tab_CLAHE.indexOf(self.tbw_CLAHE), QCoreApplication.translate("MainWindow", u"CLAHE", None))
        self.tab_CLAHE.setTabText(self.tab_CLAHE.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tab_transform.setTabText(self.tab_transform.indexOf(self.tbw_gray), QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u53d8\u6362", None))
        self.checkBox_cut.setText(QCoreApplication.translate("MainWindow", u"\u88c1\u526a", None))
        self.checkBox_cut_origin.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u539f\u56fe", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5bbd", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9ad8", None))
        self.tab_size.setTabText(self.tab_size.indexOf(self.tbw_cut), QCoreApplication.translate("MainWindow", u"\u88c1\u526a", None))
        self.rotate_angle.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tab_size.setTabText(self.tab_size.indexOf(self.tbw_rotate), QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c", None))
        self.tab_transform.setTabText(self.tab_transform.indexOf(self.tbw_size), QCoreApplication.translate("MainWindow", u"\u5c3a\u5bf8\u53d8\u6362", None))
    # retranslateUi

