# Monday Motivation Mailer
A python script that sends a motivational quote every Monday. It checks if the current day is Monday and, if so, selects a random quote from a quotes.txt file and sends it using the smtplib library.

Tools Used

This script uses the following tools:

Python - a high-level programming language used for general-purpose programming.
smtplib - a Python library used to send email messages using the Simple Mail Transfer Protocol (SMTP).
datetime - a Python library used to manipulate dates and times. In this script, it is used to check the current day of the week.

Usage

Before running the script, make sure to replace the following variables with your own values:

  MY_EMAIL: your email address
  RECEIVER_EMAIL: the email address of the person who will receive the email
  GMAIL_APP_PASSWORD: the app password generated from your Gmail account
  GMAIL_SMTP: the SMTP server of your email provider
  To run the script, simply execute the python main.py command in your terminal.
  In order to send emails using this script, you will need to generate an app password from your email provider (e.g. Google, Yahoo, Outlook) to use in place of your regular account password. This is done for security reasons.

Note

For the script to send an email on every Monday, it needs to be hosted on a cloud platform such as PythonAnywhere or Heroku.

Contributions

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

