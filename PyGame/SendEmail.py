import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email form Python"
sender_email = "waynendlovu16@gmail.com"
receiver_email = "waynendlovu16@gmail.com"
password = input("Enter a password:")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email")
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
     server.login(sender_email, password)
     server.sendmail(sender_email, receiver_email,message.as_string())

     print("Success")
