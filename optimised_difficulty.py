import random
import string

print("\nWelcome to password generator")

def generate_password():
    password_length = int(input("What is your password length? "))
    print("****You can add uppercase letters, lowercase letters, numbers and special characters****\n")
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        num_upper = int(input("How many uppercase letters do you need? "))
        num_lower = int(input("How many lowercase letters do you need? "))
        num_digits = int(input("How many numbers do you need? "))
        num_special = int(input("How many special characters do you need? "))

        if num_upper + num_lower + num_digits + num_special == password_length:
            password = random.sample(string.ascii_uppercase, num_upper) + \
                       random.sample(string.ascii_lowercase, num_lower) + \
                       random.sample(string.digits, num_digits) + \
                       random.sample(string.punctuation, num_special)
            random.shuffle(password)
            final_password = ''.join(password)
            print(f"Your new password is: {final_password}")
            break
        else:
            print("Wrong inputs. The sum of character counts should equal the password length.")

generate_password()
