def add():
    global num2
    x = 10
    global x
    num2 = 2000
    print("num1:",num1)
    print("num2:",num2)
    print("num1 + num2:",num1+num2)

num1 = 10
num2 = 20
print("before calling add() num2:",num2)
add()
print("after calling add()num2:",num2)