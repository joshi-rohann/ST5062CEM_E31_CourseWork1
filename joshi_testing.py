# Created by Rohan Joshi (Student ID: 210307)
import socket
import sys
from pyfiglet import Figlet     # if not installed use >> `pip install pyfiglet`
# if not installed use >> `pip install colorama`
from colorama import init, Fore, Style
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


init()
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
RESET = Fore.RESET
BRIGHT = Style.BRIGHT


def third_window():

    for widget in window.winfo_children():
        if widget != background_label:
            widget.destroy()
    text_area = tk.Text(window)
    text_area.pack(pady=46)

    def user_defined():
        '''The user defined function is used for scanning the localhost with ports from 135 whose value are given while calling the function.'''
        target = '127.0.0.1'
        open_number = 0
        close_number = 0
        for port in range(134, 138):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((target, port))
            if result == 0:
                text_area.insert(
                    tk.END, f"[+] The port {port} is open on {target}\n")
                open_number += 1

                #defined_text = f"[+] The port {port} is open on {target}"
                # defined_label = tk.Label(
                #     window, text=defined_text, background="#072F5F", foreground="white")
                # defined_label.pack()

            else:
                text_area.insert(
                    tk.END, f"[-] The port {port} is closed on {target}\n")
                close_number += 1
        text_area.insert(tk.END, "\n")
        text_area.insert(
            tk.END, f"[-] The closed ports are {close_number} and open ports are {open_number}\n")
        text_area.insert(tk.END, "\n")
        text_area.insert(tk.END, "\n")
        text_area.insert(tk.END,
                         "Scanning the ports from range 134 to 137 was successful !!!\n")

        s.close()
        back = tk.Button(window, text="Take me back", command=second_window, background="#072F5F", foreground="white",
                         font=('Times New Roman', 15))
        back.pack(pady=15)

    user_defined()


def second_window():
    for widget in window.winfo_children():
        if widget != background_label:
            widget.destroy()

    user_defined_button = tk.Button(window, text="scanning the localhost with ports from 135", background="#072F5F", foreground="white",
                                    font=('Times New Roman', 15), command=third_window)
    user_defined_button.pack(pady=15)

    single_port_button = tk.Button(window, text="scanning the list of ports of the given target", background="#072F5F", foreground="white",
                                   font=('Times New Roman', 15))
    single_port_button.pack(pady=15)

    range_port_button = tk.Button(window, text="Scan ports of specific range", background="#072F5F", foreground="white",
                                  font=('Times New Roman', 15))
    range_port_button.pack(pady=15)

    multi_port_button = tk.Button(window, text="Scan user-specified list of ports", background="#072F5F", foreground="white",
                                  font=('Times New Roman', 15))
    multi_port_button.pack(pady=15)

    all_port_button = tk.Button(window, text="scan all the ports of the given target", background="#072F5F", foreground="white",
                                font=('Times New Roman', 15))
    all_port_button.pack(pady=15)

    back = tk.Button(window, text="Take me back", command=first, background="#072F5F", foreground="white",
                     font=('Times New Roman', 15))
    back.pack(pady=15)


window = tk.Tk()
window.title("Port Scanner")
window.geometry("940x660")

global image
image = PhotoImage(file="python.png")
background_label = ttk.Label(window, image=image)

background_label.place(x=0, y=0, relwidth=1, relheight=1)


def first():
    for widget in window.winfo_children():
        if widget != background_label:
            widget.destroy()

    text1 = ttk.Label(window, text="Port Scanning", background="#072F5F", foreground="white",
                      font=('Times New Roman', 36, 'bold'))
    text1.pack(pady=34)

    text2 = ttk.Label(window, text="Created by Rohan Joshi", background="#072F5F", foreground="white",
                      font=('Times New Roman', 19, 'italic'))
    text2.pack()

    scan_button = tk.Button(window, text="Scanning Options",
                            font=('Times New Roman', 15), command=second_window)
    scan_button.pack(pady=15)


first()
window.mainloop()


def singleportinput():
    '''The function is used for scanning the single port of the given target through the user input.'''
    target = input("Enter the target IP: ")
    port = int(input("Enter the port number of the target to scan: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"\n{GREEN}[+] The port {port} is open on {target}{RESET}")
    else:
        print(f"\n{RED}[!] The port {port} is close on {target}{RESET}")
    s.close()
    print("-"*80, end='\n\n')


def multiportinput(target, ports):
    '''The function is used for scanning the list of ports of the given target.'''
    print('\n')
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, int(port)))
        if result == 0:
            print(f"{GREEN}[+] The port {port} is open on {target}{RESET}")
        else:
            print(f"{RED}[!] The port {port} is close on {target}{RESET}")
        s.close()
    print("-"*80, end='\n\n')


def rangeportinput(target, start, end):
    '''The function is used to scan the range of ports of the given target.'''
    print('\n')
    op = 0
    cp = 0
    for port in range(start, end+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{GREEN}[+] The port {port} is open on {target}{RESET}")
            op += 1
        else:
            print(f"{RED}[!] The port {port} is close on {target}{RESET}")
            cp += 1
        s.close()
    print(
        f"\nThe number of ports status are:\nOpened Ports:\t{op}\nClosed Ports:\t{cp}")
    print("-"*80, end='\n\n')


def allportscan(target):
    '''The function is used to scan all the ports of the given target.'''
    print('\n')
    op = 0
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{GREEN}[+] The port {port} is open on {target}{RESET}")
            op += 1
        s.close()
    print(
        f"\nThe number of ports status are:\nOpened Ports:\t{op}\nClosed Ports:\t{65535-op}")
    print("-"*80, end='\n\n')


# if __name__ == '__main__':
#     while True:
#         print("Press '1' to run the user defined function. Here, target 127.0.0.1 and port 135.")
#         print("Press '2' to run user input function for url and a port.")
#         print("Press '3' to run user input function for url and multiple ports.")
#         print("Press '4' to run user input function for url and range of ports.")
#         print("Press '5' to run user input function for url and all ports.")
#         print("Press '6' to exit the program")
#         op = input("Enter your selection: ")

#         if op == '1':
#             user_defined('127.0.0.1', 135)

#         elif op == '2':
#             singleportinput()

#         elif op == '3':
#             host = input("Enter the IP of your target: ")
#             ports_collection = input(
#                 "Enter the ports to be scanned seperated with ',': ")
#             ports_collection = ports_collection.replace(" ", "")
#             ports = ports_collection.split(',')
#             multiportinput(host, ports)

#         elif op == '4':
#             host = input("Enter the IP of the target: ")
#             ports_range = input("Enter the range of the ports using '-': ")
#             ports = ports_range.split('-')
#             rangeportinput(host, int(ports[0]), int(ports[1]))

#         elif op == '5':
#             print(
#                 f"\n{RED}You are choosing to scan all the ports so it might take time (Approx. 90 min maximum).{RESET}\n")
#             host = input("Enter the IP of the target: ")
#             allportscan(host)

#         elif op == '6':
#             print(f"\n{BLUE}{BRIGHT}Terminating the program...{RESET}\n")
#             sys.exit()

#         else:
#             print('\n')
#             print('*'*30)
#             print(
#                 f"{RED}:(\t:(\t:(\t:(\nThere is the error in the input.\nPlease choose the choice wisely.{RESET}")
#             print('*'*30)
#             print('\n')
