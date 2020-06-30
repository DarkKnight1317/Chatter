from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# GLOBAL CONSTANTS
HOST = "local host"
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 512

# GLOBAL VARIABLES
messages = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def receive_messages(messages):
    """
    receive messages from server
    :param messages: str
    :return: None
    """
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("uft8")
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEPTION],", e)
            break


def send_message(msg):
    """
    send messages to server
    :param msg: str
    :return: None
    """
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()


receive_thread = Thread(target=receive)
receive_thread.start()

send_message("Bishal")
send_message("Hello")