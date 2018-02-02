#!/usr/bin/env python

import smtplib
import argparse
import sys

# parse cmd arguments
cmd_parser = argparse.ArgumentParser(description='Email confirmation registry')
cmd_parser.add_argument('email', help='Email addresses to send to', nargs='+')
cmd_parser.add_argument('-c', metavar="CONTENT", dest="content", help='Email content to be sent. Defaults to stdin if omitted', nargs=1, type=argparse.FileType('r'), default=sys.stdin)
args = cmd_parser.parse_args()
print(args)

# in some cases args.content is returned as single element list
#   if it is then simply restore the element in args.content (remove list)
if isinstance(args.content, list):
    args.content = args.content[0]

for email in args.email:
    if '@' not in email and args.content.name != "<stdin>":
        print('Email "' +  email + '" is invalid. Only one argument to -c is allowed')
        exit()
    if '@' not in email:
        print('Email "' +  email + '" is invalid')
        exit()

# Set constants
CONST_GMAIL_SMTP = 'smtp.gmail.com'
TLS_PORT = 587
CLIENT_EMAIL = "anasayubi7152@gmail.com"
CLIENT_PASSWORD = ''
CONTENT = '' 

# print message if input will be taken from stdin
if args.content.name == "<stdin>":
    print("Message Content:")

# grab content (works for file or stdin)
CONTENT = args.content.read()

#print(CONTENT) 

# Get password
email_password_file = open("email_password.txt", "r")
CLIENT_PASSWORD = email_password_file.readline()

# Send email
for email in args.email:
    s = smtplib.SMTP(CONST_GMAIL_SMTP, TLS_PORT)
    print(s.ehlo())
    print(s.starttls())
    print(s.ehlo())
    print(s.login(CLIENT_EMAIL, CLIENT_PASSWORD))
    print(s.sendmail(CLIENT_EMAIL, email, CONTENT))
    print(s.quit())
