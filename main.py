import random
import side 

print()
side.print_in_box("Welcome to Stoners, Paper, Scissors")

def compChoice():
  return random.randrange(3)

def playerChoice():
  print("---------------------------------------")
  print("Choose an option:")
  print("0: Stone")
  print("1: Paper")
  print("2: Scissors")
  n = int(input("\nEnter the number of your choice (0, 1, or 2): "))

  if n in [0,1,2]:
    return n
  else:
    raise Exception("Inappropriate choice.")

def getResult(comp,player):
  # 0 --> stone
  # 1 --> paper
  # 2 --> scissors

  # computer:player
  #   player stone, player paper, player scissors
  l = [['D',        'W',          'L'],  #computer stone
       ['L',        'D',          'W'],  #computer paper
       ['W',        'L',          'D']]  #computer scissors
  
  # win-loss-draw is for player
  return l[comp][player]

def printResult(res):
  print()

  match res:
    case 'D':
      print("Match Draw!")
    case 'W':
      print("You have Won!")
    case 'L':
      print("You have Lost!")
    case _:
      pass
  return

def play():
  try:
    printResult(getResult(compChoice(), playerChoice()))
    pass
  except Exception as e:
    print(f"ERROR: {e}")



while True:
  play()

  ch = input("\nExit(y/)?: ")
  if ch == "y":
    print("---------------------------------------")
    break
  print("---------------------------------------")