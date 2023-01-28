#!/bin/env python3
# Zoom delegate adder v0.2
# Author: Kyle Copley

import requests
import json
import os
import argparse

bearerToken = os.environ.get('zoomBearer')

parser = argparse.ArgumentParser(
                    prog = 'Zoom Delegate Adder',
                    description = 'Adds assistants to a zoom users account for delegate access')

parser.add_argument( "-t", "--target", dest='targetUser', type=str, help="The user who you want to add an assistant to")
parser.add_argument("-a", "--assistant", dest='assistantUser', type=str, help="The user who will be added as an assistant to the target User")

args = parser.parse_args()

assistants =  {
  "assistants":[
        {
          "email": args.assistantUser
        }
    ]
}

newUser = args.targetUser

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