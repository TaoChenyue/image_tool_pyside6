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
    QListWidgetItem, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QSplitter, QVBoxLayout, QWidget)

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

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 406, 1800))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(200, 1800))
        self.scrollAreaWidgetContents.setStyleSheet(u".QFrame{\n"
"	border: 1px solid black;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 3, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)

        self.CLAHE_clip = QDoubleSpinBox(self.frame_3)
        self.CLAHE_clip.setObjectName(u"CLAHE_clip")
        self.CLAHE_clip.setValue(4.000000000000000)

        self.gridLayout_4.addWidget(self.CLAHE_clip, 1, 1, 1, 1)

        self.CLAHE_size = QSpinBox(self.frame_3)
        self.CLAHE_size.setObjectName(u"CLAHE_size")
        self.CLAHE_size.setValue(12)

        self.gridLayout_4.addWidget(self.CLAHE_size, 1, 3, 1, 1)

        self.checkBox_CLAHE = QCheckBox(self.frame_3)
        self.checkBox_CLAHE.setObjectName(u"checkBox_CLAHE")

        self.gridLayout_4.addWidget(self.checkBox_CLAHE, 0, 0, 2, 1)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.checkBox_HE = QCheckBox(self.frame_6)
        self.checkBox_HE.setObjectName(u"checkBox_HE")

        self.gridLayout_7.addWidget(self.checkBox_HE, 0, 0, 1, 1)

        self.checkBox_AutoGamma = QCheckBox(self.frame_6)
        self.checkBox_AutoGamma.setObjectName(u"checkBox_AutoGamma")

        self.gridLayout_7.addWidget(self.checkBox_AutoGamma, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_LOG = QCheckBox(self.frame_7)
        self.checkBox_LOG.setObjectName(u"checkBox_LOG")

        self.gridLayout_2.addWidget(self.checkBox_LOG, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)

        self.LOG_v = QDoubleSpinBox(self.frame_7)
        self.LOG_v.setObjectName(u"LOG_v")
        self.LOG_v.setDecimals(3)
        self.LOG_v.setMinimum(0.001000000000000)
        self.LOG_v.setMaximum(999.990000000000009)
        self.LOG_v.setSingleStep(0.100000000000000)
        self.LOG_v.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.LOG_v, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_GAMMA = QCheckBox(self.frame_8)
        self.checkBox_GAMMA.setObjectName(u"checkBox_GAMMA")

        self.gridLayout_3.addWidget(self.checkBox_GAMMA, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)

        self.GAMMA_c = QDoubleSpinBox(self.frame_8)
        self.GAMMA_c.setObjectName(u"GAMMA_c")
        self.GAMMA_c.setDecimals(3)
        self.GAMMA_c.setMinimum(0.001000000000000)
        self.GAMMA_c.setMaximum(999.000000000000000)
        self.GAMMA_c.setSingleStep(0.100000000000000)
        self.GAMMA_c.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.GAMMA_c, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_MeanStd = QCheckBox(self.frame_9)
        self.checkBox_MeanStd.setObjectName(u"checkBox_MeanStd")

        self.horizontalLayout_3.addWidget(self.checkBox_MeanStd)

        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.MeanStd_mean = QDoubleSpinBox(self.frame_9)
        self.MeanStd_mean.setObjectName(u"MeanStd_mean")
        self.MeanStd_mean.setMaximum(255.000000000000000)
        self.MeanStd_mean.setValue(127.000000000000000)

        self.horizontalLayout_3.addWidget(self.MeanStd_mean)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.MeanStd_std = QDoubleSpinBox(self.frame_9)
        self.MeanStd_std.setObjectName(u"MeanStd_std")
        self.MeanStd_std.setMaximum(255.000000000000000)
        self.MeanStd_std.setValue(32.000000000000000)

        self.horizontalLayout_3.addWidget(self.MeanStd_std)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.cut_height = QSpinBox(self.frame_4)
        self.cut_height.setObjectName(u"cut_height")
        self.cut_height.setMaximum(10000)
        self.cut_height.setValue(128)

        self.gridLayout_5.addWidget(self.cut_height, 1, 2, 1, 1)

        self.checkBox_cut = QCheckBox(self.frame_4)
        self.checkBox_cut.setObjectName(u"checkBox_cut")

        self.gridLayout_5.addWidget(self.checkBox_cut, 0, 0, 1, 1)

        self.checkBox_cut_origin = QCheckBox(self.frame_4)
        self.checkBox_cut_origin.setObjectName(u"checkBox_cut_origin")

        self.gridLayout_5.addWidget(self.checkBox_cut_origin, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 1, 1, 1)

        self.cut_width = QSpinBox(self.frame_4)
        self.cut_width.setObjectName(u"cut_width")
        self.cut_width.setMaximum(10000)
        self.cut_width.setValue(128)

        self.gridLayout_5.addWidget(self.cut_width, 0, 2, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 1, 1, 1, 1)

        self.cut_whole = QPushButton(self.frame_4)
        self.cut_whole.setObjectName(u"cut_whole")

        self.gridLayout_5.addWidget(self.cut_whole, 2, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.slider_rotate = QSlider(self.frame_5)
        self.slider_rotate.setObjectName(u"slider_rotate")
        self.slider_rotate.setMaximum(360)
        self.slider_rotate.setValue(180)
        self.slider_rotate.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.slider_rotate, 3, 0, 1, 2)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)

        self.rotate_angle = QLabel(self.frame_5)
        self.rotate_angle.setObjectName(u"rotate_angle")

        self.gridLayout_6.addWidget(self.rotate_angle, 1, 1, 1, 1)

        self.btn_rotate_left = QPushButton(self.frame_5)
        self.btn_rotate_left.setObjectName(u"btn_rotate_left")

        self.gridLayout_6.addWidget(self.btn_rotate_left, 4, 0, 1, 1)

        self.btn_rotate_right = QPushButton(self.frame_5)
        self.btn_rotate_right.setObjectName(u"btn_rotate_right")

        self.gridLayout_6.addWidget(self.btn_rotate_right, 4, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.splitter_2.addWidget(self.frame)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.view = ImageViewer(self.splitter)
        self.view.setObjectName(u"view")
        self.view.setMinimumSize(QSize(0, 0))
        self.splitter.addWidget(self.view)
        self.lst_files = QListWidget(self.splitter)
        self.lst_files.setObjectName(u"lst_files")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lst_files.sizePolicy().hasHeightForWidth())
        self.lst_files.setSizePolicy(sizePolicy)
        self.lst_files.setMinimumSize(QSize(0, 0))
        self.lst_files.setMaximumSize(QSize(16777215, 200))
        self.splitter.addWidget(self.lst_files)
        self.splitter_2.addWidget(self.splitter)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u9002\u5e94\u5c3a\u5bf8", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9650\u5236\u5bf9\u6bd4\u5ea6", None))
        self.checkBox_CLAHE.setText(QCoreApplication.translate("MainWindow", u"CLAHE", None))
        self.checkBox_HE.setText(QCoreApplication.translate("MainWindow", u"HE", None))
        self.checkBox_AutoGamma.setText(QCoreApplication.translate("MainWindow", u"AutoGamma", None))
        self.checkBox_LOG.setText(QCoreApplication.translate("MainWindow", u"LOG", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.checkBox_GAMMA.setText(QCoreApplication.translate("MainWindow", u"GAMMA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.checkBox_MeanStd.setText(QCoreApplication.translate("MainWindow", u"MeanStd", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u503c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u5dee", None))
        self.checkBox_cut.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\u88c1\u526a", None))
        self.checkBox_cut_origin.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u539f\u56fe", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5bbd", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9ad8", None))
        self.cut_whole.setText(QCoreApplication.translate("MainWindow", u"\u88c1\u526a\u6574\u56fe(S)", None))
#if QT_CONFIG(shortcut)
        self.cut_whole.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c\u89d2\u5ea6", None))
        self.rotate_angle.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_rotate_left.setText(QCoreApplication.translate("MainWindow", u"\u987a\u65f6\u9488(\u2190)", None))
#if QT_CONFIG(shortcut)
        self.btn_rotate_left.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.btn_rotate_right.setText(QCoreApplication.translate("MainWindow", u"\u9006\u65f6\u9488(\u2192)", None))
#if QT_CONFIG(shortcut)
        self.btn_rotate_right.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

