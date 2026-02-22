import random
...
#1 for rock
#-1 for paper
#0 for scissor
...
computer = random.choice([-1,0,1])
youenter = input("Enter your choice: ")
if youenter not in ["r","p","s"]:
    print("invalid choice! please enter r , p or s.")
    exit()
yordict = {"r":1 ,"p":-1 , "s":0 }
reversedict = {1  :"r", -1 :"p", 0 :"s" }
you = yordict[youenter]
print(f"You chose {reversedict [you]}\nComputer chose {reversedict[computer]}")
if(computer == you):
    print("it's a draw!")
else:
    if(computer == -1 and you == 1):
        print("you lose!...you did well but better luck next time..")
    elif(computer == -1 and you == 0):
        print("you win")
    elif(computer == 1 and you == 0):
        print("you lose!...you did well but better luck next time..")
    elif(computer == 1 and you == -1):
        print("you win!")
    elif(computer == 0 and you == 1):
        print("you win!")
    elif(computer == 0 and you == -1):
        print("you lose!...you did well but better luck next time..")
    else:
        print("something went wrong!")
        
    