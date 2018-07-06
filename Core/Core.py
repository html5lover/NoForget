'''
NoForget 2.1.0
by 9XPenguin (Ken Shibata)
Last Edited 07-06-2018
Uses SOftware (PyQt5) supplied by Riverbank Computing and Qt 5 supplied by The Qt Company.
This software is licensed under the GNU General Public License.
'''
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Root(QMainWindow):
    def __init__(self, QApp):
        super().__init__()
        self.QApp = QApp
    def setupUi(self):
        self.PLQuestions = [['<b>1/6</b><hr>時間割を確認しましたか？','1','2','3'],
                            ['<b>2/6</b><hr>教科書を入れましたか？','1','2','3'],
                            ['<b>3/6</b><hr>ノートを入れましたか？','1','2','3'],
                            ['<b>4/6</b><hr>給食の用意を入れましたか？','1','2','3'],
                            ['<b>5/6</b><hr>宿題を入れましたか？','1','2','3'],
                            ['<b>6/6</b><hr>筆箱を入れましたか？','1','2','3']]
        self.PLQuestionCounter = 0
        self.setWindowTitle('')
        self.showMaximized()
        self.QGLRoot = QGridLayout()
        self.QWTDummy = QWidget()
        self.setCentralWidget(self.QWTDummy)
        self.QWTDummy.setLayout(self.QGLRoot)
        self.QLBTool = QLabel(self)
        self.QLBTool.setText('Tool')
        self.QGLRoot.addWidget(self.QLBTool, 0, 0, 0, 3)
        self.QPB0 = QPushButton(self)
        self.QPB0.setText('0')
        self.QPB0.clicked.connect(self.updateUiQPB0)
        self.QGLRoot.addWidget(self.QPB0, 1, 0)
        self.QPB1 = QPushButton(self)
        self.QPB1.setText('1')
        self.QPB1.clicked.connect(self.updateUiQPB1)
        self.QGLRoot.addWidget(self.QPB1, 1, 1)
        self.QPB2 = QPushButton(self)
        self.QPB2.setText('2')
        self.QPB2.clicked.connect(self.updateUiQPB2)
        self.QGLRoot.addWidget(self.QPB2, 1, 2)
    def startUi(self):
        self.show()
        self.updateUi()
    def updateUi(self):
        self.QLBTool.setText(self.PLQuestions[self.PLQuestionCounter][0])
        self.QPB0.setText(self.PLQuestions[self.PLQuestionCounter][1])
        self.QPB1.setText(self.PLQuestions[self.PLQuestionCounter][2])
        self.QPB2.setText(self.PLQuestions[self.PLQuestionCounter][3])
    def updateUiQPB0(self):
        if self.PLQuestionCounter != len(self.PLQuestions) - 1:
            self.PLQuestionCounter += 1
        else:
            exit()
        self.updateUi()
    def updateUiQPB1(self):
        if self.PLQuestionCounter != len(self.PLQuestions) - 1:
            self.PLQuestionCounter += 1
        else:
            exit()
        self.updateUi()
    def updateUiQPB2(self):
        exit()
#        if self.PLQuestionCounter != len(self.PLQuestions) - 1:
#            self.PLQuestionCounter += 1
#        else:
#            exit()
#        self.updateUi()
QApp = QApplication(sys.argv)

App = Root(QApp)
App.setupUi()
App.startUi()

sys.exit(QApp.exec_())
