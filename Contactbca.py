
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

if __name__ == "__main__":
    main()        