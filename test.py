#!/usr/bin/python3
from model import Model
#import pandas as pd

import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


model = Model()
#df = pd.read_csv("labels.csv", index_col="ClassId")
label_dict={'Arborio':0,'Basmati':1,'Ipsala':2,'Jasmine':3,'Karacadag':4}
k = list(label_dict.keys())

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        #self.setStyleSheet('''QLabel{ border: 4px dashed aaa }''')

    def setPixmap(self, image):
        super().setPixmap(image)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setAcceptDrops(True)
        
        self.l1 = QLabel()
        self.l1.setText("Label:")

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)
        mainLayout.addWidget(self.l1)

        self.setLayout(mainLayout)
        

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))
        x = model.predict(file_path)
        self.l1.setText("Label: "+k(x))


app = QApplication(sys.argv)
MainWindow = Window()
MainWindow.show()
sys.exit(app.exec_())
