import vercel

class handler(vercel.API):
    def vercel(self, url, data, headers):
        try:
            with open('stu.txt','w+') as fin:
                fin.write('aaaa')
        except BaseException:
            self.send_code(200)
            self.send_text('write fail')
        else:
            self.send_code(200)
            self.send_text('write success')