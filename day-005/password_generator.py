import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
letter = int(input("How many letter would you like in your password?"))
symbol =  int(input("How many symbols would you like?"))
number = int(input("How many numbers would you like?"))


total1 = []
total2 = []


for i in range(1,letter+1):
    num_random = random.randint(0,len(letters)-1)
    total1.append(letters[num_random])
    total2.append(letters[num_random])


for i in range(1,symbol+1):
    num_random = random.randint(0,len(symbols)-1)
    total1.append(symbols[num_random])
    total2.append(symbols[num_random])

for i in range(1,number+1):
    num_random = random.randint(0,len(numbers)-1)
    total1.append(numbers[num_random])
    total2.append(numbers[num_random])


password1 = ""

for i in range(1,len(total1)+1):
    pos_random = random.randint(0,len(total1)-1)
    password1 = password1 + total1.pop(pos_random)

print(f"El primer password es: {password1}")

# Other form 

password2 = ""

random.shuffle(total2)
for i in total2:
    password2+=i
print(f"El segundo password es: {password2}")


