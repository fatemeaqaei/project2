a = 1
b = 0
n = int(input("enter a number: "))

for i in range(n):
    c = a + b
    a = b
    b = c
    print("fibonachi series is: ",c)    
