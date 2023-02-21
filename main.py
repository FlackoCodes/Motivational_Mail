from datetime import datetime as dt
from smtplib import SMTP
import random

# Constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_mail"
RECIPIENT_EMAIL = "recepient_mail"
APP_PASSWORD = "your smtplib app password"
SUBJECT = "Monday Motivation Mail"
QUOTES_FILE = "quotes.txt"

def send_email(sender_email, recipient_email, subject, message):
    """Send an email with the given subject and message from the given sender to the given recipient on mondays."""
    with SMTP(SMTP_SERVER, port=SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=APP_PASSWORD)
        connection.sendmail(from_addr=sender_email, to_addrs=recipient_email, msg=f"Subject: {subject}\n\n{message}")

now = dt.now() # checking the current date and time

# checking if the day is monday
if now.weekday() == 0:
    with open(QUOTES_FILE) as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
        send_email(SENDER_EMAIL, RECIPIENT_EMAIL, SUBJECT, quote)
