from datetime import datetime as dt
from smtplib import SMTP
import random 
now = dt.now() # checking the current date and time

# checking if the day is monday

if now.weekday() == 1:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
        MY_EMAIL = "lesliejoe2k2@gmail.com"
        RECIEVER_EMAIL = "larteyleslie@yahoo.com"
        GMAIL_APP_PASSWORD = "lgswruirjhbtoejj"
        GMAIL_SMPT = "smtp.gmail.com"
        
        with SMTP(GMAIL_SMPT, port=587) as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=GMAIL_APP_PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIEVER_EMAIL, msg=f"Subject: Monday Motivation Mail\n\n {quote}")
        
else:
    print("Yessir!")
print(quote)