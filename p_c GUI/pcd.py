# ProducterAndConsumer
import sys
#from time import sleep
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, \
    QGridLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer



class Example(QWidget):

    
    
    def __init__(self):
        """初始化"""
        super().__init__()  # 初始化父类
        self.counter=1#产品计数
        self.product=""
        self.flag=0#判断quit时候是什么操作
        self.initUI()

    def word_style(self):
        """定义文字格式"""

        font1 = QFont()
        font1.setFamily('consolas')  # 字体的类型
        font1.setBold(True)  # 将文字加粗
        font1.setPointSize(14)  # 字体的大小

        font2 = QFont()
        font2.setFamily('consolas')
        font2.setPointSize(8)

        font3 = QFont()
        font3.setFamily('consolas')
        font3.setPointSize(8)
        return font1, font2, font3

    def initUI(self):
        """创建一个GUI"""

        """创建组件"""

        # 定义文字的样式
        self.font1, self.font2, self.font3 = self.word_style()

        # 标签
        self.labelCenter = QLabel(self)
        self.labelCenter.setText('')
        self.labelCenter.setGeometry(300, 100, 450, 131)

        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)
        self.label6 = QLabel(self)
        self.label1.setGeometry(10, 130, 54, 15)
        self.label2.setGeometry(10, 320, 54, 15)
        self.label3.setGeometry(10, 510, 54, 15)
        self.label4.setGeometry(850, 130, 54, 15)
        self.label5.setGeometry(850, 320, 54, 15)
        self.label6.setGeometry(850, 510, 54, 15)
        
        # 文本
        self.lineEdit1 = QLineEdit(self)
        self.lineEdit2 = QLineEdit(self)
        self.lineEdit3 = QLineEdit(self)
        self.lineEdit4 = QLineEdit(self)
        self.lineEdit5 = QLineEdit(self)
        self.lineEdit6 = QLineEdit(self)
        self.lineEdit1.setReadOnly(True)
        self.lineEdit2.setReadOnly(True)
        self.lineEdit3.setReadOnly(True)
        self.lineEdit4.setReadOnly(True)
        self.lineEdit5.setReadOnly(True)
        self.lineEdit6.setReadOnly(True)


        

        # 按钮
        self.proButton1 = QPushButton(self)
        self.proButton1.setText('生产者1')
        self.proButton2 = QPushButton(self)
        self.proButton2.setText('生产者2')
        self.proButton3 = QPushButton(self)
        self.proButton3.setText('生产者3')

        self.conButton1 = QPushButton(self)
        self.conButton1.setText('消费者1')
        self.conButton2 = QPushButton(self)
        self.conButton2.setText('消费者2')
        self.conButton3 = QPushButton(self)
        self.conButton3.setText('消费者3')

        self.ButtonQuit = QPushButton(self)
        self.ButtonQuit.setText('退出管程')
        # 设置按钮上的字体
        self.proButton1.setFont(self.font2)
        self.proButton2.setFont(self.font2)
        self.proButton3.setFont(self.font2)
        self.conButton1.setFont(self.font2)
        self.conButton2.setFont(self.font2)
        self.conButton3.setFont(self.font2)

        self.wavehouse = [self.lineEdit1, self.lineEdit2, self.lineEdit3,self.lineEdit4, self.lineEdit5, self.lineEdit6]  # 仓库空间
        self.buttonlist = [self.proButton1, self.proButton2, self.proButton3,self.conButton1,self.conButton2,self.conButton3]  # 阻塞队列
        self.monitorlist= [self.label1,self.label2,self.label3,self.label4,self.label5,self.label6]
        '''添加组件'''
        self.proButton1.setGeometry(50, 100, 111, 71)
        self.proButton2.setGeometry(50, 290, 111, 71)
        self.proButton3.setGeometry(50, 480, 111, 71)
        self.conButton1.setGeometry(720, 100, 111, 71)
        self.conButton2.setGeometry(720, 290, 111, 71)
        self.conButton3.setGeometry(720, 480, 111, 71)
        self.ButtonQuit.setGeometry(360, 490, 141, 51)

        self.lineEdit1.setGeometry(180, 300, 81, 41)
        self.lineEdit2.setGeometry(270, 300, 81, 41)
        self.lineEdit3.setGeometry(360, 300, 81, 41)
        self.lineEdit4.setGeometry(450, 300, 81, 41)
        self.lineEdit5.setGeometry(540, 300, 81, 41)
        self.lineEdit6.setGeometry(630, 300, 81, 41)
        '''添加事件'''

        # 生产者
        self.proButton1.clicked.connect(self.pressP)
        self.proButton2.clicked.connect(self.pressP)
        self.proButton3.clicked.connect(self.pressP)

        # 消费者
        self.conButton1.clicked.connect(self.pressC)
        self.conButton2.clicked.connect(self.pressC)
        self.conButton3.clicked.connect(self.pressC)

        #退出管程
        self.ButtonQuit.clicked.connect(self.quit)

        #刚开始无法消费
        self.conButton1.setEnabled(False)
        self.conButton2.setEnabled(False)
        self.conButton3.setEnabled(False)
        #刚开始管程没启动
        self.ButtonQuit.setEnabled(False)
        '''基本设置'''
        self.resize(906, 632)
        self.setWindowTitle('生产者-消费者问题')
        self.show()

        self.timerout=QTimer()
        self.timerout.start(4000)
        self.timerout.timeout.connect(self.randomshot)
        
        

    def randomshot(self):
            op = randint(1,6)
            if op==1:
                self.proButton1.click()
            elif op==2:
                self.proButton2.click()
            elif op==3:
                self.proButton3.click()
            elif op==4:
                self.conButton1.click()
            elif op==5:
                self.conButton2.click()
            elif op==6:
                self.conButton3.click()
            else:
                print("参数错误")#uesless

    def pressP(self):
        """处理生产者按钮按下产生的事件"""
        self.ButtonQuit.setEnabled(True)#启动管程
        self.flag=1
        source = self.sender()
        producer = source.text()  # 指明哪一个生产者
        if producer[-1] == '1':
            self.label1.setText("->")
            self.label1.setStyleSheet('color:red')
            self.proButton1.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif producer[-1] == '2':
            self.label2.setText("->")
            self.label2.setStyleSheet('color:red')
            self.proButton2.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            self.label3.setText("->")
            self.label3.setStyleSheet('color:red')
            self.proButton3.setStyleSheet("background-color: rgb(255, 0, 0);")

        self.product="第"+str(self.counter)+"pro"
        self.counter+=1
        self.labelCenter.setText("生产者"+producer[-1]+" 正在使用管程访问临界区...\n生产 "+self.product+" 中")

        
        for button in self.buttonlist:#所有其他程序停止
            button.setEnabled(False)
        
        self.timer=QTimer()
        self.timer.start(2000)
        self.timer.timeout.connect(self.quit)  
             
        

        
        
    def pressC(self):
        self.ButtonQuit.setEnabled(True)#启动管程
        self.flag=-1
        source = self.sender()
        consumer = source.text()  # 指明哪一个消费者
        if consumer[-1] == '1':
            self.label4.setText("<-")
            self.label4.setStyleSheet('color:red')
            self.conButton1.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif consumer[-1] == '2':
            self.label5.setText("<-")
            self.label5.setStyleSheet('color:red')
            self.conButton2.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            self.label6.setText("<-")
            self.label6.setStyleSheet('color:red')
            self.conButton3.setStyleSheet("background-color: rgb(255, 0, 0);")

        self.labelCenter.setText("消费者"+consumer[-1]+" 正在使用管程访问临界区...")
        
        for button in self.buttonlist:
            button.setEnabled(False)
        
        self.timer=QTimer()
        self.timer.start(2000)
        self.timer.timeout.connect(self.quit)  


    

    def quit(self):
        self.timer.stop()
        for item in self.buttonlist:
            item.setStyleSheet("background-color: rgb(225, 225, 225);")

        for item in self.monitorlist:#标识复位
            item.setText("")
            
        if self.flag==1:#消费操作
            self.flag=0 
            self.labelCenter.setText("生产结束 退出管程")
            for i in range(4,-1,-1):
                self.wavehouse[i+1].setText(self.wavehouse[i].text())
            self.wavehouse[0].setText(self.product)

            if self.lineEdit6.text()!='':#满了只允许消费
                self.conButton1.setEnabled(True)
                self.conButton2.setEnabled(True)
                self.conButton3.setEnabled(True)
            else:
                for button in self.buttonlist:
                    button.setEnabled(True)

        elif self.flag==-1:
            self.flag=0
            for i in range(5,-1,-1):
                if self.wavehouse[i].text()!='':
                    self.labelCenter.setText("消费了"+self.wavehouse[i].text()+" 退出管程")
                    self.wavehouse[i].setText('')
                    break

            if self.lineEdit1.text()=='':#空了只允许生产
                self.proButton1.setEnabled(True)
                self.proButton2.setEnabled(True)
                self.proButton3.setEnabled(True)
            else:
                for button in self.buttonlist:
                    button.setEnabled(True)
        
        else:
            print("参数错误")#uesless

        self.ButtonQuit.setEnabled(False)#退出时候管程关闭


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())