import vercel

class handler(vercel.API):
    def vercel(self, url, data, headers):
        self.send_code(200)
        self.send_text('url :\n' + 
                       url + '\n'+ 
                       '\n' +
                       '==========\n'+
                       'data :\n' + 
                       str(data) + '\n' +
                       '\n' +
                       '==========\n'+
                       'headers :\n' + 
                       str(headers)
                      )
