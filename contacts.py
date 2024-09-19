# Jonathan Nuez
# 9/16/24
# Purpose: Manages the contact list (add, modify, delete, sort)

def add_contact(contact_list, first_name="", last_name=""):
    contact_list.append([first_name, last_name])

def modify_contact(contact_list, index=0, first_name="", last_name=""):
    if 0 <= index < len(contact_list):
        contact_list[index] = [first_name, last_name]
        return True
    return False

def delete_contact(contact_list, index=0):
    if 0 <= index < len(contact_list):
        contact_list.pop(index)
        return True
    return False

def sort_contacts(contact_list, column=0):
    contact_list.sort(key=lambda x: x[column])
