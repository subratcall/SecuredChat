#!/usr/bin/env python3
"""chat client """ 
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import simpledialog


def receive():
    """Receiving massages"""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except :  
            break


def send(event=None): 
    """sending messages."""
    msg = my_msg.get()
    my_msg.set("")  
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """When the window is closed."""
    my_msg.set("{quit}")
    send()

#Some gui defines
top = tkinter.Tk()
top.configure(background='black')
top.title("Chatter")
top.geometry("900x700")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame) 

msg_list = tkinter.Listbox(messages_frame, height=20, width=75, yscrollcommand=scrollbar.set , font=("Monospace Regular", 17 ), fg = '#33cc33', bg='black')
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg  , width = 35 , font=("Monospace Regular", 16 ))
entry_field.bind("<Return>", send)
entry_field.pack()
top.protocol("WM_DELETE_WINDOW", on_closing)
#Connection defines
HOST = '127.0.0.1'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

#define the client socket and options 
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop() 