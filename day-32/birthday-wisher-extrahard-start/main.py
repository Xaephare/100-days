import pandas as pd
import random
import smtplib
import datetime as dt


MY_EMAIL = 'youremailhere@gmail.com'
PASSWORD = 'yourpassword'

LETTER_PATHS = ('letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt')

# ---------------------------------------------------------------------------------------
now = dt.datetime.now()
current_day = now.day
current_month = now.month

df = pd.read_csv('birthdays.csv')
birthday_dict = df.to_dict('records')

# -------------------------------------------  --------------------------------------------

todays_birthdays = []
for person in birthday_dict:
    if person['month'] == current_month and person['day'] == current_day:
        todays_birthdays.append({'name':person['name'], 'email':person['email']})


# ------------------------------------------ SEND PERSONALISED EMAILS ---------------------------------------------

for birthday in todays_birthdays:
    with open(random.choice(LETTER_PATHS)) as letter:
        letter_contents = letter.read()
        personalised_letter = letter_contents.replace('[NAME]', birthday['name'])

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday['email'],
            msg=f"Subject:Happy Birthday!\n\n{personalised_letter}"
        )
