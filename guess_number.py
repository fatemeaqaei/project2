import random 

counter=1
computer_number=random.randint(10,40)
for i in range(10):
    user_number=int(input("enter your guess number: "))
    if computer_number==user_number:
        print("you win 😎")
        break
    elif computer_number>user_number:
        counter+=1
        print("go up ⬆")
    elif computer_number<user_number:
        counter+=1
        print("go down ⬇")
print("the number of your guess is: ",counter)