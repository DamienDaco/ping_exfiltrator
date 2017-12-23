try:
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except:
    print("[-] Import failed. PyQt5 library not found. \nTry installing it with: apt install python3-qt5")
    exit()

from ui.design_ping_exfiltrator import Ui_MainWindow
from app.logic import *
import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.interface_box.addItems(get_interfaces())
        self.selected_interface = str(self.interface_box.currentText())
        self.string_ip = self.ip_line.placeholderText()
        print("IP is %s" % self.string_ip)
        print(type(self.string_ip))

        self.logic = Logic(self.string_ip, self.selected_interface)
        self.ip_line.editingFinished.connect(self.process_ip)
        self.start_button.clicked.connect(self.logic.start_thread)
        self.stop_button.clicked.connect(self.logic.stop_thread)

    def process_ip(self):

        if self.ip_line.text():
            self.logic.binary_ip = clean_ip(self.ip_line.text())
            print("IP changed to %s " % self.ip_line.text())
        elif self.ip_line.placeholderText():
            self.logic.binary = clean_ip(self.ip_line.placeholderText())
            print("IP changed to %s " % self.ip_line.placeholderText())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
