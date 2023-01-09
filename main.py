from datetime import datetime
import requests
import os

API_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.environ.get("HABIT_TRACKER_USERNAME")
TOKEN = os.environ.get("HABIT_TRACKER_TOKEN")
GRAPH_ID = "codinghabit2022"

graph_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs"
pixel_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

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
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many hours did you use to code today? "),
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

# # add a pixel
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# # update a pixel
# response = requests.put(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)


