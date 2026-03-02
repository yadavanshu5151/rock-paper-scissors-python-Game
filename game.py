import random
while True:
# 1 for Rock
# -1 for Paper
# 0 for Scissors

 computer = random.choice([-1, 0, 1])
 user_input = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").lower()

 if user_input not in ["r", "p", "s"]:
        print("Invalid Choice! Please enter R, P, or S.")
        continue
 choice_dict = {"r": 1, "p": -1, "s": 0}
 reverse_dict = {1: "Rock", -1: "Paper", 0: "Scissors"}

 user = choice_dict[user_input]

 print("\n---------------------------")
 print(f"You chose: {reverse_dict[user]}")
 print(f"Computer chose: {reverse_dict[computer]}")
 print("---------------------------")

 if computer == user:
                  print("Result: It's a Draw!")
 else:

     if (computer == -1 and user == 1):
             print("Result: You Lose!")
     elif (computer == -1 and user == 0):
            print("Result: You Win!")
     elif (computer == 1 and user == 0):
             print("Result: You Lose!")
     elif (computer == 1 and user == -1):
            print("Result: You Win!")
     elif (computer == 0 and user == 1):
             print("Result: You Win!")
     elif (computer == 0 and user == -1):
            print("Result: You Lose!")
     else :
            print("Unexpected Error!")

   # Ask to restart
 play_again = input("\nDo you want to play again? (Y/N): ").lower()

 if play_again == "n":
  print("Thanks for playing! ")
  break
 