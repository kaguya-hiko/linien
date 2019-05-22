# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalWidget = CentralPanel(self.centralwidget)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.go_left = QtWidgets.QPushButton(self.horizontalWidget)
        self.go_left.setObjectName("go_left")
        self.horizontalLayout_8.addWidget(self.go_left)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scan_amplitude = QtWidgets.QLabel(self.horizontalWidget)
        self.scan_amplitude.setObjectName("scan_amplitude")
        self.horizontalLayout_3.addWidget(self.scan_amplitude)
        self.increase_scan_amplitude = QtWidgets.QPushButton(self.horizontalWidget)
        self.increase_scan_amplitude.setObjectName("increase_scan_amplitude")
        self.horizontalLayout_3.addWidget(self.increase_scan_amplitude)
        self.decrease_scan_amplitude = QtWidgets.QPushButton(self.horizontalWidget)
        self.decrease_scan_amplitude.setObjectName("decrease_scan_amplitude")
        self.horizontalLayout_3.addWidget(self.decrease_scan_amplitude)
        self.reset_scan_amplitude = QtWidgets.QPushButton(self.horizontalWidget)
        self.reset_scan_amplitude.setObjectName("reset_scan_amplitude")
        self.horizontalLayout_3.addWidget(self.reset_scan_amplitude)
        self.verticalLayout_17.addLayout(self.horizontalLayout_3)
        self.graphicsView = PlotWidget(self.horizontalWidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(100, 100))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_17.addWidget(self.graphicsView)
        self.horizontalLayout_8.addLayout(self.verticalLayout_17)
        self.go_right = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_right.sizePolicy().hasHeightForWidth())
        self.go_right.setSizePolicy(sizePolicy)
        self.go_right.setObjectName("go_right")
        self.horizontalLayout_8.addWidget(self.go_right)
        self.horizontalLayout.addWidget(self.horizontalWidget)
        self.rightPanel = RightPanel(self.centralwidget)
        self.rightPanel.setMinimumSize(QtCore.QSize(250, 0))
        self.rightPanel.setObjectName("rightPanel")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.rightPanel)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.openDeviceManagerButton = QtWidgets.QPushButton(self.rightPanel)
        self.openDeviceManagerButton.setObjectName("openDeviceManagerButton")
        self.verticalLayout_11.addWidget(self.openDeviceManagerButton)
        self.closeButton = QtWidgets.QPushButton(self.rightPanel)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_11.addWidget(self.closeButton)
        self.shutdownButton = QtWidgets.QPushButton(self.rightPanel)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 25, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(102, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(204, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.shutdownButton.setPalette(palette)
        self.shutdownButton.setAutoFillBackground(False)
        self.shutdownButton.setObjectName("shutdownButton")
        self.verticalLayout_11.addWidget(self.shutdownButton)
        self.toolBox = QtWidgets.QToolBox(self.rightPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(250, 0))
        self.toolBox.setObjectName("toolBox")
        self.page = SpectroscopyPanel()
        self.page.setGeometry(QtCore.QRect(0, 0, 250, 303))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 220, 500))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.modulation_frequency = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.modulation_frequency.setObjectName("modulation_frequency")
        self.horizontalLayout_6.addWidget(self.modulation_frequency)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.modulation_amplitude = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.modulation_amplitude.setObjectName("modulation_amplitude")
        self.horizontalLayout_2.addWidget(self.modulation_amplitude)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ramp_speed = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.ramp_speed.setObjectName("ramp_speed")
        self.horizontalLayout_5.addWidget(self.ramp_speed)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.demodulation_phase = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.demodulation_phase.setObjectName("demodulation_phase")
        self.horizontalLayout_4.addWidget(self.demodulation_phase)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.groupBox_7 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.demodulation_frequency = QtWidgets.QComboBox(self.groupBox_7)
        self.demodulation_frequency.setObjectName("demodulation_frequency")
        self.demodulation_frequency.addItem("")
        self.demodulation_frequency.addItem("")
        self.demodulation_frequency.addItem("")
        self.verticalLayout_13.addWidget(self.demodulation_frequency)
        self.verticalLayout_9.addWidget(self.groupBox_7)
        self.groupBox_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.signal_offset = QtWidgets.QSpinBox(self.groupBox_6)
        self.signal_offset.setObjectName("signal_offset")
        self.horizontalLayout_7.addWidget(self.signal_offset)
        self.verticalLayout_9.addWidget(self.groupBox_6)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.toolBox.addItem(self.page, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 250, 303))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_14.addWidget(self.label_7)
        self.toolBox.addItem(self.page_3, "")
        self.page_2 = LockingPanel()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 250, 303))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 220, 504))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.kp = QtWidgets.QSpinBox(self.groupBox_5)
        self.kp.setMinimum(-8192)
        self.kp.setMaximum(8191)
        self.kp.setObjectName("kp")
        self.verticalLayout_6.addWidget(self.kp)
        self.ki = QtWidgets.QSpinBox(self.groupBox_5)
        self.ki.setMinimum(-8192)
        self.ki.setMaximum(8191)
        self.ki.setObjectName("ki")
        self.verticalLayout_6.addWidget(self.ki)
        self.kd = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kd.sizePolicy().hasHeightForWidth())
        self.kd.setSizePolicy(sizePolicy)
        self.kd.setMinimum(-8192)
        self.kd.setMaximum(8191)
        self.kd.setObjectName("kd")
        self.verticalLayout_6.addWidget(self.kd)
        self.verticalLayout_8.addWidget(self.groupBox_5)
        self.lock_control_container = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.lock_control_container.setObjectName("lock_control_container")
        self.auto_mode = QtWidgets.QWidget()
        self.auto_mode.setObjectName("auto_mode")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.auto_mode)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.auto_mode)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.checkBox = QtWidgets.QCheckBox(self.auto_mode)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_10.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.auto_mode)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_10.addWidget(self.checkBox_2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.auto_mode)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_10.addWidget(self.checkBox_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.auto_mode)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_10.addWidget(self.checkBox_3)
        self.lock_control_container.addTab(self.auto_mode, "")
        self.manual_mode = QtWidgets.QWidget()
        self.manual_mode.setObjectName("manual_mode")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.manual_mode)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.manual_mode)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_12.addWidget(self.label_6)
        self.radioButton = QtWidgets.QRadioButton(self.manual_mode)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_12.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.manual_mode)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_12.addWidget(self.radioButton_2)
        self.manualLockButton = QtWidgets.QPushButton(self.manual_mode)
        self.manualLockButton.setObjectName("manualLockButton")
        self.verticalLayout_12.addWidget(self.manualLockButton)
        self.lock_control_container.addTab(self.manual_mode, "")
        self.verticalLayout_8.addWidget(self.lock_control_container)
        self.lock_status_container = LockStatusPanel(self.scrollAreaWidgetContents)
        self.lock_status_container.setObjectName("lock_status_container")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.lock_status_container)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.lock_status = QtWidgets.QLabel(self.lock_status_container)
        self.lock_status.setObjectName("lock_status")
        self.verticalLayout_18.addWidget(self.lock_status)
        self.stop_lock = QtWidgets.QPushButton(self.lock_status_container)
        self.stop_lock.setObjectName("stop_lock")
        self.verticalLayout_18.addWidget(self.stop_lock)
        self.verticalLayout_8.addWidget(self.lock_status_container)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_11.addWidget(self.toolBox)
        self.horizontalLayout.addWidget(self.rightPanel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.lock_control_container.setCurrentIndex(0)
        self.closeButton.clicked.connect(self.rightPanel.close_app)
        self.shutdownButton.clicked.connect(self.rightPanel.shutdown_server)
        self.openDeviceManagerButton.clicked.connect(self.rightPanel.open_device_manager)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.go_left.setText(_translate("MainWindow", "<"))
        self.scan_amplitude.setText(_translate("MainWindow", "100 %"))
        self.increase_scan_amplitude.setText(_translate("MainWindow", "+"))
        self.decrease_scan_amplitude.setText(_translate("MainWindow", "-"))
        self.reset_scan_amplitude.setText(_translate("MainWindow", "reset"))
        self.go_right.setText(_translate("MainWindow", ">"))
        self.openDeviceManagerButton.setText(_translate("MainWindow", "Device manager"))
        self.closeButton.setText(_translate("MainWindow", "Close client"))
        self.shutdownButton.setText(_translate("MainWindow", "Shutdown server"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Modulation frequency"))
        self.label_5.setText(_translate("MainWindow", "MHz"))
        self.groupBox.setTitle(_translate("MainWindow", "Modulation amplitude"))
        self.label.setText(_translate("MainWindow", "Vpp"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Ramp speed"))
        self.label_4.setText(_translate("MainWindow", "Hz"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Demodulation phase"))
        self.label_3.setText(_translate("MainWindow", "deg"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Demodulation frequency"))
        self.demodulation_frequency.setItemText(0, _translate("MainWindow", "1f"))
        self.demodulation_frequency.setItemText(1, _translate("MainWindow", "3f"))
        self.demodulation_frequency.setItemText(2, _translate("MainWindow", "5f"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Signal offset"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Spectroscopy"))
        self.label_7.setText(_translate("MainWindow", "still missing..."))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Signal filtering"))
        self.groupBox_5.setTitle(_translate("MainWindow", "P,I and D"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">For automatic lock, click and drag over a line.</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Automatic relock"))
        self.checkBox_2.setText(_translate("MainWindow", "Determine signal offset"))
        self.checkBox_4.setText(_translate("MainWindow", "Emit TTL when locked"))
        self.checkBox_3.setText(_translate("MainWindow", "Relock on TTL"))
        self.lock_control_container.setTabText(self.lock_control_container.indexOf(self.auto_mode), _translate("MainWindow", "Auto"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Center the line and zoom in before pressing the button.</span></p></body></html>"))
        self.radioButton.setText(_translate("MainWindow", "Rising slope"))
        self.radioButton_2.setText(_translate("MainWindow", "Falling slope"))
        self.manualLockButton.setText(_translate("MainWindow", "Lock!"))
        self.lock_control_container.setTabText(self.lock_control_container.indexOf(self.manual_mode), _translate("MainWindow", "Manual"))
        self.lock_status.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Lock status</span></p></body></html>"))
        self.stop_lock.setText(_translate("MainWindow", "Stop lock"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Locking"))


from central_panel import CentralPanel
from lock_status_panel import LockStatusPanel
from locking_panel import LockingPanel
from plot_widget import PlotWidget
from right_panel import RightPanel
from spectroscopy_panel import SpectroscopyPanel


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
