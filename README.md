This repository contains two example methods of uploading data to a google sheet from an application. This method allows anyone with the script to freely upload data, it is not intended for uploading to private individuals google drives and validating who is sending the requests.

----
Method 1 - Google Forms - upload_google_form.py:
You can create a google sheet linked to a google form, and then an application can upload data by sending form requests.
This method requires zero dev setup/interaction with the Google API

Steps:
On any google account:
1. Create a new sheet
2. Go to Tools > Create a New Form
3. Setup the form with fields for all the data you want, I would suggest using all short answer or paragraph for ease, although you don't need to
4. Click Share, and copy the link out
5. Paste the link into the form_url variable at the top of upload_google_form.py
6. Modify the data_to_send list to have all the data you want uploaded
7. Run the script, and the Google sheet should update

This method works by simply sending a post request to the public google forum with the data already filled out.
Ensure the forum is publicly accessible to anyone with the link, and that it does not required being signed into a google account
    These should be default when making a form
    
----

Method 2 - pygsheets - edit_google_sheets.py
This method uses a python library that allows modifying a google sheet on a Service Account using a key file by using Googles API.'

Steps:
Installing:
Have python installed already
In a command prompt, enter python -m pip install https://github.com/nithinmurali/pygsheets/archive/staging.zip

Setting up a google account:
First, I would recommend using a team account instead of your own private account

You can follow along with https://pygsheets.readthedocs.io/en/latest/authorization.html but its a bit dated
so not everything is in the exact same places
    Use the service account method, not the oauth

1. Go to https://console.developers.google.com/
2. In the top left, there is a project selection dropdown box, click it and then click NEW PROJECT
    2b. Set whatever name you want, go ahead and click create
3. Click the project selection box again and this time select the project you just created so it is active
4. On the far left, select "Enabled APIs & services"
5. Click "+ ENABLE APIS AND SERVICES" near the top middle of the screen
6. In the search box, type "sheet", select Google Sheets API, and click Enabled
7. Repeat the enable service process but for Google Drive API instead
8. On the far left select "Credentials"
9. Near top middle click "+ CREATE CREDENTIALS" and select Service account
    9b. Give it a name and then just click "Done"
10. Select that service on the Credentials page, it will show up as an email at the bottom of the page under Service Accounts
11. Go to the KEYS tab of the new window
12. Click ADD KEY > Create new key > JSON > CREATE
    12b. This will download a JSON file, make sure you save it off as it will need to be in the same directory as the example test_sheets.py script. Probably rename it too.
13. You are all done, just have the test_sheets.py script provide a path to that downloaded file and set USER_EMAIL in the script to your email

Documentation:
https://github.com/nithinmurali/pygsheets
https://pygsheets.readthedocs.io/en/latest/reference.html


