import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = '127.0.0.1'
PORT = 9090


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring(
            "Nickname", "Please choose a nickname", parent=msg)

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="#83838B")
        self.win.title(f"Chat of {self.nickname}")
        self.win.resizable(0, 0)

        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="#83838B")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(
            self.win, text="Message:", bg="#83838B")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3, bg="#BDBDB7")
        self.input_area.pack(padx=20, pady=5)

        self.button_frame = tkinter.Frame(self.win, bg="#83838B")
        self.button_frame.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(
            self.button_frame, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.grid(row=0, column=0, padx=20, pady=5)

        self.decrypt_button = tkinter.Button(
            self.button_frame, text="Decrypt", command=self.decrypt_message)
        self.decrypt_button.config(font=("Arial", 12))
        self.decrypt_button.grid(row=0, column=1, padx=20, pady=5)

        self.gui_done = True
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()

    def rot13_encode(self, text):
        result = ""
        for char in text:
            ascii_value = ord(char)
            if 65 <= ascii_value <= 90:
                result += chr((ascii_value - 65 + 13) % 26 + 65)
            elif 97 <= ascii_value <= 122:
                result += chr((ascii_value - 97 + 13) % 26 + 97)
            else:
                result += char
        return result
        print(result)

    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        message = self.rot13_encode(message)
        print(message)
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def rot13_decode(self, text):

        result = ""
        for char in text:
            ascii_value = ord(char)
            if 65 <= ascii_value <= 90:
                result += chr((ascii_value - 78) % 26 + 65)
            elif 97 <= ascii_value <= 122:
                result += chr((ascii_value - 110) % 26 + 97)
            else:
                result += char
        return result

    def decrypt_message(self):
        texts = self.text_area.get(1.0, tkinter.END)
        decrypt_message = self.rot13_decode(texts)
        self.text_area.config(state='normal', bg="#BDBDB7")
        self.text_area.delete(1.0, tkinter.END)
        self.text_area.insert('end', decrypt_message)
        self.text_area.yview('end')
        self.text_area.config(state='disabled', bg="#BDBDB7")

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')

                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal', bg="#BDBDB7")
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled', bg="#BDBDB7")
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.sock.close()
                break


client = Client(HOST, PORT)
