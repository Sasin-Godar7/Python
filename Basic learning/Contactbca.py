
contact = { }

def addContact(name,phone,email,address):
    contact[name] = {'phone':phone , 'email':email ,'address':address}
    print(f"Contact {name} added .")


def update_contact(name,phone = None , email=None ,address=None):
    if name in contact:
        if phone:
            contact[name]['phone'] = phone 
        if email :
            contact[name]['email'] = email
        print(f"contact {name} updated.")

        if address :
            contact[name]['address'] = address
        print(f"contact {name} updated.")

    else:
        print(f"contact {name} not found.")


def delete_contact(name):
    if name in contact:
        del contact[name]
        print(f"contact {name} deleted.")

    else:
        print(f"Contact {name} not found.")  


def search_contact(name):
    if name in contact:
        print(f"Name: {name}")
        print(f"Phone: {contact[name]['phone']}")
        print(f"Email: {contact[name]['email']}")
        print(f"Address: {contact[name]['address']}")

    else:
        print(f"Contact {name } not Found.")


def display_all_contact(name):
    if contact:
        for name,details in contact.items():
            print(f"Name :{name},Phone:{details['phone']} , Email:{details['email']} , Address:{details['address']}")
    else:
        print("No contacts available")            


def main():
    while True:
        print("\n Contact Book Menu -->>>")
        print("1.Add Contact")
        print("2.Update Contact")
        print("3.Delete Contact")
        print("4.Search Contact")
        print("5.Display All Contact")
        print("6.Exit")

        try:
            choice = int(input("Enter your choice :"))
        except:
            print("Invalid input ! please enter a number between 1 and 6.")
            continue

        if choice ==1 :
            name = input("Enter your name :")
            email = input("Enter your email :")
            phone = input("Enter your phone :") 
            address = input("Enter your address :")
            addContact(name,email,phone,address) 

        if choice == 2:
            name = input("enter the name to update the contact :")
            phone =input("enter new phone number (leave blank to keep current):")  
            email =input("enter new  emial (leave blank to keep current):")  
            update_contact(name,phone if phone else None , email if email else None) 

        elif choice == 3:
            name =  input("enter the name to delete the contact :")
            delete_contact(name)   

        elif  choice == 4:
            name = input("enter the name to search the contact :")
            search_contact(name)      

        elif  choice == 5 :
           
            display_all_contact(name)

        elif  choice == 6 :
            print("Exiting the program")  
            break   


if __name__ == "__main__":
    main()  


