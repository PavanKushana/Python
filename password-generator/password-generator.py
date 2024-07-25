import random

print("Welcome to the Pypassword generator")

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?']

#how many letters do you want 
choice_letters = int(input("How many letters do you want: "))
#how many symbols do you want
choice_numbers = int(input("How many numbers do you want: "))
#how many numbers do you want
choice_symbols = int(input("How many symbols do you want: "))

len_letter = len(letters)
len_number = len(numbers)
len_symbol = len(symbols)



random_letter = 0
random_number = 0
random_symbol = 0

temp ="" #created a temporary variable


#Easy printing by concatinating strings

# #input for number
# for letter in range(1, (choice_letters + 1)):
#     random_letter = random.randint(0, (len_letter - 1))
#     new_letter = letters[random_letter]
#     temp += new_letter

# for number in range(1, (choice_numbers + 1)):
#     random_number = random.randint(0, (len_number - 1))
#     new_number = numbers[random_number]
#     temp += new_number

# for symbol in range(1, (choice_symbols + 1)):
#     random_symbol = random.randint(0, (len_symbol - 1))
#     new_symbol = symbols[random_symbol]
#     temp += new_symbol


# print(f"Your password is: {temp}")

# ---------------------------

#using random.choice()

for letter in range(1, (choice_letters + 1)):
    random_letter = random.choice(letters)
    temp += random_letter

for number in range(1, (choice_numbers + 1)):
    temp += random.choice(numbers)              

for symbol in range(1, (choice_symbols + 1)):
    temp += random.choice(symbols)

print(f"Your Password: {temp}")

#printing password randomly --> strong password

password_chars = []

# Add the specified number of random letters to the password
for _ in range(choice_letters):
    password_chars.append(random.choice(letters))

# Add the specified number of random numbers to the password
for _ in range(choice_numbers):
    password_chars.append(random.choice(numbers))

# Add the specified number of random symbols to the password
for _ in range(choice_symbols):
    password_chars.append(random.choice(symbols))

# Shuffle the characters in the password to ensure a random order
random.shuffle(password_chars)

# Join the list of characters into a single string to form the final password
password = ''.join(password_chars)

# Print the final password
print(f"Your strong password is: {password}")