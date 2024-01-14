"""
Uses google forms as an intermediary to uploading data to a google sheet without having to set up any keys
"""

import requests
#If this isn't detected, do python -m pip install requests

#This should be the share link, you can shorten it if you want, it doesn't matter
form_url = "https://forms.gle/nUNqkgmjrfNsGEFZ8"
data_to_send = ["Jim", "A", "Yes"] #This is the data that will be submitted, ensure its in the order the questions are asked

#get response of form so can parse out the FORM_ID and the entry ids for uploading data
form_response = requests.get(form_url)

#Pull out the full form path. This way, if the provided URL is shortened or a redirect, it will still get the correct URL
path_start = form_response.text.find("docs-seu")
path_start = form_response.text.find('https', path_start)
path_end = form_response.text.find('"', path_start)
path = form_response.text[path_start:path_end]

#Pull the FORM ID out of the path
id_start = path.find("forms/d/e/") + len("forms/d/e/")
id_end = path[id_start:].find("/") + id_start
form_id = path[id_start:id_end]
print("Form ID:", form_id)

#Discover keys that can be set
data_start = form_response.text.find("var FB_PUBLIC_LOAD_DATA_")
data_start = form_response.text.find("[", data_start)
data_end = form_response.text.find(";", data_start)
data_variable = form_response.text[data_start:data_end]
data_variable = data_variable.replace("null", "None") #Convert to python formatted object instead of JSON
data = eval(data_variable) #Load the string in as the list it is

#Print all the question Name and its associated entry ID, and store the entry ids.
entry_params = []
data_order = []
for param_info in data[1][1]:
    text = param_info[1]
    entry_id = param_info[4][0][0]
    print(f"{text}={entry_id}")
    data_order.append(text)
    entry_params.append(f"entry.{entry_id}")

#Build the URL to send responses too
form_response_url = f"https://docs.google.com/forms/d/e/{form_id}/formResponse"

#Note the order must match the order they are in the sheet
print("Data must be in order:", data_order)


#Format data to send out
data_to_send = dict(zip(entry_params, data_to_send))
print("Sending response:", data_to_send)

# #Make sure to use a post request and data. This will ensure that the
# #data is put in the body of the post request instead of the query string
# #of the URL. If you put the data in the query string, it is possible that a
# #sufficently large query string would be considered too large and rejected by the server
response = requests.post(url=form_response_url, data=data_to_send)
print(f"{response.status_code=}")

#Suggestions:
#To make this as easy to use as possible, making everything a text input in the
#forum and then just formatting the data in your program when sending it would be easiest.
#You can do multiple choice, checkboxes, etc... whatever you want, just ensure the data you want
#to send matches the options in the sheet