import random

computer_score=0
user_score=0

while user_score < 5 and computer_score < 5:
    print("1. Rock 🧱")
    print("2. Paper 📃")
    print("3. Scissors 🔪")

    computer_choice=random.randint(1,3)
    user_choice=int(input("enter your choice: "))

    
    print("the computer choice is: ",computer_choice)
    print("the user choice is :",user_choice)

    if user_choice==1 and computer_choice==2:
        computer_score+=1

    elif user_choice == 1 and computer_choice == 3:
        user_score += 1

    elif user_choice == 2 and computer_choice == 1:  
        user_score += 1

    elif user_choice == 2 and computer_choice == 3:
        computer_score += 1

    elif user_choice == 3 and computer_choice == 1:
        computer_score += 1

    elif user_choice == 3 and computer_choice == 2:
        user_score += 1

if user_score < computer_score:
    print()
    print("computer wins! 💻")

elif user_score > computer_score:
    print("You win 🎉")