#ssl is Secure Sockets Layer (secure link between server and browser)
#tls is the same thing but newer
#SMTP stands for Simple Mail Transfer Protocol

import smtplib, ssl, os
import sys
from email.mime.text import MIMEText

# Account Details
sender = "pymessengerbot@gmail.com"
password = "dwyzgykmzroygpip"
smtp_server = "smtp.gmail.com"


def send_message(phone_number:str, message:str, subject = "",carrier = None, port = 587):
    
    # format phone_number
    phone_number = "".join([i for i in phone_number if i.isnumeric()])

    carriers=['@text.att.net','@tmobile.net','@vtext.com','@messaging.sprintpcs.com']

    carrier_hash_table = {
        "att": "@text.att.net",
        "tmobile": "@tmobile.net",
        "verizon": "@vtext.com",
        "sprint": "@messaging.sprintpcs.com"
    }

    carrier_defined = False
    if carrier:
        carrier = carrier_hash_table[carrier]
        carrier_defined = True
    
    # message body goes here
    msg = MIMEText(message, 'plain')
    msg['Subject'] = f"Subject: {subject}"

    message = msg.as_string()

    # initialize server
    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()                           
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)
        
    # send mail
    if carrier_defined:
        server.sendmail(sender, phone_number+carrier, message)
        print(f"Sent to {phone_number+carrier}\n")
    else:
        for carrier in carriers:
            receiver = phone_number+carrier
            server.sendmail(sender, receiver, message)
            print(f"Sent to {receiver}\n")
    
    # quit server
    server.quit()


if __name__ == "__main__":
    # py main.py phone_number message subject carrier
    send_message(*[sys.argv[i] for i in range(1,len(sys.argv))])