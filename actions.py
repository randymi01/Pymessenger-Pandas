def search():
    searching=True
    while searching:
        try:
            querry=input('\nWho would you like to text?: ')
            number=cus.search(cus.contacts,querry) #number=[phonenumber, name]
            print('\nSearching...')
            if number=='failed':
                raise ContactNotFoundError
            if number[0]=='multiple':
                raise MultipleContactsError

        except ContactNotFoundError:
            addname=input('\nContact not found! \nWould you like to add a name to your Contacts?\n[y] or [n]: ')
            if addname == 'y':
                name=str(input('Name of new contact: '))
                pnum=str(input('Number of new contact: '))
                cus.addname(name,pnum)
            else:
                pass
        except MultipleContactsError:
            matches=number[1]
            print('\nMultiple possible contacts have been found.\n')
            choice=int(input('Choose which one you want to message: {}\nPlease respond with numbers (1-10)\nType \'0\' to quit \nChoice: '.format(matches)))
            if choice==0:
                quit()
            if choice !=0:
                number=cus.search(cus.contacts,matches[choice-1])
                searching=False
        else:
            bs=True
            while bs:
                confirmation=input('Are you sure you want to text: {} at {}? (y/n): '.format(number[1],number[0]))
                if confirmation in ['y','n']:
                    bs=False
                else:
                    print('\nPlease enter a valid character ("y" or "n")')
            if confirmation=='n':
                quit()
            if confirmation=='y':
                searching=False
        return number

def send(receiver, message, **kwargs):
    if kwargs:
        for key,item in kwargs.items():
            if key=="port":
                global port
                port=int(item)
            elif key=="context":
                global context
                context=str(item)
            else:
                continue
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()                           #recognizes the server ehlo = helo
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)
    print('\nMessage sent to ',number[1],' on ',carrier)
    server.sendmail(sender, receiver, message)
    server.quit()

def annoy():
    phonenumber=search()
    message=input('What is your repeating message?: ')
    times=int(input('How many times would you like to annoy?: '))
    for i in range(times):
        for carrier in carriers:
            receiver = phonenumber+carrier
            context = ssl.create_default_context()
            try:
                send(receiver, message, port=587)
            except Exception as ex:
                print(ex)
