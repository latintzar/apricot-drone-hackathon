#!/bin/bash
sudo ssh -o ConnectTimeout=15 root@5.161.178.146 'python3 - <<"PY"
import json,urllib.request,urllib.parse
t=json.load(open("/home/founder/.hermes/google_token.json"))
d=urllib.parse.urlencode({"client_id":t["client_id"],"client_secret":t["client_secret"],"refresh_token":t["refresh_token"],"grant_type":"refresh_token"}).encode()
print(json.load(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token",data=d)))["access_token"])
PY'
