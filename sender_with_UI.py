# Python 3
# gedit 8

import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import numpy 
import csv
import socket

class App(QWidget):

	def sender(self):          # START btn
		#result=list(csv.reader(open("/home/pabitra/QT5/c2/ut.csv","r"),delimiter=","))
		print(ipAdr)
		print(port)
		print(result)
		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		for i in range(len(result)):
			sw= str(result[i][0]+" "+result[i][1] )
			s.sendto(sw.encode(),(ipAdr,port))

		s.close()
		
	def open_files(self):   # browser Button
		dialog = QFileDialog()
		fname = dialog.getOpenFileName(self, "Open file")
		self.myTextBox.setText(fname[0])
		filename=fname[0]
		reader = csv.reader(open(filename, "r"), delimiter=",")
		global result
		result =list(reader)
		
	def ipEditer(self,text1):        # ip edit 
		#print(text1)
		global ipAdr
		if text1 !="":
			ipAdr=text1
		else :
			ipAdr="127.0.0.1"
		
	def portEditer(self,text2):     # port edit
		#print(text2)
		global port
		if text2 != "":
			port=int(text2)
		else :
			import random
			port=random.randint(1,1000)
		
	def __init__(self):
		super().__init__()
		
		# declare the Universal variables ### these names should not be repeated
		# result :- it's the list read from i/p file 
		# ip-
		# port :- 
		self.initUI()

	def initUI(self):
		
		# Basic tile,icon,geometry,statusBar
		self.setWindowTitle("Sender ")
		self.setWindowIcon(QIcon("download.png"))
		self.setGeometry(100,100,320,180)
		self.statusBar=QStatusBar()    # change in every condition
		self.statusBar.showMessage("ready")
		
		# create widgets
		
		browserButton=QPushButton("browse files ",self)
		browserButton.resize(browserButton.sizeHint())
		browserButton.setToolTip("Press to select the file you want ")
		browserButton.clicked.connect(self.open_files)
		
		#print(self.result)
		
		startButton= QPushButton("START",self)
		startButton.resize(startButton.sizeHint())
		startButton.setToolTip("Press to  run the Sender")
		startButton.clicked.connect(self.sender)
		
		self.myTextBox=QTextEdit(self)
		# resize feature
		
		
		self.bill_1=QLabel("<b> ip Address <\b>")
		self.bill_1.adjustSize()
		
		self.bil_2=QLabel("<b>Port<\b>")
		self.bil_2.adjustSize()
		
		ipEdit=QLineEdit(self)
		try:
			ipEdit.textChanged[str].connect(self.ipEditer)
		except:
			pass
		
		portEdit=QLineEdit(self)
		try:
			portEdit.textChanged[str].connect(self.portEditer)
		except:
			ValueError
		
		self.bil_3=QLabel("<b>Message Box<\b>")	
		self.myMessageBox=QTextEdit(self)
		
		
		grid=QGridLayout()
		grid.setSpacing(10)
		grid.addWidget(browserButton,1,0)
		grid.addWidget(startButton,1,1)
		grid.addWidget(self.myTextBox,2,0)
		grid.addWidget(self.bill_1,3,0)
		grid.addWidget(self.bil_2,3,1)
		grid.addWidget(ipEdit,4,0)
		grid.addWidget(portEdit,4,1)
		grid.addWidget(self.bil_3,5,0)
		grid.addWidget(self.myMessageBox,6,0)
		self.setLayout(grid)
		
		
		self.show()
	
	def closeEvent(self,event):
		reply=QMessageBox.question(self,"Message","Quit ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
		
		if reply==QMessageBox.Yes:
			event.accept()
		if reply==QMessageBox.No :
			event.ignore()
					
	
if __name__ == '__main__':
	app=QApplication(sys.argv)
	r=App()
	sys.exit(app.exec_())
