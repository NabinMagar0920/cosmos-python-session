import requests

loc = input("enter your location: ")
date = input("enter the date (YYYY-MM-DD): ")
print("simple python weather application")
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{loc}/{date}"

try:
    response = requests.get(url, params={'key': '2QC2WZDVJRS57AJ5RMXPJ7MPA'})
    data = response.json()
    print(data['description'])
except:
    print("invalid error")
    


