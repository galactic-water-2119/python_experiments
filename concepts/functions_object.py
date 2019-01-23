#functions as a object

def bro(msg):
    print(msg)

bro("You are my bro")



#functions as arguments

def adding(x):
    return x + (x*x)

def substracting(x):
    return (x*x) - x

def operate(func, x):
    result = func(x)
    return result

friend = bro
friend("You are my friend")
a = operate(adding, 2)
b = operate(substracting, 3)

print(a,b)

# functions return function / nested function

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

#outputs "Hello"
new()



def dupe_easiely(func):
    def inner():
        print("I got duped")
        func()
    return inner

def ordinary():
    print("I am an ordinary person")

duped = dupe_easiely(ordinary)
duped()