# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:31:49 2023

@author: osjac
"""
import numpy as np

import matplotlib.pyplot as plt

from PyQt5 import QtWidgets, uic,QtCore
import sys

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure








class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('vogel.ui', self)

               
        
        self.layout = self.findChild(QtWidgets.QVBoxLayout, "thisOne")
        
        
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        
        self.layout.addWidget(self.canvas)
        
        self.button = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.button.clicked.connect(self.reset)
        
        self.aValue = self.findChild(QtWidgets.QDoubleSpinBox, "doubleSpinBox_1")
        self.bValue = self.findChild(QtWidgets.QDoubleSpinBox, "doubleSpinBox_2")
        self.cValue = self.findChild(QtWidgets.QSpinBox, "spinBox_3")
        
        self.aValue.valueChanged.connect(self.updateSlider)
        self.bValue.valueChanged.connect(self.updateSlider)
        
        self.aSlider = self.findChild(QtWidgets.QSlider, "horizontalSlider_1")
        self.bSlider = self.findChild(QtWidgets.QSlider, "horizontalSlider_2")
        self.cSlider = self.findChild(QtWidgets.QSlider, "horizontalSlider_3")
        
        self.aSlider.valueChanged.connect(self.updateSpin)
        self.bSlider.valueChanged.connect(self.updateSpin)
        
        self.cValue.valueChanged.connect(self.plotter)
        self.cSlider.valueChanged.connect(self.plotter)
        
        
        #set mins and max:
        self.aValue.setMinimum(0)
        self.aValue.setMaximum(10)
        self.bValue.setMinimum(0)
        self.bValue.setMaximum(180)
        self.cValue.setMinimum(1)
        self.cValue.setMaximum(1000)
        self.aSlider.setMinimum(0*10000)
        self.aSlider.setMaximum(10*10000)
        self.bSlider.setMinimum(0*10000)
        self.bSlider.setMaximum(180*10000)
        self.cSlider.setMinimum(1)
        self.cSlider.setMaximum(1000)
        
        
        
        self.show()
        
        

    def reset(self):
        self.aValue.setValue(float(1))
        self.bValue.setValue(float(137.50800))
        self.cValue.setValue(int(100))
        


    def updateSpin(self):
        self.aValue.setValue(float(self.aSlider.value()/10000))
        self.bValue.setValue(float(self.bSlider.value()/10000))
        #print("updatedSpin") 
        self.plotter()
    
    def updateSlider(self):
        self.aSlider.setValue(int(self.aValue.value()*10000))
        self.bSlider.setValue(int(self.bValue.value()*10000))
        #print("updatedSlider")
        self.plotter()

    def plotter(self):
        a = self.aValue.value()
        alpha = self.bValue.value()
        N = self.cValue.value()
        
        self.fig.clear()
        
        Alpha = alpha#*(np.pi/180)#137.508*(np.pi/180)
        #a = 1
        #N = 1000

        r = []
        theta = [] 


        for n in range(0,N):
            r.append(a*np.sqrt(n))
            theta.append(n*Alpha)


        
        ax = self.fig.add_subplot(projection='polar')
        ax.scatter(np.array(theta)*(np.pi/180), np.array(r))
        

        
        self.canvas.draw()
        
        
        


    



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec())
    #app.exec()
    #del window, app