import json
import requests

seperate = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

# 1 - Login
url = 'https://bootcampspot.com/api/instructor/v1/login'
headers = {'Content-Type': "application/javascript"}
data = {"email": "user@domain.com", "password": ""}
login = requests.post(url, json=data, headers=headers)

x = json.loads(login.text)
print(x)
authToken = x["authenticationInfo"]["authToken"]

print (seperate)
print ("Login Response")
print (seperate)
print (login.text)

# ======================================================================

# 2 - Get Enrollment ID
url = 'https://bootcampspot.com/api/instructor/v1/me'
headers = {'Content-Type': "application/json"}
data = x["authenticationInfo"]["authToken"]
me = requests.get(url, params={"authToken":data}, headers=headers)

x = json.loads(me.text)
eid = x['Enrollments'][0]['id']
print (seperate)
print ("Me Response")
print (seperate)
# print(x['Enrollments'][0]['id'])
# print (me.text)

# ======================================================================

# 3 - Get Sessions
url = 'https://bootcampspot.com/api/instructor/v1/sessions'
# headers = {'Content-Type': "application/json"}
# data = {"enrollmentId": x["Enrollments"][0]["id"]}
# resp = requests.post(url, json=data, headers=headers)
headers = {'Content-Type': "application/json", "authToken":authToken}
data = eid
sesh = requests.get(url, params={"enrollmentId":data}, headers=headers)

x = json.loads(sesh.text)
print ("Session Response")
print (seperate)
print (sesh.text)

# ======================================================================

# # 4 - Session Details
# url = 'https://bootcampspot.com/api/instructor/v1/sessionsDetail'
# headers = {'Content-Type': "application/javascript"}
# data = {"email": "user@domain.com", "password": ""}
# seshDeets = requests.post(url, json=data, headers=headers)

# x = json.loads(seshDeets.text)
# print ("Login Response")
print (seperate)
# print (seshDeets.text)
# print (seperate)