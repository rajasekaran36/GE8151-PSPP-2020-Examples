number = 23
guess = int(input("enter a number:"))
#while(number!=guess):
#for i in range(1000000000):
while(number!=guess):
    print('Wrong Try again')
    guess = int(input("enter a number:"))
else:
    print('Hey you found my number 23')