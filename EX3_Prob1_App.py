from PyQt5.QtWidgets import QApplication, QWidget
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from EX3_Prob1_Gui import Ui_Form
from EX3_Prob1_stem import RLCCalc 
import sys


class main_window(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupImageLabel()
        self.show()
         #setting up some signals and slots
        self.cal_but.clicked.connect(self.calc)
        self.controller = RLC_Controller()
        self.show()

    def setupImageLabel(self):
        #region setup a label to display the image of the circuit
        self.pixMap = qtg.QPixmap()
        self.pixMap.load("Circuit1.png")
        self.image_label = qtw.QLabel()
        self.image_label.setPixmap(self.pixMap)
        self.layout_GridInput.addWidget(self.image_label)
    def setZoom(self):
        self.gv_Main.resetTransform()
        self.gv_Main.scale(self.spnd_Zoom.value(), self.spnd_Zoom.va    
        #endregion
    def calc(self):
        '''
        This is called when the calculate button is clicked
        :return: nothing
        '''
        self.RLC_Controller.odeSystem()
        #endregion

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())
