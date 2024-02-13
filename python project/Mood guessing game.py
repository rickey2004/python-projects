
mood=['happy', 'anger','sad']
print(mood)
print()
print("Enter your choice:-")
user = int(input(''' 1 = Happy
 2 = anger
 3 = sad :-'''))
print("Enter your choice:-")
if (user == 1 ):
  userchoice = 'happy :-'
  print(userchoice," its good to be happy")
elif ( user == 2 ):
    userchoice = 'anger :-'
    print(userchoice,"calm down")

elif( user == 3):
    userchoice = 'sad :-'
    print(userchoice,'always keep smiling')
else:
    print('not statement found')
