import json
import time

import requests
import vercel


class handler(vercel.API):
    def vercel(self, url, data, headers):
        if(not data):
            self.send_code(200)
            self.send_text(json.dumps({"upload":"fail","error":"Need data"}))
            return
        url = "https://data.mongodb-api.com/app/data-uqbpx/endpoint/data/beta/action/insertOne"
        payload = json.dumps({
            "collection": "student",
            "database": "class7",
            "dataSource": "Cluster0",
            "document": data
        })
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'eOYzarNsIRJ7h9n0JEWGqa59yMKN6i8u1temFAmjRDz3qLzDIfAHRFX8A8ESPwnx'
        }
        for i in range(5):
            try:
                response = requests.post(url, headers=headers, data=payload)
            except:
                time.sleep(0.05)
            else:
                self.send_code(200)
                self.send_text(response.text)
                break
                return
        else:
            self.send_code(200)
            self.send_text(json.dumps({"upload":"fail","error":"Net Error"}))
