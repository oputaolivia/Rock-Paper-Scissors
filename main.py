import random

while True:
  outcomes = {"R": "Rock", "P": "Paper", "S": "Sicssors"}
  outcome = list(outcomes)
  player = input("Enter either R, P or S: ").upper()
  CPU = random.choice(outcome)

  #Validating input
  if player in outcomes:
    print(f"'Player({outcomes[player]}) : CPU({outcomes[CPU]})'")
  else:
    print("Invalid input")
    continue 

  # Determining winner
  if player == CPU:
    print("It's a tie")
    continue
  elif player =="R":
    if CPU == "S":
      print("Player wins and CPU lost")
    else:
      print("CPU wins and Player lost")
  elif player == "S":
    if CPU == "P":
      print("Player wins and CPU lost")
    else:
      print("CPU wins and Player lost")
  elif player =="P":
    if CPU == "R":
      print("Player wins and CPU lost")
    else:
      print("CPU wins and Player lost")
  break
