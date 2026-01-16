import random

"""
1 for snake 
-1 for water
 0 for gun

"""

computer = random.choice([-1, 0, 1])
youstr= input("Enter your choice : ")
youdict = {'s':1,'w':-1,'g':0}
reversedict = {1:'snake',-1:'water',0:'gun'}
you = youdict[youstr]

#by now we have 2 variables (computer and you)

print(f"Computer chose {reversedict[computer]}\nYou chose {reversedict[you]}")
if computer == you:
    print("Match Draw")
else:
    if({computer - you} == -1 or {computer - you} == 2):
        print("You Lose")
    else:
        print("You Win")
# if(computer == -1 and you == 1):
#     print("You win")

# elif(computer == -1 and you == 0):
#     print("You lose")

# elif(computer == 1 and you == -1):
#     print("You lose")

# elif(computer == 1 and you == 0):
#     print("You win")

# elif(computer == 0 and you == -1):
#     print("You lose")

# elif(computer == 0 and you == 1):
#     print("You win")
