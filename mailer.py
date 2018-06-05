import smtplib as smtp
from email.mime.text import MIMEText
stg = open('pwd.txt', 'r') # Change the password to match yours in the pwd.txt file
pwd = str(stg.read())
my_email = 'your email'
sending = "spam email"

def send(sending, my_email, pwd):
    server = smtp.SMTP('smtp-mail.outlook.com', 587) # Change this to match your email provider
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(my_email, pwd)
    msg = MIMEText("Message")
    msg['From'] = my_email
    msg['To'] = sending
    msg['Subject'] = "Python email"
    text = msg.as_string()
    server.sendmail(my_email, sending, text)
    server.quit()
    print('Email sent successfully')
while True:
    send(sending, my_email, pwd)
