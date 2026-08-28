gender = ("male", "female", "others", "male")  #tuples
print(gender.index("male"))
s={20,30,20}  #sets
print(s)

s1 ={1,2,3}
s2={3,4,5}
print(s1 | s2)  #union
print(s1 & s2)  #intersection
print(s1 - s2)
print(s1 ^ s2)    #symmetric

s={1,2,3,4}
s.add(4)
s.discard(10)
s.pop()

