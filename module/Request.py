

class Request:

    def __init__(self):
        self.status_line = {"method":"", "path":"", "version":""}
        self.header = list()

    def Parse_request(self, msg):
        if (msg==""):
            return
        status_line = msg.split("\r\n")[0].split(" ")
        self.status_line["method"] = status_line[0]
        self.status_line["path"] = status_line[1] if status_line[1]!="/" else "/file/index.html"
        self.status_line["version"] = status_line[2]
        for line in msg.split("\r\n")[1:]:
            self.header.append(line)

    def Get_contentType(self):
        if self.status_line["path"]=="":
            raise Exception("例外が発生しました")

        path = self.status_line["path"]
        extension = path.split("/")[-1].split(".")[-1]
        if extension=="js":
            extension = "javascript"
        contentType = "Content-Type: text/" + extension
        return contentType



