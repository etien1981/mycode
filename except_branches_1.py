#!/usr/bin/python3
"""Alta3 | TRPatrick
   Except Branching Example 1"""

def main():
    """Try, with Multiple Except Branches"""
    try:
        # This code block is intentionally designed to throw a division by zero error
        result = 1 / 0
    except ZeroDivisionError:
        print("Caught a division by zero!")
    except ValueError:
        print("Caught a value error!")
    except Exception:
        print("Caught an unspecified error!")

if __name__ == "__main__":
    main()

