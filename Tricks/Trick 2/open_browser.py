import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl("https://www.google.com"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName("a.exe")

    window = SimpleBrowser()
    window.show()

    sys.exit(app.exec_())
