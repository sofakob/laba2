import re
import sys

def laba2val(parol):
    if len(parol) < 10:
        print("Password must have more than 10 symbols", file=sys.stderr)
        return 1

    if not any(char.isdigit() for char in parol):
        print("Password must have at least one digit", file=sys.stderr)
        return 1

    if not any(char.isupper() for char in parol) or not any(char.islower() for char in parol):
        print("Password must have at least one uppercase or lowercase letter", file=sys.stderr)
        return 1

    print("You are a smart person")
    return 0

if __name__ == "__main__":
    parol = input().strip()

    exit_code = laba2val(parol)
    sys.exit(exit_code)
