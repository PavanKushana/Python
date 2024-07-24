import random

print("Let's play Rock-Paper-Scissors Game")
choice = input("Rock\nPaper\nScissors\nChoose one: ").lower()
# person = ["rock", "paper", "scissors"] user must select value matches in the list
# print(choice)

computer = ["rock", "paper", "scissors"]
count = len(computer) # total 3 values
select = random.randint(0, count - 1) #range in b/w 0 to 2
system = computer[select] # it assigns value w.r.t index in computer list
print(f"Computer choice: {system}")

if (choice == system):
    print("Match draw..Try again!")  
else:
    if (choice == "rock" and system == "scissors") or (choice == "paper" and system == "rock") or (choice == "scissors" and system == "paper"):
        print("You win")
    else:
        print("Computer wins")