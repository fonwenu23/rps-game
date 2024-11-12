def rps():
    choice = ['rock', 'paper', 'scissors']
    bot = random.choice(choice)

    my_choice = input("Enter rock', 'paper', 'scissors': ").lower()
    if my_choice not in choice:
        print(f"Invalid selection. Try again.")
        return rps()

    print(f"You picked {my_choice}.")
    print(f"The computer chose {bot}.")

    if my_choice == bot:
        print(f"The game is a tie.") 
    elif my_choice == 'paper' and bot == 'scissors' or\
         my_choice == 'rock' and bot == 'paper' or\
         my_choice == 'scissors' and bot == 'rock':
        print(f"You lose! Try again!")
    else:
        print(f"Nice! You Win")

rps()