import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_leght = int(input("Masukkan panjang password"))

password = ""
for i in range(pass_leght):
    password += random.choice(karakter)
print (password)
