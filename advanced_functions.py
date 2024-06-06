#!/usr/bin/python3
"""Alta3 | TRPatrick
   Demonstration of Advanced Function Features"""








x = "This variable is set globally"

def test_scope():
    x = "This variable is local"
    print("Inside function:", x)

def print_greeting(message="Hello, World!"):
    print(message)


def main():
    print_greeting()
    print_greeting("Hello Function!")
    test_scope()
    print("outside function:", x)

if __name__ == "__main__":
    main()
