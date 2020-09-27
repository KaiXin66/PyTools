# -*- coding: utf-8 -*-
import subprocess
import sys
from time import sleep

from PyQt5.QtWidgets import QMessageBox, QButtonGroup, QApplication, QMainWindow
from wmi import WMI

from ipswitch.netUi import UiMainWindow


class Window(UiMainWindow):

    def __init__(self, main_window):
        super().__init__()
        self.setupUi(main_window)
        block = QButtonGroup(main_window)
        block.addButton(self.radioButton, 1)
        block.addButton(self.radioButton_2, 2)
        self.pushButton.clicked.connect(lambda: self.assembleIpAddress(block))

    def assembleIpAddress(self, block):
        """组装ip地址，输出设置的可用ip"""
        check_id = block.checkedId()
        ip_address = {'mask': ['255.255.254.0']}
        if check_id == 1:
            ip = ['192.168.76.1']
            ip_address['gateway'] = ip
            ip_address['dns'] = ip
            ip_segments = ['192.168.77.', '192.168.76.']
            url = ip[0]
            self.outputMessage(ip_address, ip_segments, url)
        elif check_id == 2:
            ip_address['gateway'] = ['192.168.0.1']
            ip_address['dns'] = ['114.114.114.114']
            ip_segments = ['192.168.1.', '192.168.0.']
            url = 'www.baidu.com'
            self.outputMessage(ip_address, ip_segments, url)

    def outputMessage(self, ip_address, ip_segments, url):
        """输出结果消息"""
        for ip_segment in ip_segments:
            message = self.getIp(ip_address, ip_segment, url)
            QMessageBox.information(mainWindow, "提示", message)
            if '192.168' in message or '管理' in message:
                break

    @staticmethod
    def setIp(ip_address):
        """设置ip地址"""
        wmi_service = WMI()
        col_nic_configs = wmi_service.Win32_NetworkAdapterConfiguration(IPEnabled=True)
        if len(col_nic_configs) < 1:
            QMessageBox.information(mainWindow, "提示", "没有找到可用的网络适配器")
            return False
        else:
            obj_nic_config = col_nic_configs[0]
            return_value = obj_nic_config.EnableStatic(IPAddress=ip_address['ip'], SubnetMask=ip_address['mask'])
            if return_value[0] < 2:
                way_res = obj_nic_config.SetGateways(DefaultIPGateway=ip_address['gateway'], GatewayCostMetric=[1])
                if way_res[0] < 2:
                    dns_res = obj_nic_config.SetDNSServerSearchOrder(DNSServerSearchOrder=ip_address['dns'])
                    if dns_res[0] < 2:
                        sleep(3)
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

    def getIp(self, ip_address, ip_segment, url):
        """轮巡设置ip，返回可用ip"""
        num = 1
        message = ''
        while num < 255:
            ip_address['ip'] = [ip_segment + str(num)]
            print(ip_segment + str(num))
            if self.setIp(ip_address):
                if self.validIp(url):
                    message = ip_segment + str(num)
                    break
                else:
                    num += 1
                    if num == 255:
                        message = "没有找到可用的IP"
            else:
                message = "请以管理员身份运行程序"
                break
        return message

    @staticmethod
    def validIp(url):
        """验证ip是否可用"""
        cmd = 'ping -n 2 -w 3 ' + url
        result = subprocess.getstatusoutput(cmd)
        print(result)
        if result[0] == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Window(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
