import requests

API_ENDPOINT = "https://pixe.la/v1/users"

parameters = {
    "token" : "AtomicHabits",
    "username" : "Thulani",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"

}

response = requests.post(API_ENDPOINT, params=parameters)