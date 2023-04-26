#ssl is Secure Sockets Layer (secure link between server and browser)
#tls is the same thing but newer
#SMTP stands for Simple Mail Transfer Protocol

import require
import smtplib, ssl, os
import sys
import fullscreen
import regex

sys.path.append(os.getcwd() + '\\Contacts')

os.chdir(os.getcwd() + "/Contacts")

from process_contacts import *


try:
    linux_interaction()
except:
    pass

#your gmail account with less secure app access
sender = "pymessengerbot@gmail.com"
password = 'dwyzgykmzroygpip'
smtp_server = 'smtp.gmail.com'

#Requires sys.argv = [program name, phone number, message]
if len(sys.argv) > 1:
    carriers=['@text.att.net','@tmobile.net','@vtext.com','@messaging.sprintpcs.com']
    for carrier in carriers:
        receiver = str(sys.argv[1])+carrier
        context = ssl.create_default_context()
        port=587
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()                           #recognizes the server ehlo = helo
            server.starttls(context=context)
            server.ehlo()
            server.login(sender, password)
            server.sendmail(sender, receiver, sys.argv[2])
        except Exception as e:
            print("Error Occured")
            print(e)
        finally:
            server.quit()
    sys.exit()


print("""


  _____       _   _                   __  __
 |  __ \     | | | |                 |  \/  |
 | |__) |   _| |_| |__   ___  _ __   | \  / | ___  ___ ___  ___ _ __   __ _  ___ _ __
 |  ___/ | | | __| '_ \ / _ \| '_ \  | |\/| |/ _ \/ __/ __|/ _ \ '_ \ / _` |/ _ \ '__|
 | |   | |_| | |_| | | | (_) | | | | | |  | |  __/\__ \__ \  __/ | | | (_| |  __/ |
 |_|    \__, |\__|_| |_|\___/|_| |_| |_|  |_|\___||___/___/\___|_| |_|\__, |\___|_|
         __/ |                                                         __/ |
        |___/                                                         |___/

""")
print('')


port = 587 #(465 is SSL, 587 is TLS)

sender_copy = sender
sender = input('Enter your email (Press enter for default)(accounts must have "allow less secure app access" turned on):')

# enter here too
if not sender:
    sender = sender_copy
else:
    password=input('\nWhat is your password?: ')




class Error(Exception):
    pass
class ContactNotFoundError(Error):
    pass
class MultipleContactsError(Error):
    pass

searching=True

# number = ["phonenumber, name"]

while searching:
    try:
        querry = input('\nWho would you like to text?: ')

        #returns a list of possible names
        possible_contacts = regex.search(querry,import_contacts)

        print('\nSearching...')
        if possible_contacts == "no contacts":
            raise ContactNotFoundError

        if len(possible_contacts)>1:
            raise MultipleContactsError

    except ContactNotFoundError:
        addname=input('\nContact not found! \nWould you like to add a name to your Contacts?\n[y] or [n]: ')
        if addname == 'y':

            f_name=str(input('First Name of new contact: '))
            l_name=str(input('Last Name of new contact: '))
            pnum=str(input('Number of new contact: '))

            contacts_contents = [l_name, f_name, pnum, f_name + ' ' + l_name]
            add_contact(contacts_contents)
        else:
            continue

    except MultipleContactsError:
        print('\nMultiple possible contacts have been found.\n')
        choice=int(input('Choose which one you want to message: {}\nPlease respond with numbers (1-10)\nType \'0\' to quit \nChoice: '.format(possible_contacts)))
        if choice<=0:
            continue
        if choice !=0:
            number=[import_phonenumbers[import_contacts.index(possible_contacts[choice-1])], possible_contacts[choice-1]]
            searching=False
    else:
        badinput = True
        while badinput:
            confirmation=input('Are you sure you want to text: {} at {}? (y/n): '.format(possible_contacts[0], contacts.at[list(contacts["fullname"]).index(possible_contacts[0]),"Phone Number"]))
            if confirmation in ['y','n']:
                badinput = False
            else:
                print('\nPlease enter a valid character ("y" or "n")')
        if confirmation=='n':
            continue
        if confirmation=='y':
            number=[import_phonenumbers[import_contacts.index(possible_contacts[0])], possible_contacts[0]]
            searching = False;

not_confirmed=True
while not_confirmed:
    ask=input('\nWhat would you like to say?: ')
    bs=True
    while bs:
        confirmation=input('\nAre you sure you would like to send: "{}"?\n(y/n): '.format(ask))
        if confirmation in ['y','n']:
            bs=False
        else:
            print('\nPlease enter a valid character ("y" or "n")')

    if confirmation=='n':
        print('\nPlease re-write your message\n')
    if confirmation=='y':
        not_confirmed=False


message = """\

 {}

""".format(ask)
#message = MIMEText('<html><body><h1>Hello World</h1>' +
#'<p>this is hello world from <a href="http://www.python.org">Python</a>...</p>' +
#'</body></html>', 'html', 'utf-8')
#message.attach(MIMEText('<html><body><h1>Hello</h1>' +
#'<p><img src="cid:0"></p>' +
#'</body></html>', 'html', 'utf-8'))

badinput=True
while badinput:
    multi = input("Do you want to send this message multiple times? (y,n): ")
    if confirmation in ['y','n']:
        badinput=False
    else:
        print('\nPlease enter a valid character ("y" or "n")')

carrier_question = 0

if multi == 'y':
    times = int(input("How many times do you want it to send?: "))
    carrier_question = int(input("Which carrier: att, tmobile, vtext, sprint [1-4, zero for unknown]: "))
else:
    times = 1

phonenumber=str(number[0])
carriers=['@text.att.net','@tmobile.net','@vtext.com','@messaging.sprintpcs.com']

if(carrier_question >= 1):
    carriers = [carriers[carrier_question-1]]
    
for i in range(times):
    for carrier in carriers:
        try:
            receiver = phonenumber+carrier
            context = ssl.create_default_context()
            port=587
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()                           #recognizes the server ehlo = helo
            server.starttls(context=context)
            server.ehlo()
            server.login(sender, password)
            print('\nMessage sent to ',str(number[1]),' on ',carrier, ' at ',str(number[0]))
            server.sendmail(sender, receiver, message)
        except TypeError as e:
            print("Error Occured in sending")
            print("Password and Sender Address missing on line 26")
        finally:
            server.quit()
