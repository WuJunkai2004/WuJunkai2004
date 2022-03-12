import re
import requests
import vercel

class handler(vercel.API):
    def vercel(self, url, data, headers):
        config = requests.get('http://wxshi.top:9090/clash/config').text
        for patt in re.findall(r'\s+?#.+?(?=\n)', config):
            config = re.sub(patt, '', config)
        config =re.sub('http://wxshi.top:9090/clash/',
                       'https://wu-junkai.vercel.app/api/',
                       config)

        self.send_code(200)
        self.send_text(config)
