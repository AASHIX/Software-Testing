#====================================================
# File: Calculator.py
# Course: Software testing
# Author: Ashish Ajay
# Version: 1.2
# Description: A simple athematic calculator.

#======================================================

# This constant is not a strictly need yet, but it demonstrates the naming convention. (They are in UPPER CASE).


VERSION: str = "v1.2"

def add(a: float, b: float) -> float:
    """Returning the sum of two numbers"""
    return a+b

def subtract(a: float, b: float) -> float:
    """"Returns the of subtraction"""
    return a-b

def multiple(a: float, b: float) ->float:
    return a*b

def division(a: float, b: float) -> float:
    if b==0:
        raise ValueError("The value cannot be zero")
    return a/b

def displayResult(operation: str, a: float, b: float, result: float) -> None:
    print(f"[{VERSION}] {operation} ({a}, {b})= {result:.2f}") 


#This line of code will only execute when this file ran individually, if this imported then it will not run.
if __name__=="__main__":
    print("="*50)
    print(f"INFT 1207 - calculator.py demo ({VERSION})")
    print("="*50)
    displayResult("add", 10, 3, add(10, 3))
    displayResult("subtract", 10, 3, subtract(10, 3))
    displayResult("multiply", 10, 3, multiple(10, 3))
    displayResult("division", 10, 3, division(10, 3))
    

    

