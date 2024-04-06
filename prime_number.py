a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

a = int(a)
b = int(b)

sosu = True
if a <= 1:
    sosu = False
else:
    i = 2
    while i < a:
        if a % i == 0:
            sosu = False
            break
        i += 1

if sosu:
    print("素数です")
else:
    print("素数ではありません")

sosu = True
if b <= 1:
    sosu = False
else:
    i = 2
    while i < b:
        if b % i == 0:
            sosu = False
            break
        i += 1

if sosu:
    print("素数です")
else:
    print("素数ではありません")

