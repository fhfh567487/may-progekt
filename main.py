import random
passwords = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
l = int(input('введите длину пороля'))
parol = ''
for i in range (l):
    parol+= random.choice(passwords)
print(parol)