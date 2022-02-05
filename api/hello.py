import vercel

class handler(vercel.API):
    def vercel(self, url, data, headers):
        self.send_code(200)
        self.send_text('hello world\n\nurl = ' + url + '\n\ndata = ' + str(data) + '\n\nheaders = ' + str(headers))