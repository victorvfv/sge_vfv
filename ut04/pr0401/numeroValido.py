import random

def numeroValido():
    x= random.randint(1,100000)
    y=""
    while(y!=x):
        print("dime el numero: " + str(x))
        y=int(input())
    print("muchas gracias")

numeroValido()