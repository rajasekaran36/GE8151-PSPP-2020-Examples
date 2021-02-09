# guess a number
import random
low = 1
high = 1000
print("Guess any number from 1 to 1000")
guess = random.randint(low, high)
user_input = "s"
while(user_input != "C"):
    print("Guess:",guess)
    print("If Low type L or High type H or Correct type C")
    user_input = input()
    if(user_input=="L"):
        low = guess
    elif(user_input=="H"):
        high = guess
    guess = random.randint(low, high)