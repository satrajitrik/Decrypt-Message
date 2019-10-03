import socket
import base64
import sys

HOST = 'crime.cse545.rev.fish'  # The server's hostname or IP address
PORT = 30925                    # The port used by the server
handle = "smaitra"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT)) 
data = sock.recv(1024)
sock.send("{}\n".format(handle).encode("utf-8"))
data = sock.recv(1024)

try:
    string = ""
    for i in range(70):
        min_length = sys.maxsize
        chosen_char = ""
        for ch in range(32, 128):
            sock.send(("{}{}\n".format(string, chr(ch))).encode("utf-8"))
            reply = sock.recv(131072).decode("utf-8")
            start_str = "message:\n"
            end_str = "\n\nIf"

            start = reply.find(start_str) + len(start_str)
            end = reply.find(end_str)

            encrypted_message = reply[start:end]

            if min_length > len(base64.b64decode(encrypted_message)):
                min_length = len(base64.b64decode(encrypted_message))
                chosen_char = chr(ch)

            if not reply:
                break
        string += chosen_char
        print(string)
        print("Iteration: ", i)

except KeyboardInterrupt:
    print("bye")

print("End.... ")
