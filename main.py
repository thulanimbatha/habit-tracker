from urllib import request
import requests

API_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "thulani"
TOKEN = "AtomicHabits"

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

user_parameters = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"

}

graph_parameters = {
    "id"    : "codinghabit2022",
    "name"  : "Coding Graph",
    "unit"  : "hrs",
    "type"  : "float",
    "color" : "ichou",
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

# # create user account
# response = requests.post(url=API_ENDPOINT, json=parameters)
# print(response.text)

# create a graph definition
response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
print(response.text)