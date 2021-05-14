import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()

        if 'https://' in url:
            self.browser.setUrl(QUrl(url))
        elif 'www.' in url:
            if 'https://' in url:
                self.browser.setUrl(QUrl(url))
            elif 'https://' not in url:
                url = 'https://' + url
                self.browser.setUrl(QUrl(url))
        elif 'www.' not in url:
            url = input('search >>> ').replace(' ','+')
            template = f'https://www.google.com/search?ei=v04xYMemCYyf4-EPo_22sA4&q={url}&oq={url}&gs_lcp=Cgdnd3Mtd2l6EAMyBwguEEMQkwIyBAgAEAoyBggAEAoQAjIECC4QQzIGCAAQChACMgQIABAKMgQIABAKMgQIABBDMgQIABAKMgQIABAKOgoIABCxAxCwAxACOgcIABCwAxBDOg0IABCxAxCDARCwAxACOgsIABCxAxCDARCwAzoHCC4QsAMQQzoKCAAQsQMQgwEQQzoPCAAQsQMQgwEQAhCfARBDOgQIABACOgQILhACOgYIABAKEEM6AggAOgIILjoGCC4QChACOgQILhAKOgcILhANEJMCOgQIABANOgYIABANEAI6BAguEA1QtRFY5jhgqTpoAnAAeACAAcQBiAGnD5IBBDAuMTOYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz&ved=0ahUKEwiHgtH-hfnuAhWMzzgGHaO-DeYQ4dUDCA0&uact=5'
            self.browser.setUrl(QUrl(template))


    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('My Cool Browser')
window = MainWindow()
app.exec_()