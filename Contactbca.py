
contact = { }
def addContact(name,phone,email):
    contact[name] = {'phone':phone , 'email':email}
    print(f"Contact {name} added .")


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
            choice = int(input("Enter your choice"))
        except:
            print("Invalid input ! please enter a number between 1 and 6.")
            continue

        if choice ==1 :
            name = input("Enter your name :")
            email = input("Enter your email :")
            phone = input("Enter your phone :") 
            addContact(name,email,phone)   




if __name__ == "__main__":
    main()        

