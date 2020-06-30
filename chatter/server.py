from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person


# GLOBAL CONSTANTS
HOST = 'localhost'
PORT = 5500
BUFSIZ = 512
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10

# GLOBAL VARIABLES
persons = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)  # set up server

def broadcast(msg, name):
    """
    Send new messages to all clients
    :param msg: bytes["utf8"]
    :param name: str
    :return:
    """
    for person in persons:
        client = person.client
        client.send(bytes(name + ": ", "utf8") + msg)


def client_communication(person):
    """
    THREAD TO HANDLE ALL MESSAGES FROM CLIENT
    ;param person: Person
    ;return: None
    """
    run = True
    client = person.client
    name = person.name
    # addr = person.addr

    name = client.recv(BUFSIZ).decode("utf8")
    msg = f"{name} has joined the chat!"
    broadcast(msg) # Broadcast welcome message
    while run:
        msg = person.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(f"{name} has left the chat.", "")
            person.close()
            persons.remove(person)
        else:
            client.send(msg, name)




def wait_for_connection():
    """
    WAIT FOR CONNECTION FROM NEW CLIENTS, STRT NEW THREAD ONCE CONNECTED
    :param SERVER: SOCKET
    :return: NONE
    """
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons.append(person)
            print(f"[CONNECTION]: {addr} connected to server at {time.time()}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[FAILURE]", e)
            run = False
    print("SERVER CRASHED!!!!")


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS)
    print("[STARTED] Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
