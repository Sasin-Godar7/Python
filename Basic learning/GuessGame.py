import random 
randomnum = random.randint(1,20)
attempt =0 
print("Welcome to the guessing game \n")


while True:
    guess = input("\nEnter your guess number from 1 - 20 (or type 'a' to quit :) ")
    if guess =='a':
        print(f"Thanks for playing secrect number was {randomnum}")
        break
    if not guess.isdigit():
        print("please enter the valid number")
        continue
    guess = int(guess)
    attempt += 1

    if guess == randomnum:
        print(f"Yayy you guess it perfectly in {attempt} attempt")
        break

    elif guess<randomnum:
        print("Your guess is low !! Try higher number")

    else:
        print("Your guess is high !! Try lower numbers")

    