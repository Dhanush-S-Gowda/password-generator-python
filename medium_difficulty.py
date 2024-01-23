import random
print("\nWelcome to password generator")
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
specialChar = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

password = []

while True:
    passwordLength = int(input("What is your password length?"))
    print("****You can add uppercase letters, lowercase letters, numbers and special characters****\n")
    upCaseFlag = int(input("How many uppercase letters do you need? "))
    loCaseFlag = int(input("How many lowercase letters do you need? "))
    numFlag = int(input("How many numbers do you need? "))
    charFlag = int(input("How many special characters do you need? "))
    if(upCaseFlag + loCaseFlag + numFlag + charFlag == passwordLength):
        while(upCaseFlag):
            password.append(random.choice(upperCase))
            upCaseFlag-=1
        while(loCaseFlag):
            password.append(random.choice(lowerCase))
            loCaseFlag-=1
        while(numFlag):
            password.append(random.choice(numbers))
            numFlag-=1
        while(charFlag):
            password.append(random.choice(specialChar))
            charFlag-=1
        break
    else:
        print("Wrong inputs. The sum of character counts should equal the password length.")

random.shuffle(password)
final_password = ""
for char in password:
    final_password+=str(char)

print(f"Your new password is {final_password}")
