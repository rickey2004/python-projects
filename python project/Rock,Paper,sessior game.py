import random
ucount = 0
ccount = 0
l = ['rock','paper','scissor']
uc = int(input('''1 = yes
2 = no|exit'''))
while True:
 if uc==1:
  ui = int(input(''' 1 rock
  2 paper
  3 scissor'''))
  if ui==1:
    uch = "rock"
  elif ui==2:
      uch = "paper"
  elif ui == 3:
      uch = "scissor"
  # else:
  #     print("wrong statement")
  cch = random.choice(l)
  print(cch)

  if ((uch == "rock" and cch == "scissor") or (uch == "paper" and cch == "rock") or (uch == "scissor" and cch == "paper")):
      print("user choice", uch)
      print("computer choice", cch)
      print("user won!")
      ucount = ucount + 1
  elif((cch == "rock" and cch == "scissor") or (cch == "paper" and uch == "rock") or (cch == "scissor" and uch == "paper")):
      print("user choice", uch)
      print("computer choice", cch)
      print(" computer won!")
      ccount = ccount + 1
  else :
    print("user choice", uch)
    print("computer choice", cch)
    print(" Draw!")
    ucount = ucount + 1
    ccount = ccount + 1
  if ucount==ccount:
      print("Final game draw..")
      print("User score", ucount)
      print("Computer score", ccount)
  elif ucount>ccount:
      print("finally you won the game..")
      print("User score", ucount)
      print("Computer score", ccount)
  else:
      print("finally computer won the game..")
      print("User score", ucount)
      print("Computer score", ccount)

 else:
      break

