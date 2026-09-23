import requests 
#1. Dispatch a Get  request to Github API
response = requests.get("https://api.github.com")
#2. Inspect the response neumerical statuscode
print(response.status_code)
#3. Extract and response parse JSON payload
print(response.json()) #Parsed response   