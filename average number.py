average=0
counter=0

while(True):
    num=input("enter your grade: ")
    if num=='exit':
        break
    else:
        average=average+int(num)
        counter+=1

print("student average number is: ",str(average/counter))

