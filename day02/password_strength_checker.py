# Password Strength Checker

# Ask user to input their password
# check if passwoed length is 8 characters long
# check if it has numbers
# check if it has uppercase or lowercase
# print weak, medium or strong


user = input("Enter password: ")

password = user

has_digit = any(c.isdigit() for c in password)
has_lowercase = any(c.islower() for c in password)
has_uppercase = any(c.isupper() for c in password)

if len(password) <= 8:
    print("Weak") 
elif has_digit and has_lowercase and has_uppercase:
    print("Strong")
elif has_digit and (has_lowercase or has_uppercase):
    print("Medium")
else:
    print("Weak")



