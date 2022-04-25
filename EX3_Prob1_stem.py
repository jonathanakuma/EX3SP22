

import math
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from scipy import optimize as op


class RLC_Model():
    def __init__(self, pos=None, x=None, y=None, z=None):
        """
        x, y, and z have the expected meanings
        :param pos: a tuple (x,y,z)
        :param x: float
        :param y: float
        :param z: float
        """
        #set default values
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        #unpack position from a tuple if given
        if pos is not None:
            self.x, self.y, self.z = pos
        #override the x,y,z defaults if they are given as arguments
        self.x=x if x is not None else self.x
        self.y=y if y is not None else self.y
        self.z=z if z is not None else self.z

class RLC_Controller():
    def __init__(self, model=None, ax=None):
        self.model=RLC_Model() if model is None else model
        self.view=RLC_View()
        self.view.ax = ax
    # region Functions that operate on the model (i.e., change model state)
    def odeSystem(self, X, t, *args):
        """
        this is the odeSystem callback I'm using for odeint().  The *args contains a callback for the input voltage.
        :param X: the current values of the state variables
        :param t: the current time from odeint
        :param args: fn(t), L, R, C
        :return: list of derivatives of state variables
        """
        # read values from the GUI
        C = float(self.view.curr_input.text())
        R = float(self.view.res_input.text())
        L = float(self.view.ind_input.text())
        # unpack X into convenient variables
        fn, L, R, C = args
        # assign friendly variable names
        i1 = X[0]
        i2 = X[1]
        # calculate the current input voltage
        vt = fn(t)
        # calculate derivatives for the state variables
        i1dot = (vt - (i1 - i2) * R) / L
        # i1dot=(-vt+(i1-i2)*R)/L
        i2dot = i1dot - i2 / (R * C)
        return [i1dot, i2dot]



class RLC_View():
    def __init__(self):
        self.res_lb = qtw.QLabel()
        self.curr_lb = qtw.QLabel()
        self.ind_lb = qtw.QLabel()
        self.freq_lb = qtw.QLabel()
        self.phase_lb = qtw.QLabel()
        self.mag_lb = qtw.QLabel()
        self.curr_input = qtw.QLineEdit()
        self.res_input = qtw.QLineEdit()
        self.ind_input = qtw.QLineEdit()
        self.freq_input = qtw.QLineEdit()
        self.phase_input = qtw.QLineEdit()
        self.mag_input = qtw.QLineEdit()
