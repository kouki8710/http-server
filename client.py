import socket

ip = socket.gethostbyname(socket.gethostname())
print(ip)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

msg = b""
while True:
    read_msg = s.recv(8)
    if len(read_msg)==0:
        break
    msg += read_msg
# print(msg.decode("utf-8"))