# -*- coding: utf-8 -*-

import sys
import time
from subprocess import run

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from crawl.grep import Ui_MainWindow


class Window(Ui_MainWindow):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi(mainWindow)
        self.pushButton.clicked.connect(lambda: self.startChrome())
        self.pushButton_2.clicked.connect(lambda: self.search())

    def startChrome(self):
        self.thread = RunThread()
        self.thread.start()

    def search(self):
        # 获取关键字
        world = self.lineEdit.text()
        if len(world) == 0:
            world = "whatsapp"
        # 获取网络服务名称
        network_name = self.lineEdit_2.text()
        if len(network_name) == 0:
            network_name = "以太网专用网络"
        # 关闭网络服务
        cmd_stop_net = 'netsh interface set interface name="' + network_name + '" admin=DISABLED'
        run(cmd_stop_net, shell=True)
        time.sleep(1)
        # 查找文档中所有a标签
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            chrome_driver = "chromedriver.exe"
            driver = webdriver.Chrome(chrome_driver, options=chrome_options)
            urls = driver.find_elements_by_xpath("//a")
            result = set()
            for url in urls:
                if world in url.text:
                    # print(url.text)
                    result.add(url.text)
            self.outputFile(result, world)
        except:
            QMessageBox.information(mainWindow, "提示", "无法连接")
        # 启动网络服务
        cmd_start_net = 'netsh interface set interface name="' + network_name + '" admin=ENABLED'
        run(cmd_start_net, shell=True)

    def outputFile(self, result, world):
        # 扫描结果个数
        mycount = len(result)
        if mycount > 0:
            # 设置输出文件名
            filename = world + "_" + str(int(time.time())) + ".txt"
            f = open(filename, 'w', encoding='utf-8')  # 文件路径、操作模式、编码  # r''
            for a in result:
                f.write(a + "\n")
            f.close()
            message = str(mycount) + "个扫描结果已写入到<" + filename + ">文件中"
            QMessageBox.information(mainWindow, "提示", message)
        else:
            QMessageBox.information(mainWindow, "提示", "扫描到0个结果")


class RunThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, parent=None):
        super(RunThread, self).__init__()

    def run(self):
        cmd_str = 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"'
        # os.system(cmd_str)
        run(cmd_str, shell=True)
        self.trigger.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Window(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
