a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
def euclid(c, d):
    c = int(c)
    d = int(d)
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
        return "互いに素です。"
    else:
        return "互いに素ではありません"

number = euclid(a, b)
print(number, "が最大公約数です。")

kazu = tagainiso(a, b) 
print(kazu)
