from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMenuBar,QAction,qApp,QVBoxLayout,\
    QHBoxLayout, QGridLayout,QLabel,QMessageBox,QMainWindow, QStatusBar,QCalendarWidget,QGroupBox
from PyQt5.QtGui import QFont, QPalette,QPixmap,QBrush,QColor
import sys


class APP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()

    #关闭窗口询问
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示', '确定要退出系统',QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.YES:
            event.accept()
        else:
            event.ignore()
    #创建UI
    def initui(self):
        self.setWindowTitle('首页')
        self.resize(1100, 600)
        self.setFixedSize(self.width(), self.height())
        #添加菜单栏
        fileaction = QAction('新建窗口', self)
        fileaction.setShortcut('CTRL+C')
        exitaction = QAction('退出', self)
        exitaction.setShortcut('CTRL+Q')
        exitaction.triggered.connect(qApp.quit)
        menubar = QMenuBar(self)
        menu = menubar.addMenu('菜 单')
        menu.addAction(fileaction)
        menu.addAction(exitaction)

        #创建控件
        label = QLabel('仓库管理系统',self)
        label.move(0,20)
        label.resize(10000,100)
        label.setFont(QFont('隶书',20))
        palettle = QPalette()
        palettle.setBrush(self.backgroundRole(), QBrush(QPixmap('title.PNG')))
        label.setAutoFillBackground(True)
        label.setPalette(palettle)

        btn1 = QPushButton('基本资料',self)
        btn1.move(200, 150)
        btn2 = QPushButton('入库管理',self)
        btn2.move(297, 150)
        btn3 = QPushButton('出库管理',self)
        btn3.move(394, 150)
        btn4 = QPushButton('仓库管理',self)
        btn4.move(491, 150)
        btn5 = QPushButton('明细报表',self)
        btn5.move(588, 150)
        btn6 = QPushButton('统计报表',self)
        btn6.move(685, 150)
        btn7 = QPushButton('系统设置',self)
        btn7.move(782, 150)

        groupbox1 = QGroupBox('固定资产',self)
        groupbox1.setGeometry(200, 190 ,340,360)
        groupbox2 = QGroupBox('IT配件', self)
        groupbox2.setGeometry(550, 190, 340, 360)
        groupbox1.setStyleSheet('QGroupBox{ border: 1px groove red; border-radius:5px;border-style: inset;}')
        groupbox2.setStyleSheet('QGroupBox{ border: 1px groove blue; border-radius:5px;border-style: inset;}')

        btna = QPushButton('出库管理')
        btnb = QPushButton('入库管理')
        btnc = QPushButton('员工信息')
        btnd = QPushButton('部门信息')

        btn21 = QPushButton('出库管理')
        btn22 = QPushButton('入库管理')
        btn23 = QPushButton('配件信息')
        btn24 = QPushButton('资产信息')

        gbox = QGridLayout(groupbox1)
        gbox.addWidget(btna, 0, 0)
        gbox.addWidget(btnb, 0, 1)
        gbox.addWidget(btnc, 1, 0)
        gbox.addWidget(btnd, 1, 1)

        gbox2 = QGridLayout(groupbox2)
        gbox2.addWidget(btn21, 0, 0)
        gbox2.addWidget(btn22, 0, 1)
        gbox2.addWidget(btn23, 1, 0)
        gbox2.addWidget(btn24, 1, 1)

        groupbox1.setLayout(gbox)
        groupbox2.setLayout(gbox2)


        statusbar = QStatusBar(self)
        statusbar.move(0,570)
        statusbar.showMessage('操作员:',     )

        self.show()

if __name__ == '__main__':

	app = QApplication(sys.argv)
	win = APP()
	sys.exit(app.exec_())
