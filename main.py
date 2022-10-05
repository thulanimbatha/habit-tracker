import requests

API_ENDPOINT = "https://pixe.la/v1/users"

parameters = {
    "token" : "AtomicHabits",
    "username" : "thulani",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"

}

response = requests.post(url=API_ENDPOINT, json=parameters)
print(response.text)