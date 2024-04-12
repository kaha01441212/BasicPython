a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
a = int(a)
b = int(b)
def soha(a):
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
        return True 
    else:
        return False

print(soha(a))
print(soha(b))