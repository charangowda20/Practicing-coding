#for loop
# multiplication
for j in range(1,31):
    print(f"3 X {j} = {j*3}")
    #print("")

# addition
for n in range(1):
    for m in range(11):
        print(f"{m} + {n} = {m+n}")

# printing letter by name
name= "charan"
for letter in name:
    print(letter)

# finding vowels
vowels=('a','e','i','o','u')
for word in name:
    if word == vowels:
        print(word)