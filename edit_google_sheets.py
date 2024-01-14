import pygsheets
import pathlib
import numpy as np
import json


#Note: Pygsheets documentation isn't the best, so might have to snoop in the source
#to figure out valid values for some of the parameters. The search bar works pretty good though
#so its not too bad.
valid_roles = ['organizer', 'owner', 'writer', 'commenter', 'reader'] #Found from pygsheets.drive

#Get path to key folder using a path relative to this script (__FILE__)
my_parent_folder = pathlib.Path(__file__).parent
key_path = (my_parent_folder / "key.json") #This means key.json is in the same directory as this script, this is the JSON downloaded from the website

USER_EMAIL = "example@gmail.com" #PUT YOUR EMAIL HERE 

gc = pygsheets.authorize(service_account_file=key_path)

existing_sheets = gc.spreadsheet_titles()
sheet_name = 'my test sheet'
if sheet_name not in existing_sheets:
    print("Creating sheet:", sheet_name)
    sh = gc.create(sheet_name)
    #Make sure to share the sheet with the google account you want to actually be able to view and edit it, 
    #otherwise it will only be accessible via scripts
    print("Sharing new sheet with:", USER_EMAIL)
    sh.share(USER_EMAIL, role="writer")
#Alternatively, you could create a sheet, and then share it with the email created by the service account you made
#and then just directly access it without having to create it.
with open(key_path, 'r') as fp:
    client_email = json.load(fp)["client_email"]
    print("Email to share sheets with so the script can access them:", client_email)

#Following is just example code from PYGSHEETS

print("Updating values in existing sheet")
# Open spreadsheet and then worksheet
sh = gc.open(sheet_name)
wks = sh.sheet1

# Update a cell with value (just to let him know values is updated ;) )
wks.update_value('A1', "Hey yank this numpy array")

# update the sheet with array
my_nparray = np.random.randint(10, size=(3, 4))
wks.update_values('A2', my_nparray.tolist())
print("Done")