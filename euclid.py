a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a=int(a)
b=int(b)

def euclid(c,d):
    if c<d:
        c,d = d,c #c,dを入れ替える
    
    kari = 0
    while d!=0:
        kari = c%d
        c=d
        d=kari
        
    return c

number = euclid(a,b)
print(number,"が最大公約数です。")