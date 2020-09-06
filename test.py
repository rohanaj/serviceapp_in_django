import requests
#requestobj =
'''json = {
    "user": 1,

        "requestdesc": "Good",
        "city": "Indore",
        "state": 1,
        "pincode": "452001",
        "countrycode": "91",
        "phone_number": "9303745814",
             "status":1,
"requesttype": [1,2]
        }
json2 = {"status":3,"remarks":"work done","updated_by":3}
headers = {"Authorization":"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk3OTMyMzQ5LCJqdGkiOiJhNGQzNDA1Mjk1Nzg0OTEzOWNmYzIxODc0YjJjNzk0MiIsInVzZXJfaWQiOjN9.FVYGb3Xor8XqY1I7FYqZ4KOJNAZS5jw67-4YljbZkbQ"}
url = "http://127.0.0.1:8000/updaterequest/1"
r = requests.put(url=url,headers=headers,json=json2)
r = r.json()
print(r)
'''
headers = {"Authorization":"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5ODA5MTIyNSwianRpIjoiNmNkODk0NDgyNGNjNDQ0YmE4YjhjNzZkYWJlOTI3OTUiLCJ1c2VyX2lkIjozfQ.OQ9qPsNi1OAnaPu6MeYNC6owWff-KttRL7I6c7wdrus"}
json = {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5ODA5MTIyNSwianRpIjoiNmNkODk0NDgyNGNjNDQ0YmE4YjhjNzZkYWJlOTI3OTUiLCJ1c2VyX2lkIjozfQ.OQ9qPsNi1OAnaPu6MeYNC6owWff-KttRL7I6c7wdrus"}
url = "http://127.0.0.1:8000/api/auth/jwt/refresh"
r = requests.post(url=url,json=json)
print(r.json())
