import requests
from datetime import *
import os

    #TODO create the user account

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.environ["TOKEN"]
USERNAME = "dcordero"
GRAPH_ID = "graph123cycling"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

    #TODO Create the graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Miles",
    "type": "float",
    "color": "sora",
}
#
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = date.today()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "30.0",
}

# add_pixel = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(today.strftime("%Y%m%d"))
# print(add_pixel.text)
# print(add_pixel.json())

update_date = "20210422"
pixel_update_config = {
    "date": update_date,
    "quantity": "4.0",
}
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_date}"

# update_pixel = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(update_pixel.text)

delete_pixel = requests.delete(url=pixel_update_endpoint, headers=headers)
print(delete_pixel.text)