a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a = int(a)
b = int(b)
def euclid(c, d):
    if c < d:
        c, d = d, c 
    
    kari = 0
    while d != 0:
        kari = c % d
        c = d
        d = kari
        
    return c

def tagainiso(a, b):
    if euclid(a, b) == 1:
        return True
    else:
        return False

number = euclid(a, b)
print(number, "が最大公約数です。")

kazu = tagainiso(a, b) 
print(kazu)

