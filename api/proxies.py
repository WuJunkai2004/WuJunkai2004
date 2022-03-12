import re
import requests
import urllib.parse
import vercel

class handler(vercel.API):
    def vercel(self, url, data, headers):
        for item in data.keys():
            print(urllib.parse.unquote(data[item]))
            data[item] = urllib.parse.unquote(data[item])
            print(data)
        url = 'http://wxshi.top:9090/clash/proxies?' + urllib.parse.urlencode(data)
        config = requests.get(url).text
        config = re.sub(r'"name":".+?"',
                        '"name":""',
                        config)
        self.send_code(200)
        self.send_text(config)
