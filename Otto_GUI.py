# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Otto_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1378, 1175)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.main_VerticalLayout = QtWidgets.QVBoxLayout(Form)
        self.main_VerticalLayout.setObjectName("main_VerticalLayout")
        self.gb_Input = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_Input.sizePolicy().hasHeightForWidth())
        self.gb_Input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_Input.setFont(font)
        self.gb_Input.setObjectName("gb_Input")
        self.gridLayout = QtWidgets.QGridLayout(self.gb_Input)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_Calculate = QtWidgets.QPushButton(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Calculate.sizePolicy().hasHeightForWidth())
        self.btn_Calculate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Calculate.setFont(font)
        self.btn_Calculate.setObjectName("btn_Calculate")
        self.gridLayout.addWidget(self.btn_Calculate, 0, 2, 3, 2)
        self.lbl_P0 = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_P0.sizePolicy().hasHeightForWidth())
        self.lbl_P0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_P0.setFont(font)
        self.lbl_P0.setObjectName("lbl_P0")
        self.gridLayout.addWidget(self.lbl_P0, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_TLow = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_TLow.sizePolicy().hasHeightForWidth())
        self.lbl_TLow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_TLow.setFont(font)
        self.lbl_TLow.setObjectName("lbl_TLow")
        self.gridLayout.addWidget(self.lbl_TLow, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.le_TLow = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_TLow.sizePolicy().hasHeightForWidth())
        self.le_TLow.setSizePolicy(sizePolicy)
        self.le_TLow.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_TLow.setFont(font)
        self.le_TLow.setClearButtonEnabled(True)
        self.le_TLow.setObjectName("le_TLow")
        self.gridLayout.addWidget(self.le_TLow, 1, 1, 1, 1)
        self.lbl_V0 = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_V0.sizePolicy().hasHeightForWidth())
        self.lbl_V0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_V0.setFont(font)
        self.lbl_V0.setObjectName("lbl_V0")
        self.gridLayout.addWidget(self.lbl_V0, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_THigh = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_THigh.sizePolicy().hasHeightForWidth())
        self.lbl_THigh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_THigh.setFont(font)
        self.lbl_THigh.setObjectName("lbl_THigh")
        self.gridLayout.addWidget(self.lbl_THigh, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 4, 1, 1)
        self.le_THigh = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_THigh.sizePolicy().hasHeightForWidth())
        self.le_THigh.setSizePolicy(sizePolicy)
        self.le_THigh.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_THigh.setFont(font)
        self.le_THigh.setClearButtonEnabled(True)
        self.le_THigh.setObjectName("le_THigh")
        self.gridLayout.addWidget(self.le_THigh, 0, 1, 1, 1)
        self.le_V0 = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_V0.sizePolicy().hasHeightForWidth())
        self.le_V0.setSizePolicy(sizePolicy)
        self.le_V0.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_V0.setFont(font)
        self.le_V0.setClearButtonEnabled(True)
        self.le_V0.setObjectName("le_V0")
        self.gridLayout.addWidget(self.le_V0, 3, 1, 1, 1)
        self.le_P0 = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_P0.sizePolicy().hasHeightForWidth())
        self.le_P0.setSizePolicy(sizePolicy)
        self.le_P0.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_P0.setFont(font)
        self.le_P0.setClearButtonEnabled(True)
        self.le_P0.setObjectName("le_P0")
        self.gridLayout.addWidget(self.le_P0, 2, 1, 1, 1)
        self.le_CR = QtWidgets.QLineEdit(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_CR.sizePolicy().hasHeightForWidth())
        self.le_CR.setSizePolicy(sizePolicy)
        self.le_CR.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_CR.setFont(font)
        self.le_CR.setClearButtonEnabled(True)
        self.le_CR.setObjectName("le_CR")
        self.gridLayout.addWidget(self.le_CR, 4, 1, 1, 1)
        self.lbl_CR = QtWidgets.QLabel(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_CR.sizePolicy().hasHeightForWidth())
        self.lbl_CR.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_CR.setFont(font)
        self.lbl_CR.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_CR.setObjectName("lbl_CR")
        self.gridLayout.addWidget(self.lbl_CR, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.rdo_English = QtWidgets.QRadioButton(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdo_English.sizePolicy().hasHeightForWidth())
        self.rdo_English.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdo_English.setFont(font)
        self.rdo_English.setChecked(True)
        self.rdo_English.setObjectName("rdo_English")
        self.gridLayout.addWidget(self.rdo_English, 3, 3, 1, 1)
        self.rdo_Metric = QtWidgets.QRadioButton(self.gb_Input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdo_Metric.sizePolicy().hasHeightForWidth())
        self.rdo_Metric.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdo_Metric.setFont(font)
        self.rdo_Metric.setChecked(False)
        self.rdo_Metric.setObjectName("rdo_Metric")
        self.gridLayout.addWidget(self.rdo_Metric, 3, 2, 1, 1)
        self.main_VerticalLayout.addWidget(self.gb_Input)
        self.gb_Output = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_Output.sizePolicy().hasHeightForWidth())
        self.gb_Output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_Output.setFont(font)
        self.gb_Output.setObjectName("gb_Output")
        self.grid_Output = QtWidgets.QGridLayout(self.gb_Output)
        self.grid_Output.setObjectName("grid_Output")
        self.label_7 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.grid_Output.addWidget(self.label_7, 4, 0, 1, 1)
        self.le_T3 = QtWidgets.QLineEdit(self.gb_Output)
        self.le_T3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_T3.sizePolicy().hasHeightForWidth())
        self.le_T3.setSizePolicy(sizePolicy)
        self.le_T3.setMinimumSize(QtCore.QSize(0, 0))
        self.le_T3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_T3.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_T3.setFont(font)
        self.le_T3.setObjectName("le_T3")
        self.grid_Output.addWidget(self.le_T3, 3, 1, 1, 1)
        self.le_T4 = QtWidgets.QLineEdit(self.gb_Output)
        self.le_T4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_T4.sizePolicy().hasHeightForWidth())
        self.le_T4.setSizePolicy(sizePolicy)
        self.le_T4.setMinimumSize(QtCore.QSize(0, 0))
        self.le_T4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_T4.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_T4.setFont(font)
        self.le_T4.setObjectName("le_T4")
        self.grid_Output.addWidget(self.le_T4, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.grid_Output.addWidget(self.label_11, 3, 3, 1, 1, QtCore.Qt.AlignRight)
        self.label_5 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.grid_Output.addWidget(self.label_5, 2, 0, 1, 1)
        self.le_T2 = QtWidgets.QLineEdit(self.gb_Output)
        self.le_T2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_T2.sizePolicy().hasHeightForWidth())
        self.le_T2.setSizePolicy(sizePolicy)
        self.le_T2.setMinimumSize(QtCore.QSize(0, 0))
        self.le_T2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_T2.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_T2.setFont(font)
        self.le_T2.setObjectName("le_T2")
        self.grid_Output.addWidget(self.le_T2, 2, 1, 1, 1)
        self.le_T1 = QtWidgets.QLineEdit(self.gb_Output)
        self.le_T1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_T1.sizePolicy().hasHeightForWidth())
        self.le_T1.setSizePolicy(sizePolicy)
        self.le_T1.setMinimumSize(QtCore.QSize(0, 0))
        self.le_T1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_T1.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_T1.setFont(font)
        self.le_T1.setObjectName("le_T1")
        self.grid_Output.addWidget(self.le_T1, 0, 1, 1, 1)
        self.le_PowerStroke = QtWidgets.QLineEdit(self.gb_Output)
        self.le_PowerStroke.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_PowerStroke.sizePolicy().hasHeightForWidth())
        self.le_PowerStroke.setSizePolicy(sizePolicy)
        self.le_PowerStroke.setMinimumSize(QtCore.QSize(0, 0))
        self.le_PowerStroke.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_PowerStroke.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_PowerStroke.setFont(font)
        self.le_PowerStroke.setObjectName("le_PowerStroke")
        self.grid_Output.addWidget(self.le_PowerStroke, 0, 4, 1, 1)
        self.le_HeatAdded = QtWidgets.QLineEdit(self.gb_Output)
        self.le_HeatAdded.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_HeatAdded.sizePolicy().hasHeightForWidth())
        self.le_HeatAdded.setSizePolicy(sizePolicy)
        self.le_HeatAdded.setMinimumSize(QtCore.QSize(0, 0))
        self.le_HeatAdded.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_HeatAdded.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_HeatAdded.setFont(font)
        self.le_HeatAdded.setObjectName("le_HeatAdded")
        self.grid_Output.addWidget(self.le_HeatAdded, 3, 4, 1, 1)
        self.lbl_T1Units = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_T1Units.sizePolicy().hasHeightForWidth())
        self.lbl_T1Units.setSizePolicy(sizePolicy)
        self.lbl_T1Units.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_T1Units.setFont(font)
        self.lbl_T1Units.setObjectName("lbl_T1Units")
        self.grid_Output.addWidget(self.lbl_T1Units, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.grid_Output.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.grid_Output.addWidget(self.label_14, 0, 3, 1, 1, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.grid_Output.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.grid_Output.addWidget(self.label_10, 4, 3, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_PowerStrokeUnits = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_PowerStrokeUnits.sizePolicy().hasHeightForWidth())
        self.lbl_PowerStrokeUnits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_PowerStrokeUnits.setFont(font)
        self.lbl_PowerStrokeUnits.setObjectName("lbl_PowerStrokeUnits")
        self.grid_Output.addWidget(self.lbl_PowerStrokeUnits, 0, 5, 1, 1)
        self.lbl_T4Units = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_T4Units.sizePolicy().hasHeightForWidth())
        self.lbl_T4Units.setSizePolicy(sizePolicy)
        self.lbl_T4Units.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_T4Units.setFont(font)
        self.lbl_T4Units.setObjectName("lbl_T4Units")
        self.grid_Output.addWidget(self.lbl_T4Units, 4, 2, 1, 1)
        self.lbl_T3Units = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_T3Units.sizePolicy().hasHeightForWidth())
        self.lbl_T3Units.setSizePolicy(sizePolicy)
        self.lbl_T3Units.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_T3Units.setFont(font)
        self.lbl_T3Units.setObjectName("lbl_T3Units")
        self.grid_Output.addWidget(self.lbl_T3Units, 3, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.grid_Output.addWidget(self.label_12, 4, 5, 1, 1)
        self.le_Efficiency = QtWidgets.QLineEdit(self.gb_Output)
        self.le_Efficiency.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_Efficiency.sizePolicy().hasHeightForWidth())
        self.le_Efficiency.setSizePolicy(sizePolicy)
        self.le_Efficiency.setMinimumSize(QtCore.QSize(0, 0))
        self.le_Efficiency.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_Efficiency.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_Efficiency.setFont(font)
        self.le_Efficiency.setObjectName("le_Efficiency")
        self.grid_Output.addWidget(self.le_Efficiency, 4, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_Output.addItem(spacerItem1, 3, 6, 1, 1)
        self.lbl_HeatInUnits = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_HeatInUnits.sizePolicy().hasHeightForWidth())
        self.lbl_HeatInUnits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_HeatInUnits.setFont(font)
        self.lbl_HeatInUnits.setObjectName("lbl_HeatInUnits")
        self.grid_Output.addWidget(self.lbl_HeatInUnits, 3, 5, 1, 1)
        self.lbl_CompressionStrokeUnits = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_CompressionStrokeUnits.sizePolicy().hasHeightForWidth())
        self.lbl_CompressionStrokeUnits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_CompressionStrokeUnits.setFont(font)
        self.lbl_CompressionStrokeUnits.setObjectName("lbl_CompressionStrokeUnits")
        self.grid_Output.addWidget(self.lbl_CompressionStrokeUnits, 2, 5, 1, 1)
        self.lbl_T2Units = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_T2Units.sizePolicy().hasHeightForWidth())
        self.lbl_T2Units.setSizePolicy(sizePolicy)
        self.lbl_T2Units.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_T2Units.setFont(font)
        self.lbl_T2Units.setObjectName("lbl_T2Units")
        self.grid_Output.addWidget(self.lbl_T2Units, 2, 2, 1, 1)
        self.le_CompressionStroke = QtWidgets.QLineEdit(self.gb_Output)
        self.le_CompressionStroke.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_CompressionStroke.sizePolicy().hasHeightForWidth())
        self.le_CompressionStroke.setSizePolicy(sizePolicy)
        self.le_CompressionStroke.setMinimumSize(QtCore.QSize(0, 0))
        self.le_CompressionStroke.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_CompressionStroke.setBaseSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_CompressionStroke.setFont(font)
        self.le_CompressionStroke.setObjectName("le_CompressionStroke")
        self.grid_Output.addWidget(self.le_CompressionStroke, 2, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gb_Output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.grid_Output.addWidget(self.label_15, 2, 3, 1, 1, QtCore.Qt.AlignRight)
        self.main_VerticalLayout.addWidget(self.gb_Output)
        self.gb_Plot = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_Plot.sizePolicy().hasHeightForWidth())
        self.gb_Plot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gb_Plot.setFont(font)
        self.gb_Plot.setObjectName("gb_Plot")
        self.grid_Plot = QtWidgets.QGridLayout(self.gb_Plot)
        self.grid_Plot.setObjectName("grid_Plot")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_Plot.addItem(spacerItem2, 0, 4, 1, 1)
        self.cmb_Ordinate = QtWidgets.QComboBox(self.gb_Plot)
        self.cmb_Ordinate.setMaximumSize(QtCore.QSize(50, 16777215))
        self.cmb_Ordinate.setObjectName("cmb_Ordinate")
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.addItem("")
        self.cmb_Ordinate.addItem("")
        self.grid_Plot.addWidget(self.cmb_Ordinate, 0, 3, 1, 1)
        self.lbl_Abcissa = QtWidgets.QLabel(self.gb_Plot)
        self.lbl_Abcissa.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lbl_Abcissa.setObjectName("lbl_Abcissa")
        self.grid_Plot.addWidget(self.lbl_Abcissa, 0, 0, 1, 1)
        self.lbl_Ordinate = QtWidgets.QLabel(self.gb_Plot)
        self.lbl_Ordinate.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lbl_Ordinate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Ordinate.setObjectName("lbl_Ordinate")
        self.grid_Plot.addWidget(self.lbl_Ordinate, 0, 2, 1, 1)
        self.chk_LogAbcissa = QtWidgets.QCheckBox(self.gb_Plot)
        self.chk_LogAbcissa.setObjectName("chk_LogAbcissa")
        self.grid_Plot.addWidget(self.chk_LogAbcissa, 1, 0, 1, 2)
        self.chk_LogOrdinate = QtWidgets.QCheckBox(self.gb_Plot)
        self.chk_LogOrdinate.setObjectName("chk_LogOrdinate")
        self.grid_Plot.addWidget(self.chk_LogOrdinate, 1, 2, 1, 2)
        self.cmb_Abcissa = QtWidgets.QComboBox(self.gb_Plot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_Abcissa.sizePolicy().hasHeightForWidth())
        self.cmb_Abcissa.setSizePolicy(sizePolicy)
        self.cmb_Abcissa.setMaximumSize(QtCore.QSize(50, 16777215))
        self.cmb_Abcissa.setObjectName("cmb_Abcissa")
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.addItem("")
        self.cmb_Abcissa.addItem("")
        self.grid_Plot.addWidget(self.cmb_Abcissa, 0, 1, 1, 1)
        self.main_VerticalLayout.addWidget(self.gb_Plot)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.main_VerticalLayout.addItem(spacerItem3)

        self.retranslateUi(Form)
        self.cmb_Ordinate.setCurrentIndex(0)
        self.cmb_Abcissa.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gb_Input.setTitle(_translate("Form", "Input for Air Standard Otto Cycle"))
        self.btn_Calculate.setText(_translate("Form", "Calculate"))
        self.lbl_P0.setText(_translate("Form", "P0 (atm)"))
        self.lbl_TLow.setText(_translate("Form", "T Low (R)"))
        self.le_TLow.setText(_translate("Form", "500.0"))
        self.le_TLow.setPlaceholderText(_translate("Form", "enter a value for the high pressure isobar"))
        self.lbl_V0.setText(_translate("Form", "Cylinder V (ft^3)"))
        self.lbl_THigh.setText(_translate("Form", "T High (R)"))
        self.le_THigh.setText(_translate("Form", "3600.0"))
        self.le_THigh.setPlaceholderText(_translate("Form", "enter a value for the high pressure isobar"))
        self.le_V0.setText(_translate("Form", "0.02"))
        self.le_P0.setText(_translate("Form", "1.0"))
        self.le_P0.setPlaceholderText(_translate("Form", "enter a value for the low pressure isobar"))
        self.le_CR.setText(_translate("Form", "8.0"))
        self.le_CR.setPlaceholderText(_translate("Form", "turbine isentropic efficiency 0.0<eta<=1.0"))
        self.lbl_CR.setText(_translate("Form", "Compression Ratio"))
        self.rdo_English.setText(_translate("Form", "English"))
        self.rdo_Metric.setText(_translate("Form", "Metric"))
        self.gb_Output.setTitle(_translate("Form", "Output"))
        self.label_7.setText(_translate("Form", "T4"))
        self.label_11.setText(_translate("Form", "Heat Added"))
        self.label_5.setText(_translate("Form", "T2"))
        self.lbl_T1Units.setText(_translate("Form", "C"))
        self.label_9.setText(_translate("Form", "T3"))
        self.label_14.setText(_translate("Form", "Power Stroke"))
        self.label_2.setText(_translate("Form", "T1"))
        self.label_10.setText(_translate("Form", "Cycle Efficiency"))
        self.lbl_PowerStrokeUnits.setText(_translate("Form", "kJ/kg"))
        self.lbl_T4Units.setText(_translate("Form", "C"))
        self.lbl_T3Units.setText(_translate("Form", "C"))
        self.label_12.setText(_translate("Form", "%"))
        self.lbl_HeatInUnits.setText(_translate("Form", "kJ/kg"))
        self.lbl_CompressionStrokeUnits.setText(_translate("Form", "kJ/kg"))
        self.lbl_T2Units.setText(_translate("Form", "C"))
        self.label_15.setText(_translate("Form", "Compression Stroke"))
        self.gb_Plot.setTitle(_translate("Form", "Plot"))
        self.cmb_Ordinate.setItemText(0, _translate("Form", "P"))
        self.cmb_Ordinate.setItemText(1, _translate("Form", "T"))
        self.cmb_Ordinate.setItemText(2, _translate("Form", "u"))
        self.cmb_Ordinate.setItemText(3, _translate("Form", "h"))
        self.cmb_Ordinate.setItemText(4, _translate("Form", "s"))
        self.cmb_Ordinate.setItemText(5, _translate("Form", "v"))
        self.lbl_Abcissa.setText(_translate("Form", "Abcissa (x)"))
        self.lbl_Ordinate.setText(_translate("Form", "Ordinate (y)"))
        self.chk_LogAbcissa.setText(_translate("Form", "Logarithmic (x)"))
        self.chk_LogOrdinate.setText(_translate("Form", "Logarithmic (y)"))
        self.cmb_Abcissa.setCurrentText(_translate("Form", "v"))
        self.cmb_Abcissa.setItemText(0, _translate("Form", "P"))
        self.cmb_Abcissa.setItemText(1, _translate("Form", "T"))
        self.cmb_Abcissa.setItemText(2, _translate("Form", "u"))
        self.cmb_Abcissa.setItemText(3, _translate("Form", "h"))
        self.cmb_Abcissa.setItemText(4, _translate("Form", "s"))
        self.cmb_Abcissa.setItemText(5, _translate("Form", "v"))
