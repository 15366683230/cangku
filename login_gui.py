from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QWidget, QInputDialog, QLineEdit, QMessageBox,\
    QLayout, QMainWindow, QHBoxLayout, QVBoxLayout,QGridLayout
from PyQt5.QtGui import  QPalette, QBrush, QPixmap, QIcon, QFont,QColor
from PyQt5.QtCore import Qt
import sys
import pymysql

#数据库地址
server = '127.0.0.1'

#登陆窗口
class APP(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    #创建UI界面
    def initUI(self):
        self.setWindowTitle('仓库管理系统')#标题
        self.setGeometry(500, 280, 1071, 588)#窗口尺寸
        self.setWindowIcon(QIcon('ICON.PNG'))
        self.bg = QPalette()     #创建调色板
        self.bg.setBrush(self.backgroundRole(),QBrush(QPixmap('1BG.PNG'))) #图片作为背景
        self.setPalette(self.bg) #实例化调色板

        # 创建标签
        self.user_label = QLabel('用户名:', self)
        self.user_label.setFont(QFont('楷体', 12, QFont.Bold))
        self.user_label.move(360, 143)
        self.password_label = QLabel('密 码：', self)
        self.password_label.setFont(QFont('楷体', 12, QFont.Bold))
        self.password_label.move(360, 230)
        #创建输入框
        self.text1 = QLineEdit(self)
        self.text1.move(420, 140)
        self.text2 = QLineEdit(self)
        self.text2.setEchoMode(QLineEdit.Password) #密码输入框显示
        self.text2.move(420, 227)
        #按钮
        self.btn1 = QPushButton('登陆',self)
        self.btn1.setGeometry(810, 400, 132, 82 )
        self.btn2 = QPushButton('退出', self)
        self.btn2.setGeometry(30, 450, 160, 50)
    #连接数据库
    def conndb(self):
        try:
            self.db = pymysql.connect(host = server, port = 3306, user = self.text1.text(),
                                  password = self.text2.text(),db = 'cangku')
            QMessageBox.information(self, '提示', '登陆成功')
            main_window.show()
            self.close()
        except:
            QMessageBox.warning(self,'提示', '登陆失败')



 #主界面
class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        #创建UI界面
    def initUI(self):
        layout = QGridLayout(self)
        v = QVBoxLayout()



        palete = QPalette()
        palete.setColor(QPalette.Window, Qt.blue)

        label = QLabel('系统')
        label.setAutoFillBackground(True)
        label.setPalette(palete)
        label.resize(100,10)
        btn = QPushButton('按钮')
        btn.resize(100,10)
        v.addWidget(label)
        v.addWidget(btn)

        layout.addLayout(v, 0, 0)








    def main_window(self):
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = APP()
    main_window = main_window()
    ex.btn1.clicked.connect(ex.conndb)
    ex.btn2.clicked.connect(ex.close)
    ex.show()
    sys.exit(app.exec_())
