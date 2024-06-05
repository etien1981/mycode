#!/usr/bin/env python3
"""if, elif, else - A simple program using conditionals to make a decision."""

grade = float(input("What was your assignment grade?"\n))
print(grade)
if grade >= 90:
    print("Your Grade is A")
elif grade >= 80 and grade <= 89:
    print("Your Grade is B")
elif grade >= 70 and grade <= 79:
    print("Your Grade is C")
elif grade >= 60 and grade <= 69:
    print("Your Grade is D")
else: 
    print("You failed")
