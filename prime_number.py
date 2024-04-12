a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
def soha(a):
    a = int(a)
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
        return "素数です"  
    else:
        return "素数ではありません"  

print(soha(a))
print(soha(b))
