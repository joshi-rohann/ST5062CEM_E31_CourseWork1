import customtkinter as ct
import socket

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")


window = ct.CTk()
window.title("Port Scanner")
window.geometry("640x460")


def third_window():

    for widget in window.winfo_children():
        widget.destroy()
    text_area = ct.CTkTextbox(window)
    text_area.configure(width=369, height=210)
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
                    ct.END, f"[+] The port {port} is open on {target}\n")
                open_number += 1

                # defined_text = f"[+] The port {port} is open on {target}"
                # defined_label = ct.Label(
                #     window, text=defined_text, background="#072F5F", foreground="white")
                # defined_label.pack()

            else:
                text_area.insert(
                    ct.END, f"[-] The port {port} is closed on {target}\n")
                close_number += 1
        text_area.insert(ct.END, "\n")
        text_area.insert(
            ct.END, f"[-] The closed ports are {close_number} and open ports are {open_number}\n")
        text_area.insert(ct.END, "\n")
        text_area.insert(ct.END, "\n")
        text_area.insert(ct.END,
                         "Scanning the ports from range 134 to 137 was successful !!!\n")

        s.close()
        back = ct.CTkButton(window, text="Take me back", command=second_window,
                            font=('Times New Roman', 15))
        back.pack(pady=15)

    user_defined()


def second_window():
    for widget in window.winfo_children():
        widget.destroy()

    user_defined_button = ct.CTkButton(window, text="scanning the localhost with ports from 135",
                                       font=('Times New Roman', 15), command=third_window)
    user_defined_button.pack(pady=15)

    single_port_button = ct.CTkButton(
        window, text="scanning the single port of the given target through the user input", command=fourth_window)
    #   font=('Times New Roman', 15), command=fourth_window)
    single_port_button.pack(pady=15)

    multi_port_button = ct.CTkButton(
        window, text=" scanning the list of ports of the given target", command=fifth_window)
    #  font=('Times New Roman', 15), command=fifth_window)
    multi_port_button.pack(pady=15)

    range_port_button = ct.CTkButton(
        window, text="Scan ports of specific range", command=sixth_window)
    #  font=('Times New Roman', 15), command=sixth_window)
    range_port_button.pack(pady=15)

    all_port_button = ct.CTkButton(window, text="scan all the ports of the given target",
                                   command=seventh_window)  # , command=seventh_window)
    all_port_button.pack(pady=15)

    # , background="#072F5F", foreground="white",
    back = ct.CTkButton(window, text="Take me back", command=first)
    # font=('Times New Roman', 15))
    back.pack(pady=15)


def first():
    for widget in window.winfo_children():
        widget.destroy()

    text1 = ct.CTkLabel(window, text="Programming and Algorithms 2",
                        font=('Times New Roman', 46, 'bold'))
    text1.pack(pady=18)

    text1 = ct.CTkLabel(window, text="Port Scanning",
                        font=('Times New Roman', 36, 'bold'))
    text1.pack(pady=10)

    text2 = ct.CTkLabel(window, text="Created by Rohan Joshi",
                        font=('Times New Roman', 19, 'italic'))
    text2.pack(pady=4)

    scan_button = ct.CTkButton(window, text="Scanning Options",
                               font=('Times New Roman', 15), command=second_window)
    scan_button.pack(pady=15)


first()


def singleportinput(ip_entry, port_entry, root):
    '''The function is used for scanning the single port of the given target through the user input.'''

    text_area = ct.CTkTextbox(window)
    text_area.configure(width=369, height=210)
    text_area.pack(pady=46)

    open_number = 0
    close_number = 0

    target = ip_entry.get()
    port = port_entry.get()

    # target = input("Enter the target IP: ")
    # port = int(input("Enter the port number of the target to scan: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, int(port)))
    if result == 0:

        print(f"[+] The port {port} is open on {target}")
    else:
        print(f"\n[!] The port {port} is close on {target}")

    text_area.insert(
        ct.END, f"[-] The port {port} is closed on {target}\n")
    close_number += 1
    text_area.insert(ct.END, "\n")
    text_area.insert(
        ct.END, f"[-] The closed ports are {close_number} and open ports are {open_number}\n")
    text_area.insert(ct.END, "\n")
    text_area.insert(ct.END, "\n")
    text_area.insert(ct.END,
                     f"Scanning the singleport {port} of ip address {target} was successful !!!\n")

    s.close()
    back = ct.CTkButton(window, text="Take me back", command=second_window,
                        font=('Times New Roman', 15))
    back.pack(pady=15)

    root.destroy()


def fourth_window():

    root = ct.CTk()
    root.geometry("200x150")

    for widget in window.winfo_children():
        widget.destroy()
    ip_label = ct.CTkLabel(root, text="IP Address:")
    ip_label.pack()

    ip_entry = ct.CTkEntry(root)
    ip_entry.pack()

    port_label = ct.CTkLabel(root, text="Port:")
    port_label.pack()

    port_entry = ct.CTkEntry(root)
    port_entry.pack()

    submit_button = ct.CTkButton(
        root, text="Submit", command=lambda: singleportinput(ip_entry, port_entry, root))
    submit_button.pack()

    root.mainloop()


