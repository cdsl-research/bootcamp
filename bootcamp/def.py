import random

def add(x,y):
    print(x+y)

def sub(x,y):
    print(x - y)

def mul(x,y):
    print(x * y)

def div(x,y):
    print(x / y)

def ran1():
    print(random.random())

def ran2(x,y):
    print(random.randint(x,y))

def ran3(x,y):
    print(random.uniform(x,y))

add(3,5)
sub(3,5)
mul(3,5)
div(3,5)
ran1()
ran2(1,10)
ran3(1,10)