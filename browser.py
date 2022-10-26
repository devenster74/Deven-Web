from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("file:///C:/Users/nsetp/OneDrive/Desktop/school/Deven's%20HTML/Simple%20Website.html"))
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)
        back_btn = QAction("🡸", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)
        next_btn = QAction("🡺", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)
        reload_btn = QAction("🔁", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)
        home_btn = QAction("🏠", self)
        home_btn.setStatusTip("Return to Deven Web Home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
        navtb.addSeparator()
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)
        stop_btn = QAction("🛑", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)
        self.show()
 
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - Deven Web" % title)
 
    def navigate_home(self):
 
        # open deven web
        self.browser.setUrl(QUrl("file:///C:/Users/nsetp/OneDrive/Desktop/school/Deven's%20HTML/Simple%20Website.html"))
 
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
 
        if q.scheme() == "":
            q.setScheme("http")
 
        self.browser.setUrl(q)
 
    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

app = QApplication(sys.argv)
app.setApplicationName("Deven Web")
window = MainWindow()
app.exec_()
