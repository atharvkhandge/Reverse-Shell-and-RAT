# Simple Python Reverse Shell

This project demonstrates a basic remote access toolset using Python's `socket` and `os` libraries. It includes an **Attacker Console** to send commands and a **Victim Shell** to execute them and return the output.

### Components
* **Attacker_console.py**: Sets up a listening server on port 9999 to manage the remote connection.
* **Victim_shell.py**: Connects to the attacker's IP and executes received terminal commands.
* **File Transfer**: Includes a `download` feature that uses Base64 encoding to exfiltrate files from the victim.

> **Warning**: This code is for educational purposes and authorized security testing only.
