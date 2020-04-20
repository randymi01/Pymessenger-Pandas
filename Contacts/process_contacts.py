from csv import writer
from csv import reader

import_contacts = []
import_phonenumbers = []

def add_contact(list_of_elem):
    file_name = 'formatted_contacts.csv'
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)
    refresh()

#Last Name,First Name,Phone Number,fullname
row_contents = ["test", "test", "test", "test"]

#add_contact(row_contents)

def refresh():
    with open('formatted_contacts.csv', newline='') as stream:
        read = reader(stream)
        for row in read:
            if(row[3] != 'fullname'):
                import_contacts.append(row[3])
            if(row[2] != 'Phone Number'):
                import_phonenumbers.append(row[2])

refresh()
