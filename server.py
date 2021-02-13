import socket, os
from module.Request import Request
from module.Response import Response

HOST = "localhost"
PORT = 1240
ROOT_PATH = os.getcwd()

# socket初期化
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    clientsocket, address = s.accept()

    msg = clientsocket.recv(4096).decode("utf-8")
    # http通信始めか判定
    if (msg==""):
        clientsocket.close()
        continue
    
    request = Request()
    request.Parse_request(msg)

    print(f"Connection from {address} has been established!")
    path = ROOT_PATH + request.status_line["path"]
    print(path)

    response = Response()
    # ファイルが存在するか
    if not os.path.exists(path):
        response.Add_statusLine(status="404", text="Not Found")
        clientsocket.send(response.Create_response())
        clientsocket.close()
        continue
    
    f = open(path)
    response.Add_header(request.Get_contentType())
    response.Add_body(f.read())
    clientsocket.send(response.Create_response())

    #終了
    f.close()
    clientsocket.close()
    print("close")