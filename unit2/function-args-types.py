#positional arguments
def greetPerson1(name,msg):
    print("Hello "+name+"! "+msg+".")
greetPerson1("raj","welcome")
#default args
def greetPerson(name,msg="welcome"):
    print("Hello "+name+"! "+msg+".")

greetPerson("raj")
greetPerson("bala","how are you?")

#keyword arguments
greetPerson(msg="how are you?",name="shiva")

#arbitrary arguments 
def greetAll(*names):
    for name in names:
        print("Hello "+name+"! "+"welcome")

greetAll("raj","shiva")
greetAll("raj","shiva","bala")
greetAll("raj","shiva","bala","joel")