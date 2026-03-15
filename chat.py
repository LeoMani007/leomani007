import socket as s
import threading as thd

# List to keep track of active client connections
clients = []

def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except:
                remove(client)

def handle(client):
    while True:
        try:
            data = client.recv(1024)
            if not data or data == b'quit' or data == b'exit':
                remove(client)
                break
            else:
                broadcast(data, client)
        except:
            remove(client)
            break

def remove(client):
    if client in clients:
        clients.remove(client)
        client.close()

def start_server():
    server = s.socket(s.AF_INET, s.SOCK_STREAM)
    server.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    server.bind(("localhost", 5000))
    server.listen(11)
    print("Server is listening on localhost:5000...")

    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")      
        clients.append(client)
        thread = thd.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == "__main__":
    start_server()