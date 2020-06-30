from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def client_communication(client):
    run = True
    while run:
        msg = client.recv()



def wait_for_connection(SERVER):
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            Thread(target=client_communication, args=(client,)).start()
        accept Exception as e:
        print("[FAILURE]", e)
        run = Falsel

HOST = 'localhost'
PORT = 5500
BUFSIZ = 512
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection, (SERVER))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
