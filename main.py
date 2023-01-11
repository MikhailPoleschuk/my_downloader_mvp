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

      self.ui.pushButton.clicked.connect(self.test)

   def test(self) -> None:
      yt = YouTube('https://youtu.be/q3ma5waVGb0')
      videos = yt.streams.filter(file_extension='mp4')
      for v in videos:
         print(v.itag)
      stream = yt.streams.get_by_itag(18)
      stream.download()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DownLoader()
    window.show()

    sys.exit(app.exec())














