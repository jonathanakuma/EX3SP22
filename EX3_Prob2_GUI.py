from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StructuralDesign(object):
    def setupUi(self, StructuralDesign):
        StructuralDesign.setObjectName("TrussStructuralDesign")
        StructuralDesign.resize(888, 591)
        self.verticalLayout = QtWidgets.QVBoxLayout(StructuralDesign)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grp_Load = QtWidgets.QGroupBox(StructuralDesign)
        self.grp_Load.setObjectName("grp_Load")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.grp_Load)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_Open = QtWidgets.QPushButton(self.grp_Load)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Open.sizePolicy().hasHeightForWidth())
        self.btn_Open.setSizePolicy(sizePolicy)
        self.btn_Open.setObjectName("btn_Open")
        self.horizontalLayout.addWidget(self.btn_Open, 0, QtCore.Qt.AlignTop)
        self.te_Path = QtWidgets.QTextEdit(self.grp_Load)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_Path.sizePolicy().hasHeightForWidth())
        self.te_Path.setSizePolicy(sizePolicy)
        self.te_Path.setMinimumSize(QtCore.QSize(700, 50))
        self.te_Path.setMaximumSize(QtCore.QSize(1000, 100))
        self.te_Path.setBaseSize(QtCore.QSize(500, 0))
        self.te_Path.setObjectName("te_Path")
        self.horizontalLayout.addWidget(self.te_Path)
        self.verticalLayout.addWidget(self.grp_Load)
        self.grp_DesignReport = QtWidgets.QGroupBox(StructuralDesign)
        self.grp_DesignReport.setObjectName("grp_DesignReport")
        self.te_DesignReport = QtWidgets.QTextEdit(self.grp_DesignReport)
        self.te_DesignReport.setGeometry(QtCore.QRect(10, 23, 851, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_DesignReport.sizePolicy().hasHeightForWidth())
        self.te_DesignReport.setSizePolicy(sizePolicy)
        self.te_DesignReport.setMinimumSize(QtCore.QSize(300, 300))
        self.te_DesignReport.setMaximumSize(QtCore.QSize(1000, 700))
        self.te_DesignReport.setObjectName("te_DesignReport")
        self.verticalLayout.addWidget(self.grp_DesignReport)
        self.gv_Main = QtWidgets.QGraphicsView(StructuralDesign)
        self.gv_Main.setObjectName("gv_Main")
        self.verticalLayout.addWidget(self.gv_Main)

        self.retranslateUi(StructuralDesign)
        QtCore.QMetaObject.connectSlotsByName(StructuralDesign)

    def retranslateUi(self, StructuralDesign):
        _translate = QtCore.QCoreApplication.translate
        StructuralDesign.setWindowTitle(_translate("StructuralDesign", "Form"))
        self.grp_Load.setTitle(_translate("StructuralDesign", "Circuit File and Load Set"))
        self.btn_Open.setText(_translate("StructuralDesign", "Open and Read a Circuit File"))
        self.grp_DesignReport.setTitle(_translate("StructuralDesign", "Design Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StructuralDesign = QtWidgets.QWidget()
    ui = Ui_StructuralDesign()
    ui.setupUi(StructuralDesign)
    StructuralDesign.show()
    sys.exit(app.exec_()
