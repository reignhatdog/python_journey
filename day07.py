#Password Generator
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def main():
    print("Day 7: Password Generator")
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
