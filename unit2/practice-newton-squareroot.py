print("Newton Method to find sq_root")
num = int(input("Enter number: "))
guess = 1
while(True):
    x = guess
    f_x = (x**2) - num
    f_d_x = 2*x
    actual = x - (f_x/f_d_x)
    actual = round(actual,6)
    if(guess == actual):
        break
    else:
        print("guess=",guess,"actual=",actual)
        guess = actual

print("sq_root of",num,"is",guess)