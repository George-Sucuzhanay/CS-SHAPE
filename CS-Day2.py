import random 


while True:  #infinite loop!
  # First, read player move
  player_move = input("Please choose (r)ock, (p)aper, or (s)cissors: ")
  print("You chose ", player_move)

  if player_move == 'q':
    print("Goodbye")
    break

  if player_move != 'r' and player_move != 'p' and player_move != 's':
    print("Invalid move. ")
    continue 
  

  # Then, randomly select computer move
  computer_move = random.choice(['r','p','s']) 
  print("Computer chose ", computer_move)

  # Finally, determine the winner 

  if (player_move == 'r' and computer_move == 's') or \
      (player_move == 'p' and computer_move == 'r') or \
      (player_move == 's' and computer_move == 'p'): 
        print("Player wins.")

  elif (player_move == 'r' and computer_move == 'p') or \
      (player_move == 'p' and computer_move == 's') or \
      (player_move == 's' and computer_move == 'r'): 
        print("Computer wins.")

  else: 
      print("Draw.")
