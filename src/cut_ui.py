# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cut.ui'
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
    QFrame, QHBoxLayout, QLabel, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(212, 143)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.cut_height = QSpinBox(self.frame)
        self.cut_height.setObjectName(u"cut_height")
        self.cut_height.setMaximum(10000)
        self.cut_height.setValue(128)

        self.horizontalLayout.addWidget(self.cut_height)


        self.verticalLayout.addWidget(self.frame)

        self.frame1 = QFrame(Dialog)
        self.frame1.setObjectName(u"frame1")
        self.horizontalLayout_2 = QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cut_width = QSpinBox(self.frame1)
        self.cut_width.setObjectName(u"cut_width")
        self.cut_width.setMaximum(10000)
        self.cut_width.setValue(128)

        self.horizontalLayout_2.addWidget(self.cut_width)


        self.verticalLayout.addWidget(self.frame1)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u88c1\u526a\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u9ad8", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5bbd", None))
    # retranslateUi

