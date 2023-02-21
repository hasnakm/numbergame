import random

a=0
print("Guss a number within 1 and 100")
print("You have only 5 chances")
x = random.randrange(1,100)
while(a<5):
    n = int(input("Enter your selection: "))

    if n==x:
        print("You Won the Game!")
        break
    else:
        a+=1
        print(x)
        print("You Failed")
        print("You have only ",5-a," attempts left")
        
if a==5:
            print("GAME OVER")        