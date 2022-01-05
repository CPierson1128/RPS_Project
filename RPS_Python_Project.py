def game_iteration():
    acceptable_input = ['rock', 'paper', 'scissors']
    while True:
        p1_turn = input("Player 1, enter rock, paper or scissors: ").lower()
        if p1_turn in acceptable_input:
            break
        else:
            print("Invalid entry, please re-enter")
    while True:
        p2_turn = input("Player 2, enter rock, paper or scissors: ").lower()
        if p2_turn in acceptable_input:
            break
        else:
            print("Invalid entry, please re-enter") 

    if p1_turn == p2_turn:
        print("It's a tie!")
    elif p1_turn == 'rock' and p2_turn == 'paper':
        print("Player 2 wins!")
    elif p1_turn == 'rock' and p2_turn == 'scissors':
        print("Player 1 wins!")
    elif p1_turn == 'paper' and p2_turn == 'rock':
        print("Player 1 wins!")
    elif p1_turn == 'paper' and p2_turn == 'scissors':
        print("Player 2 wins!")
    elif p1_turn == 'scissors' and p2_turn == 'rock':
        print("Player 2 wins!")
    elif p1_turn == 'scissors' and p2_turn == 'paper':
        print("Player 1 wins!")
    else:
        print("Application Error")

play_again = "yes"
while play_again == 'yes':
    game_iteration()
    while True:
        play_again = input("Do you want to play again? Yes or No? ").lower()
        if play_again == 'no':
            print("Thanks for playing!")
            break
        elif play_again == 'yes':
            break
        else:
            print("Invalid entry, please re-enter")
