try:
    import requests
except ImportError:
    import urllib.request as request

import ssl
context = ssl._create_unverified_context()

try:
    import vercel
except:
    tag = 'date'
else:
    tag = ''

def get(tag):
    url = 'https://wu-junkai.vercel.app/api/'+tag
    try:
        # https://blog.csdn.net/chitaozi/article/details/106381353
        return request.urlopen(url,context=context).read().decode('utf-8')
    except BaseException as e:
        return 'Net Error :\n' + ' '.join(map(str,list(e.args)))

class handler(vercel.API):
    def vercel(self, url, data, headers):
        self.send_code(200)

        global tag

        if(not tag):
            try:
                tag = url.split('#')[1]
            except IndexError:
                tag = 'date'

        self.send_text('get https://wu-junkai.vercel.app/api/'+tag+'\n'+
                       '\n'+
                       'result =====\n'+
                       '\n'+
                       get(tag)
                       )

