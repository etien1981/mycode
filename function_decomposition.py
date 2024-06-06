#!/usr/bin/python3
"""Alta3 | TRPatrick
   Building User-Defined Functions"""
  
  




# User-defined function
def greet(name):
    print(f"Hello, {name}!")
def add(a,b):
    return a + b




def main(): 
    greet(input("What is your name!\n"))
   
    result = add(5, 3)
    print("5+3 =", result)

if __name__ == "__main__":
  main()
