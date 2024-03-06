# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CLAHE.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.CLAHE_clipLimit = QDoubleSpinBox(self.frame)
        self.CLAHE_clipLimit.setObjectName(u"CLAHE_clipLimit")
        self.CLAHE_clipLimit.setValue(4.000000000000000)

        self.horizontalLayout.addWidget(self.CLAHE_clipLimit)


        self.verticalLayout.addWidget(self.frame)

        self.frame1 = QFrame(Dialog)
        self.frame1.setObjectName(u"frame1")
        self.horizontalLayout_2 = QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.CLAHE_tileGridSize_x = QSpinBox(self.frame1)
        self.CLAHE_tileGridSize_x.setObjectName(u"CLAHE_tileGridSize_x")
        self.CLAHE_tileGridSize_x.setValue(12)

        self.horizontalLayout_2.addWidget(self.CLAHE_tileGridSize_x)


        self.verticalLayout.addWidget(self.frame1)

        self.frame2 = QFrame(Dialog)
        self.frame2.setObjectName(u"frame2")
        self.horizontalLayout_3 = QHBoxLayout(self.frame2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.CLAHE_tileGridSize_y = QSpinBox(self.frame2)
        self.CLAHE_tileGridSize_y.setObjectName(u"CLAHE_tileGridSize_y")
        self.CLAHE_tileGridSize_y.setValue(12)

        self.horizontalLayout_3.addWidget(self.CLAHE_tileGridSize_y)


        self.verticalLayout.addWidget(self.frame2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"CLAHE\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"clipLimit ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"tileGridSize_x", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"tileGridSize_x", None))
    # retranslateUi

