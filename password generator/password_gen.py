import string
import random

def main():
    print("------------------")
    print("Password Generator")
    print("------------------")
    
    while True: 
        try:
            num_characters = int(input("Number of characters (between 5 and 128): "))
            if 5 <= num_characters <= 128:
                break 
            else:
                print("Invalid! Use between 5 and 128 characters.")
        
        except ValueError:
            print("Invalid! Enter a number only.")
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(num_characters))
    print("Generated password:", password)

main()
