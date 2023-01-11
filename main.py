import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from mvp import Ui_MainWindow
from pytube import YouTube


class DownLoader(QMainWindow):
   url=''
   yt = None
   stream=None

   def __init__(self):
      super(DownLoader, self).__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.ui.pushButton_3.clicked.connect(self.clicl_ok)
      self.ui.pushButton_2.clicked.connect(self.downloads)
      self.ui.comboBox.currentTextChanged.connect(self.comboBox_changed)
      

   def clicl_ok(self) -> None:
      
      try:
         global url, yt
         list1=[]
         url=self.ui.lineEdit.text()
         print(url)
         yt = YouTube(url)
         videos = yt.streams.filter(file_extension='mp4')
         for v in videos:
            list1.append(str(v.itag))
         self.ui.comboBox.addItems(list1)
         


      except:
         url=self.ui.lineEdit.setText("error") 
      

   def downloads(self):
      global stream
      try:
         stream.download()
      except:
         print("не захотел качаться") 

      print("download OK")
  
   def comboBox_changed(self, s): # s — это str
      global stream
      print(s)
      stream = yt.streams.get_by_itag(s)
      print(stream)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DownLoader()
    window.show()

    sys.exit(app.exec())
