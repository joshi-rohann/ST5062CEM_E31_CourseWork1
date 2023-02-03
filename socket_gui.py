
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


import socket
import sys
from colorama import init, Fore
from termcolor import colored
import pyfiglet

init()
GREEN = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET


s = socket.socket()


def user_defined():
    host = "127.0.0.1"

    open_number = 0
    close_number = 0
    for port in range(130, 146):

        try:
            s.connect((host, port))
            s.settimeout(0.1)

        except:

            print(f"{RED}[!] The port {port} is closed.{RESET}")
            close_number += 1

        else:
            print(f"{GREEN}[+] The port {port} is open.{RESET}")
            open_number += 1
    print(
        f"the open ports are {open_number} and closed ports are {close_number}")


class PortScannerGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create a button for each function
        user_defined_button = QPushButton("User-defined function")
        user_input_button = QPushButton("Scan user-specified list of ports")
        scan_all_button = QPushButton("Scan all ports")
        port_range_button = QPushButton("Scan range of ports")
        quit_button = QPushButton("Quit")

        # Create a vertical layout to hold the buttons
        layout = QVBoxLayout()
        layout.addWidget(user_defined_button)
        layout.addWidget(user_input_button)
        layout.addWidget(scan_all_button)
        layout.addWidget(port_range_button)
        layout.addWidget(quit_button)

        # Set the layout of the main window
        self.setLayout(layout)

        # Connect the buttons to their respective functions
        user_defined_button.clicked.connect(user_defined)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = PortScannerGUI()
    gui.show()
    sys.exit(app.exec_())
