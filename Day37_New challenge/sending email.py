#!/usr/bin/python

import smtplib
import ssl
from getpass import getpass

server_name = 'smtp.gmail.com'
SSL_port = 465
message = "Test message as learning SMTP server"
context = ssl.create_default_context()
'''
server_connection = smtplib.SMTP_SSL(server_name, 465, context=context)
passwd = getpass("Enter your password")
server_connection.login("learningpython.2022.anjali@gmail.com", passwd)
server_connection.sendmail("learningpython.2022.anjali@gmail.com", "soumya.cric4@gmail.com", message)
server_connection.close()'''

with smtplib.SMTP_SSL(server_name, 465, context=context) as server:
   passwd = getpass("Enter your password")
   server.login("learningpython.2022.anjali@gmail.com", passwd)
   server.sendmail("learningpython.2022.anjali@gmail.com", "soumya.cric4@gmail.com", message)