def multiportinput(ip_entry, port_entry, root):
    '''The function is used for scanning the list of ports of the given target.'''
    print('\n')

    text_area = ct.CTkTextbox(window)
    text_area.configure(width=369, height=210)
    text_area.pack(pady=46)

    open_number = 0
    close_number = 0

    target = ip_entry.get()
    portt = port_entry.get()

    ports_collection = portt.replace(" ", "")
    ports = ports_collection.split(',')

    for port in ports:

        try:
            int_port = int(port)
        except ValueError:
            text_area.insert(
                "Invalid port entered. Please enter a valid port number.")
            continue

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, int_port))
        if result == 0:
            # print(f"{GREEN}[+] The port {int_port} is open on {target}{RESET}")
            text_area.insert(
                ct.END, f"[-] The port {int_port} is open on {target}\n")
            text_area.insert(ct.END, "\n")
            open_number += 1
        else:
            text_area.insert(
                ct.END, f"[-] The port {int_port} is closed on {target}\n")
            text_area.insert(ct.END, "\n")
            close_number += 1
    # print(f"{RED}[!] The port {int_port} is close on {target}{RESET}")

    text_area.insert(
        ct.END, f"[-] The closed ports are {close_number} and open ports are {open_number}\n")
    text_area.insert(ct.END, "\n")
    text_area.insert(ct.END, "\n")
    text_area.insert(ct.END,
                     f"Scanning the multiports {ports} of ip address {target} was successful !!!\n")

    s.close()
    back = ct.CTkButton(window, text="Take me back", command=second_window,
                        font=('Times New Roman', 15))
    back.pack(pady=15)

    root.destroy()


def fifth_window():

    root = ct.CTk()
    root.geometry("320x190")

    for widget in window.winfo_children():
        widget.destroy()
    ip_label = ct.CTkLabel(root, text="IP Address:")
    ip_label.pack()

    ip_entry = ct.CTkEntry(root)
    ip_entry.pack()

    port_label = ct.CTkLabel(
        root, text="Port: Enter multiple ports seperated by ','")
    port_label.pack()

    port_entry = ct.CTkEntry(root)
    port_entry.pack()

    submit_button = ct.CTkButton(
        root, text="Submit", command=lambda: multiportinput(ip_entry, port_entry, root))
    submit_button.pack()

    root.mainloop()


def rangeportinput(ip_entry, port_entry, root):
    '''The function is used to scan the range of ports of the given target.'''
    print('\n')
    op = 0
    cp = 0
    text_area = ct.CTkTextbox(window)
    text_area.configure(width=369, height=210)
    text_area.pack(pady=46)

    target = ip_entry.get()
    portt = port_entry.get()
    ports = portt.split('-')
    print(ports)

    for i in range(int(ports[0]), int(ports[1])+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, i))
        if result == 0:
            text_area.insert(
                ct.END, f"[-] The port {i} is open on {target}\n")
            text_area.insert(ct.END, "\n")
            op += 1
        else:
            text_area.insert(
                ct.END, f"[-] The port {i} is closed on {target}\n")
            text_area.insert(ct.END, "\n")

            cp += 1

        s.close()

        back = ct.Button(window, text="Take me back", command=second_window, background="#072F5F", foreground="white",
                         font=('Times New Roman', 15))
        back.pack(pady=15)

    text_area.insert(
        ct.END, f"[-] The closed ports are {cp} and open ports are {op}\n")

    text_area.insert(ct.END, "\n")
    text_area.insert(ct.END, "\n")
    text_area.insert(ct.END,
                     f"Scanning the ports of specific range of user choice of ip address {target} was successful !!!\n")
    back = ct.CTkButton(window, text="Take me back", command=second_window,
                        font=('Times New Roman', 15))
    back.pack(pady=15)

    root.destroy()


def sixth_window():

    root = ct.CTk()
    root.geometry("200x150")

    for widget in window.winfo_children():
        widget.destroy()
    ip_label = ct.CTkLabel(root, text="IP Address:")
    ip_label.pack()

    ip_entry = ct.CTkEntry(root)
    ip_entry.pack()

    port_label = ct.CTkLabel(
        root, text="Port: Enter range of ports seperated by '-'")
    port_label.pack()

    port_entry = ct.CTkEntry(root)
    port_entry.pack()

    submit_button = ct.CTkButton(
        root, text="Submit", command=lambda: rangeportinput(ip_entry, port_entry, root))
    submit_button.pack()

    root.mainloop()


def allportscan(ip_entry, root):
    '''The function is used to scan all the ports of the given target.'''
    print('\n')

    op = 0
    cp = 0
    text_area = ct.CTkTextbox(window)
    text_area.configure(width=369, height=210)
    text_area.pack(pady=46)

    target = ip_entry.get()
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, port))
        if result == 0:
            text_area.insert(
                ct.END, f"[-] The port {port} is open on {target}\n")
            text_area.insert(ct.END, "\n")
            # print(f"{GREEN}[+] The port {port} is open on {target}{RESET}")
            op += 1

        else:
            text_area.insert(
                ct.END, f"[-] The port {port} is closed on {target}\n")
            text_area.insert(ct.END, "\n")

            cp += 1
        s.close()
        text_area.insert(ct.END, "\n")
        text_area.insert(ct.END, "\n")
        text_area.insert(ct.END,
                         f"Scanning the ports of specific range of user choice of ip address {target} was successful !!!\n")
        back = ct.CTkButton(window, text="Take me back", command=second_window,
                            font=('Times New Roman', 15))
        back.pack(pady=15)
        root.destroy()


def seventh_window():

    root = ct.CTk()
    root.geometry("200x150")

    for widget in window.winfo_children():
        widget.destroy()
    ip_label = ct.CTkLabel(
        root, text="IP Address: Enter IP address of your choice")
    ip_label.pack()

    ip_entry = ct.CTkEntry(root)
    ip_entry.pack()

    submit_button = ct.CTkButton(
        root, text="Submit", command=lambda: allportscan(ip_entry, root))
    submit_button.pack()

    root.mainloop()


window.mainloop()
