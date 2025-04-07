import datetime as dt
import pandas as pd
from random import randint

PLACEHOLDER = "[NAME]"
updated_letter = "Nobody's birthday"

data_frame = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data_frame.iterrows()}

today = (dt.datetime.now().month, dt.datetime.now().day)

if today in birthdays_dict: 
    birthday_person = birthdays_dict[today]  
    with open(f"./letter_templates/letter_{randint(1, 3)}.txt") as letter_data:
        letter = letter_data.read()
        updated_letter = letter.replace(PLACEHOLDER, birthday_person["name"])

#Send mail here:        
print(updated_letter)         

       
    





