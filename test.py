"""
http://docs.python-requests.org/en/v1.0.0/user/quickstart/
"""

import requests

server_url = 'http://127.0.0.1:5000/'

"""
Get the access token so we can access the secured endpoint
"""
# The url for authorization
auth_url = server_url + "auth"
# The user we want to authenticate
payload = {"username": "joe", "password": "pass"}
# Make a post request to the server
response = requests.post(auth_url, json=payload)
# Get the json body of response
json_body = response.json()
# Retrieve the token from the json body
token = json_body["access_token"]

"""
Make a call to the endpoint with our token
"""
# The url of the endpoint
endpoint_url = server_url + "protected"
# The body we need to send in the get request
body = {"Authorization": "JWT " + token}
# Make a request to the server
response = requests.get(endpoint_url, headers=body)
# Get the text response
print(response.text)