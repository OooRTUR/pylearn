import  sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('time.png'))
        self.center()


        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())  # sizeHint() - подска для размера
        btn.move(50, 50) # перемещение относительно окна

        btn1 = QPushButton('Exit', self)
        btn1.clicked.connect(QCoreApplication.instance().quit)
        btn1.resize(btn1.sizeHint())
        btn1.move(150,50)

        self.setWindowTitle('Tooltips')

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()


    sys.exit(app.exec_())