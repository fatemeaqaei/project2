import math
second=int(input("enter second: "))

houre=second/3600
a=second%3600
minute=a/60
second=a%60
print("result is: ",math.floor(houre),":",math.floor(minute),":",math.floor(second) )