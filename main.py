
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
usr_letters = int(input("Enter how many letters you want in your password\n"))
usr_symbols = int(input("Enter how many symbols you want in your password\n"))
usr_numbers = int(input("Enter how many numbers you want in your password\n"))
total_len_pass = usr_letters+usr_symbols+usr_numbers
rand_pass = []
for letter in range(0, usr_letters):
    rand_pass += random.choices(letters)
for symbol in range(0, usr_symbols):
    rand_pass += random.choices(symbols)
for number in range(0, usr_numbers):
    rand_pass += random.choices(numbers)
random.shuffle(rand_pass)
output = "".join(rand_pass)
print(output)









