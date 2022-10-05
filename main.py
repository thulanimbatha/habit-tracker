from urllib import request
import requests

API_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "thulani"
TOKEN = "AtomicHabits"
GRAPH_ID = "codinghabit2022"

graph_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs"
pixel_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

user_parameters = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"

}

graph_parameters = {
    "id"    : GRAPH_ID,
    "name"  : "Coding Graph",
    "unit"  : "hrs",
    "type"  : "float",
    "color" : "ichou",
}

pixel_params = {
    "date" : "20221005",
    "quantity" : "2.5",
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

# # create user account
# response = requests.post(url=API_ENDPOINT, json=parameters)
# print(response.text)

# # create a graph definition
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

# add a pixel
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
