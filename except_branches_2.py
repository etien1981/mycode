#!/usr/bin/python3
"""Alta3 | TRPatrick
   Except Branching Example 2"""

def main():
    """Trying Generic Exception"""
    try:
        result = 1 / 0
    except Exception:
        print("Caught an unspecified error!")
    except ZeroDivisionError:
        print("This will never be reached.")


if __name__ == "__main__":
    main()

