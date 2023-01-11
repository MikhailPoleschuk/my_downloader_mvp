import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from mvp import Ui_MainWindow
from pytube import YouTube


class DownLoader(QMainWindow):
   def __init__(self):
      super(DownLoader, self).__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      # self.do_when_password_edit()
      self.ui.pushButton_3.clicked.connect(self.clicl_ok)
      # self.ui.pushButton.clicked.connect(self.sourse)
      self.ui.pushButton_2.clicked.connect(self.downloads)
      print(self.ui.comboBox.currentText())

   def clicl_ok(self) -> None:
      try:
         url=self.ui.lineEdit.text()
         print(url)
         yt = YouTube(url)
         videos = yt.streams.filter(file_extension='mp4')
         list1 = []                 
         str_=''
         for v in videos:
               
            list1.append(str(v.itag))
         print(*list1) 
         self.ui.comboBox.addItems(list1)
      # print(self.ui.comboBox.currentText())  
         # stream = yt.streams.get_by_itag(18)
         # stream.download()
      except:
         url=self.ui.lineEdit.setText("error") 
      

   def downloads(self):
      pass

   def combobox_select(self):
      print(self.ui.comboBox.currentText())
   
   # def do_when_password_edit(self) -> None:
   #      self.ui.lineEdit.textEdited.connect(self.sourse)

      


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DownLoader()
    window.show()

    sys.exit(app.exec())
