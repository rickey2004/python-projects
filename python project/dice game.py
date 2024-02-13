import random

for i in range(1,7):
    cc = random.randint(1,6)
    uc = int(input("enter the number between 1 to 6:-"))
    if( cc > uc ):
      print("cc is greater")
      print("cc number",cc)
      print("uc number",uc)
    elif(uc > cc):
      print("uc is greater")
      print("cc number", cc)
      print("uc number", uc)
    else:
      print("equal")