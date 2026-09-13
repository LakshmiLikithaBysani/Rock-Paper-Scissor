import random

print("✊ Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper, or scissors: ").lower()

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("🤝 It's a Tie!")

elif user == "rock" and computer == "scissors":
    print("🎉 You Win!")

elif user == "paper" and computer == "rock":
    print("🎉 You Win!")

elif user == "scissors" and computer == "paper":
    print("🎉 You Win!")

elif user in choices:
    print("😔 Computer Wins!")

else:
    print("❌ Invalid choice!")