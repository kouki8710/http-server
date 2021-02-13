

class Response:

    def __init__(self):
        self.status_line = {"version":"HTTP/1.1", "status":"200", "text":"OK"}
        self.header = list()
        self.body = "hello,world"
    
    def Create_response(self):
        response = ""
        response += self.status_line["version"] + " "
        response += self.status_line["status"] + " "
        response += self.status_line["text"] + "\r\n"
        response += "\r\n".join(self.header)
        response += "\r\n\r\n"
        response += self.body
        return response.encode("utf-8")

    def Add_statusLine(self, version="HTTP/1.1", status="200", text="OK"):
        self.status_line["version"] = version
        self.status_line["status"] = status
        self.status_line["text"] = text

    def Add_header(self, content):
        self.header.append(content)

    def Add_body(self, content):
        self.body = content
