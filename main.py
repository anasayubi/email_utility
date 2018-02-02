import smtplib

# Set constants
CONST_GMAIL_SMTP = 'smtp.gmail.com'
TLS_PORT = 587
CLIENT_EMAIL = "anasayubi7152@gmail.com"
CLIENT_PASSWORD = '' 

# Get password
email_password_file = open("email_password.txt", "r")
CLIENT_PASSWORD = email_password_file.readline()

# Send email
s = smtplib.SMTP(CONST_GMAIL_SMTP, TLS_PORT)
print(s.ehlo())
print(s.starttls())
print(s.ehlo())
print(s.login(CLIENT_EMAIL, CLIENT_PASSWORD))
print(s.sendmail(CLIENT_EMAIL, 'anasayubi@hotmail.com', "Subject: hello\nhey, how are you?"))
print(s.quit())
