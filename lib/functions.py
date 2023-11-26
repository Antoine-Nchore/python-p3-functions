#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name='Nchore'):
    print(f"Hello {name}")
greet()

def greet_with_default(name="programmer"):
    print(f"Hello, {name}")
greet_with_default()

def add(num1, num2):
    sum = num1 + num2
add(20,30)

def halve(number=10):
    division= number/2
    print(division)