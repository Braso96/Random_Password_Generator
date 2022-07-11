import random
import string

print('Hello, I am here to generate a Password for you!')

length = int(input('\nEnter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

total = lower + upper + num +symbols

temp = random.sample(total, length)

password = "".join(temp)

print(f'This is your Password: {password}')



