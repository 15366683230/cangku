import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPalette,QFont,QBrush

#实例化类
class  APP(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        self.setWindowTitle('固定资产查询')
        self.show()
    #构建窗体
    def initui(self):
        horizontalHeader = ['资产编号', '类型', '资产名称', '事件类型', '责任处室', '责任人', '员工编号', \
                            '存放地点', '工单号']
        self.tw = QTableWidget(self)
        self.tw.setRowCount(5)
        self.tw.setColumnCount(len(horizontalHeader))
        self.tw.resize(1000,600)

        self.tw.setHorizontalHeaderLabels(horizontalHeader)

        for index in range(self.tw.columnCount()):
            headItem = self.tw.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 12, QFont.Bold))
            # headItem.setForeground(QBrush(Qt.gray))
            # headItem.setTextAlignment(Qt.AlignLeft|Qt.AlignVCenter)










if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = APP()
    sys.exit(app.exec_())