try:
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except:
    print("[-] Import failed. PyQt5 library not found. \nTry installing it with: apt install python3-qt5")
    exit()

from ui.design_ping_exfiltrator import Ui_MainWindow
from app.logic import *
import sys


class EmittingStream(QObject):

    text_written = pyqtSignal(str)

    def write(self, text):
        self.text_written.emit(str(text))

    def flush(self):
        pass

'''
I was forced to implement the flush method because of a bug when exiting the program.
This didn't happen before in PyQt4. I don't know why PyQt5 behaves like that.
'''


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.original_stdout = sys.stdout
        sys.stdout = EmittingStream(text_written=self.normal_output_written)

        self.interface_box.addItems(get_interfaces())
        self.selected_interface = str(self.interface_box.currentText())
        self.string_ip = self.ip_line.placeholderText()
        print("IP is %s" % self.string_ip)
        print(type(self.string_ip))
        self.sender_button.toggle()

        self.logic = Logic(self.string_ip, self.selected_interface)
        self.ip_line.editingFinished.connect(self.process_ip)
        self.start_button.clicked.connect(self.logic.start_thread)
        self.stop_button.clicked.connect(self.logic.stop_thread)

        self.sender_button.toggled.connect(self.button_toggled)

    def process_ip(self):

        if self.ip_line.text():
            self.logic.binary_ip = clean_ip(self.ip_line.text())
            print("IP changed to %s " % self.ip_line.text())
        elif self.ip_line.placeholderText():
            self.logic.binary = clean_ip(self.ip_line.placeholderText())
            print("IP changed to %s " % self.ip_line.placeholderText())

    def button_toggled(self):

        if self.sender_button.isChecked():
            print("Sender mode enabled")
            self.start_button.setDisabled(False)
            self.stop_button.setDisabled(False)
            self.ip_line.setDisabled(False)

        elif self.receiver_button.isChecked():
            print("Receiver mode enabled")
            self.start_button.setDisabled(True)
            self.stop_button.setDisabled(True)
            self.ip_line.setDisabled(True)

    def normal_output_written(self, text):                  # Manage output to window

        self.cursor = self.text_browser.textCursor()             # These methods allow output without newlines. Better than append.
        self.cursor.movePosition(self.cursor.End)
        self.cursor.insertText(text)
        self.text_browser.setTextCursor(self.cursor)
        self.text_browser.ensureCursorVisible()

    # def __del__(self):                                      # Restore normal output
    #     # Restore sys.stdout
    #     sys.stdout = self.original_stdout


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
