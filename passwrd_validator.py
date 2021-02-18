import re

# password must consist of upper and lower case letters
# password also must consist of a number and a special character

print('\n\tPASSWORD VALIDATOR')
# Print conditions
print("\nTo pass the password test the password must conist of:\n\n\
    - 1 or more CAPITAL letters (A-Z)\n\
    - 1 or more lowercase letters (a-z)\n\
    - 1 or more numbers (0-9)\n\
    - 1 or more special characters (!@#$%^&*-+=_)\n\
    - Password must be at least 8 characters long")

# Ask user to enter the password:
password = input("\nPlease enter your password to test: ")


if re.search(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*-+=_]){8,}',password):
    print(f"Entered password: '{password}' is STRONG enough!")

# REGEX:
# ?=.* - at least 1 character in the string
# {8,} - len(string) is 8 or more characters
# r'' - raw string

else: # print which condition is not satisfied
    if len(password) < 8:
        print("Entered password is too short!")
    elif re.search(r'(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*-+=_]){8,}',password):
        print("Password is missing a uppercase haracter (A-Z)!")
    elif re.search(r'(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*-+=_]){8,}',password):
        print("Password is missing a lowercase character (a-z)!")
    elif re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*-+=_]){8,}',password):
        print('Password is missing a number (0-9)')
    else:
        print("Password is missing a special character (!@#$%^&*-+=_)")