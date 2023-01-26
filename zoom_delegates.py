#!/bin/env python3
# Zoom delegate adder v0.2
# Author: Kyle Copley

import requests
import json
import sys
import os
from assistants import assistants

bearerToken = os.environ.get('zoomBearer')

newUser = sys.argv[1]
endpoint = f"https://api.zoom.us/v2/users/{newUser}/assistants"
headers = {
   'Authorization': f'Bearer {bearerToken}',
   'Content-Type': 'application/json'
}

data = json.dumps(assistants)
res = requests.post(endpoint, data=data, headers=headers)
    
if res.status_code == 201:
    print(f"Successfully added Zoom delegates to {newUser}")
else:
    print(f"Uh oh, the response was \"{res.json()['message']} with status code {res.json()['code']}\"")