print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆


# Write your code below this line 👇
two_names = name1 + " " + name2
low_char = two_names.lower()
# print(low_char)
t = low_char.count("t")
r = low_char.count("r")
u = low_char.count("u")
e = low_char.count("e")

true = t + r + u + e

# print(true)

l = low_char.count("l")
o = low_char.count("o")
v = low_char.count("v")
e = low_char.count("e")

love = l + o + v + e

total = str(true) + str(love)

love_total = int(total)

if love_total < 10 or love_total > 90:
  print(f"Your score is {love_total}, you go together like coke and mentos.")
elif love_total > 39 and love_total < 51:
  print(f"Your score is {love_total}, you are alright together.")
else:
  print(f"Your score is {love_total}.")