import sys
import jwt
import http.client
import datetime
import json

seperate = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

# Go to 
# Then get API Key, API Secret and insert below
api_key = ''
api_sec = ''


payload = {
'iss':api_key,
'exp': datetime.datetime.now() + datetime.timedelta(hours=2)
}

jwt_encoded = str(jwt.encode(payload, api_sec), 'utf-8')

conn = http.client.HTTPSConnection("api.zoom.us")
headers = {
'authorization': "Bearer %s" % jwt_encoded,
'content-type': "application/json"
}

conn.request("GET", "/v2/users/YOUREMAIL/meetings", headers=headers)
res = conn.getresponse()
response_string = res.read().decode('utf-8')
response_obj = json.loads(response_string)
print(response_obj)