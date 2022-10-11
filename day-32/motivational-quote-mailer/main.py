import smtplib
import datetime as dt
import random

with open('quotes.txt') as quotes:
    quote_list = quotes.readlines()

now = dt.datetime.now()
day_of_week = now.weekday()

MY_EMAIL = ''
PASSWORD = ''

if day_of_week == 1:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='',
            msg=f"Subject:Motivational tuesday quote\n\n{random.choice(quote_list)}"
        )
