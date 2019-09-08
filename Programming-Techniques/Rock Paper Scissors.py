from random import randint

endstate = False
loss = 0

while endstate == False:
    
    print()
    player = int(input("1: Rock, 2: Paper, 3: Scissors "))
    print()
    comp = randint(1,3) 

    if comp == 1:         
        c_choice = "rock."
    elif comp == 2:
        c_choice = "paper."
    elif comp == 3:
        c_choice = "scissors."

    if player == 1:          
        p_choice = "rock."
    elif player == 2:
        p_choice = "paper."
    elif player == 3:
        p_choice = "scissors."

    if player == comp:
        print("You chose", p_choice,"The computer chose", c_choice)
        print("You drew.")
        print()
    elif (player == 1 and comp == 2) or (player == 2 and comp == 3) or (player == 3 and comp == 1):
        print("You chose", p_choice,"The computer chose", c_choice)
        print("You lose.")
        print()
        loss = loss + 1
        if loss == 3:
            print("You're really unlucky huh?")
            print()
        elif loss == 10:
            print("Oh my god...")
            print("You should probably give up...")
            print()
    else:
        print("You chose", p_choice,"The computer chose", c_choice)
        print("You win.")
        print()
        loss = loss - 1
        if loss == -3:
            print("You're on a streak!")
            print()
        elif loss == -10:
            print("Don't get me wrong, I'm impressed.")
            print("But you should probably be using this luck on something more productive.")
            print()
        
    endstate = str(input("Do you wish to end? Y/N "))
    if endstate == "Y" or endstate == "y" or endstate == "Yes" or endstate == "yes":
            endstate = True
            print("Thanks for playing")
    else:
        endstate = False
