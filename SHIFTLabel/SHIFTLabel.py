from PyQt5 import Qt
from PyQt5 import QtCore
import sys
import cv2
import os

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from pathlib import Path

import numpy as np

from shutil import copyfile

class Image_info(Qt.QWidget):
    def __init__(self):
            super().__init__()
            self.initUI()
    def initUI(self):
            self.label_ind=Qt.QLabel('this is result')
    

class MainWindow(Qt.QWidget):
	keyPressed = QtCore.pyqtSignal()
	def keyPressEvent(self, event):
		#print(event.key())
		#if event.key() == QtCore.Qt.Key_Q:
	#		print ("Killing")
#			self.deleteLater()
#		elif event.key() == QtCore.Qt.Key_Enter:
#			self.proceed()
		if(event.key() == QtCore.Qt.Key_1):
			self.save_categori(1)
			self.next_im()
		if(event.key() == QtCore.Qt.Key_2):
			self.save_categori(2)
			self.next_im()
		if(event.key() == QtCore.Qt.Key_3):
			self.save_categori(3)
			self.next_im()
		event.accept()
        
        
	def __init__(self):
            super().__init__()
            self.initUI()
        
        
	def initUI(self):
		#app=Qt.QApplication(sys.argv)
            #Qt.QToolTip.setFont(Qt.QFont('SansSerif', 10))

            #self.setToolTip('This is a <b>QWidget</b> widget')
            self.image_info=Qt.QLabel('',self)
            self.image_info.setGeometry(0,0,200,500)
            #btn = Qt.QPushButton('Button', self)
            #btn.setToolTip('This is a <b>QPushButton</b> widget')
            #btn.resize(btn.sizeHint())
            #btn.move(20, 20)
            #btn.clicked.connect(self.load_image)
           
            #self.tw = Qt.QTreeWidget(self)
            #self.tw.setSelectionMode(Qt.QTreeWidget.ExtendedSelection)
            #self.tw.move(20,80)
            #self.tw.resize(300,200)
            #self.tw.setColumnCount(1)
            #self.tw.setHeaderLabels(["filename"])
            
            #self.cur_dir=os.getcwd()
            
            #self.cur_dir = str(Path.home())
            #self.list_files=os.listdir(self.cur_dir)
           
            #for l in self.list_files:
                #if(not '.' in l):
            #        it=Qt.QTreeWidgetItem([l])
             #       self.tw.addTopLevelItem(it)
    
            #self.tw.doubleClicked.connect(self.open_path)
            self.content_path='SHIFTLab_data/'
            self.class_1_path=self.content_path+'class1/'
            self.class_2_path=self.content_path+'class2/'
            self.class_3_path=self.content_path+'class3/'
            os.mkdir(self.content_path)
            os.mkdir(self.class_1_path)
            os.mkdir(self.class_2_path)
            os.mkdir(self.class_3_path)
            self.open_dir='../clean_data/'
            self.files=os.listdir(self.open_dir)
            self.cur_ind=0
            #print(len(self.files))
            self.canv = PlotCanvas(self, width=12, height=9)
            self.canv.move(300,0)
            #self.load_image()
            self.setGeometry(300, 300, 1400, 1000)
            #self.setWindowTitle('Tooltips')
            self.show()
           # self.load_image(self.open_dir+self.files[self.cur_ind])
            #self.canv.fig.canvas.mpl_connect('key_press_event', self.key_press)
            
            #self.image_info=Image_info(self)
            #self.move(0,0)
            #self.setGeometry(100,100,200,200)
	def load_image(self,im_name):
                self.im=cv2.imread(im_name,cv2.IMREAD_UNCHANGED)
                self.canv.plot_im(self.im)
                #print(self.im.shape)
	def next_im(self):
		if(self.cur_ind<len(self.files)):
			
			#print(self.cur_ind)
			self.load_image(self.open_dir+self.files[self.cur_ind])
			#self.image_info.setText(self.files[self.cur_ind])
			text_data=''
			text_data+=f'{self.cur_ind}/{len(self.files)}\n'
			text_data+=f'name image: {self.files[self.cur_ind]}\n'
			text_data+=f'size of image: {self.im.shape}\n'
            #text_data+=f'size of image: {self.im.shape}\n'
			
			self.cur_ind+=1
			
			self.show_data(text_data)
            
	def save_categori(self,categori):
		try:
			if(categori==1):
                #copyfile(self.open_dir+self.files[self.cur_ind-1],self.class_1_path+self.files[self.cur_ind-1])
				cv2.imwrite(self.class_1_path+self.files[self.cur_ind-1],self.im)
			if(categori==2) :
                #copyfile(self.open_dir+self.files[self.cur_ind-1],self.class_2_path+self.files[self.cur_ind-1])
				cv2.imwrite(self.class_2_path+self.files[self.cur_ind-1],self.im)
			if(categori==3):
                #copyfile(self.open_dir+self.files[self.cur_ind-1],self.class_3_path+self.files[self.cur_ind-1])
				cv2.imwrite(self.class_3_path+self.files[self.cur_ind-1],self.im)
		except:
			print('error')
	def show_data(self,text):
		self.image_info.setText(text)
        
        
        
            
        
        
 
 
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
            self.fig = Figure(figsize=(width, height), dpi=dpi)
            #self.axes = fig.add_subplot(111)
            self.ax = self.fig.add_subplot(111)
            
            FigureCanvas.__init__(self, self.fig)
            self.setParent(parent)
            #cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
            #kid = self.fig.canvas.mpl_connect('key_press_event', self.press)
            FigureCanvas.setSizePolicy(self,
                    0,
                    0)
            FigureCanvas.updateGeometry(self)
            #self.plot()


    def plot_im(self,data):
            #self.data=data
            #data = [random.random() for i in range(25)]
            
            #ax.plot(data, 'r-')
            self.ax.clear()
            self.ax.axis('off')
            self.ax.imshow(data)
            #ax.set_title('PyQt Matplotlib Example')
            self.draw()
    def onclick(self,event):
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
         ('double' if event.dblclick else 'single', event.button,
         event.x, event.y, event.xdata, event.ydata))
        #self.data[int(event.ydata):,int(event.xdata):]=0
        #self.ax.imshow(self.data)
        self.lastx=event.xdata
        self.lasty=event.ydata
        self.ax.scatter(x=event.xdata,y=event.ydata,color='red')
        self.ax.plot(x=[event.xdata,self.lastx],y=[event.ydata,self.lasty],color='blue',style='-o')
        self.draw()
    def press(self,event):
        print(event.key)

if __name__=='__main__':
	#print('hello world')
        app=Qt.QApplication(sys.argv)	
        mw=MainWindow()
        sys.exit(app.exec_())
        
