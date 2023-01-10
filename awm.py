import math


def add():
    a = int(input("a :"))
    b = int(input("b :"))
    c = a + b
    print("Result,", c)
    return c


def ext():
    a = int(input("a :"))
    b = int(input("b :"))
    c = a - b
    print("Result,", c)
    return c


def div():
    a = int(input("a :"))
    b = int(input("b :"))
    c = a / b
    print("Result,", c)
    return c


def multiply():
    a = int(input("a :"))
    b = int(input("b :"))
    c = a * b
    print("Result,", c)
    return c


def pov():
    a = int(input("a :"))
    b = int(input("b :"))
    c = math.pow(a, b)
    print("Result,", c)
    return c


def sqrt():
    a = int(input("a :"))
    c = math.sqrt(a)
    print("Result,", c)
    return c


def fac():
    a = int(input("a :"))
    c = math.factorial(a)
    print("Result,", c)
    return c
