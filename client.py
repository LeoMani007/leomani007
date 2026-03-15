import socket as s
import threading as thd

HOST = 'localhost'
PORT = int(input("Enter port number: "))

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(f"\n{message}")
                print("> ", end="") 
            else:
                print("\nConnection closed by server.")
                client.close()
                break
        except:
            print("\nAn error occurred while receiving.")
            client.close()
            break

def send_messages():
    while True:
        try:
            msg = input("> ")
            if msg.lower() in ['quit', 'exit']:
                client.send(msg.encode())
                client.close()
                break
            client.send(msg.encode())
        except EOFError:
            break

receive_thread = thd.Thread(target=receive_messages)
receive_thread.daemon = True 
receive_thread.start()

send_messages()