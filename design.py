# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 200))
        MainWindow.setMaximumSize(QSize(300, 200))
        font = QFont()
        font.setFamilies([u"Neucha"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 160, 281, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.start_button = QPushButton(self.horizontalLayoutWidget)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout.addWidget(self.start_button)

        self.stop_button = QPushButton(self.horizontalLayoutWidget)
        self.stop_button.setObjectName(u"stop_button")

        self.horizontalLayout.addWidget(self.stop_button)

        self.endsound_button = QPushButton(self.horizontalLayoutWidget)
        self.endsound_button.setObjectName(u"endsound_button")

        self.horizontalLayout.addWidget(self.endsound_button)

        self.sound_check = QCheckBox(self.horizontalLayoutWidget)
        self.sound_check.setObjectName(u"sound_check")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sound_check.sizePolicy().hasHeightForWidth())
        self.sound_check.setSizePolicy(sizePolicy1)
        self.sound_check.setFocusPolicy(Qt.NoFocus)
        self.sound_check.setLayoutDirection(Qt.RightToLeft)
        self.sound_check.setChecked(True)

        self.horizontalLayout.addWidget(self.sound_check)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 121, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(14)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.break_time = QSpinBox(self.gridLayoutWidget)
        self.break_time.setObjectName(u"break_time")
        self.break_time.setValue(5)

        self.gridLayout.addWidget(self.break_time, 1, 0, 1, 1)

        self.work_time = QSpinBox(self.gridLayoutWidget)
        self.work_time.setObjectName(u"work_time")
        self.work_time.setValue(25)

        self.gridLayout.addWidget(self.work_time, 0, 0, 1, 1)

        self.work_txt = QLabel(self.gridLayoutWidget)
        self.work_txt.setObjectName(u"work_txt")
        self.work_txt.setFont(font)

        self.gridLayout.addWidget(self.work_txt, 0, 1, 1, 1)

        self.break_txt = QLabel(self.gridLayoutWidget)
        self.break_txt.setObjectName(u"break_txt")

        self.gridLayout.addWidget(self.break_txt, 1, 1, 1, 1)

        self.cycles = QSpinBox(self.gridLayoutWidget)
        self.cycles.setObjectName(u"cycles")
        self.cycles.setValue(4)

        self.gridLayout.addWidget(self.cycles, 2, 0, 1, 1)

        self.cycle_txt = QLabel(self.gridLayoutWidget)
        self.cycle_txt.setObjectName(u"cycle_txt")

        self.gridLayout.addWidget(self.cycle_txt, 2, 1, 1, 1)

        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(140, 0, 151, 101))
        font1 = QFont()
        font1.setFamilies([u"Neucha"])
        font1.setPointSize(24)
        self.status_label.setFont(font1)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(140, 102, 151, 51))
        font2 = QFont()
        font2.setFamilies([u"AA Clobberin Time Smooth"])
        font2.setPointSize(14)
        self.lcdNumber.setFont(font2)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("value", 0.000000000000000)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PomodoroStreamTimer", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.endsound_button.setToolTip(QCoreApplication.translate("MainWindow", u"Select sound alarm", None))
#endif // QT_CONFIG(tooltip)
        self.endsound_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.sound_check.setToolTip(QCoreApplication.translate("MainWindow", u"Sound on/off", None))
#endif // QT_CONFIG(tooltip)
        self.sound_check.setText("")
        self.work_txt.setText(QCoreApplication.translate("MainWindow", u"work", None))
        self.break_txt.setText(QCoreApplication.translate("MainWindow", u"break", None))
        self.cycle_txt.setText(QCoreApplication.translate("MainWindow", u"cycles", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status", None))
    # retranslateUi

