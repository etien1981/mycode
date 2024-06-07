#!/usr/bin/python3
"""Alta3 | TRPatrick
   Except Branching Example 3"""

def main():
    """Using a Single Except Statement"""
    try:
        # This code block is intentionally designed to throw a division by zero error
        result = 1 / 0
    except (ZeroDivisionError, ValueError) as e:
        print(f"Caught an error: {e}")

if __name__ == "__main__":
    main()

