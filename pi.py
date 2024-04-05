text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
taxt = text.replace(","," ")
word_list = taxt.split()

list_1=list(map(len, word_list))

count=0
ans = 0
for i in list_1:
    ans+=i*0.1**(count)
    count+=1
    
print (ans)
