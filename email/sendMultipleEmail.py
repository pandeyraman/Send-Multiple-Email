"""
    Python code to send same email from you gmail account to the multiple recipient
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender_email = "senderemal@domain.com"
sender_password = "mypassword"
list_of_reciever = ["xxxxx@gmail.com", "yyyyy@gmail.com","zzzz@gmail.com"]

for i in range(len(list_of_reciever)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email,sender_password)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = list_of_reciever[i]
    msg['Subject'] = "Subject of the Mail"
    body = "Message_you_need_to_send"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    s.sendmail(sender_email, list_of_reciever[i], text)
    s.quit()