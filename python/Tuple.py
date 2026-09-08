elements=("char","int","float","double","string")
print("elements: ",elements)


#slicing elements


print("slicing of elements",elements[1:3])


#concatination

E2=(1,2,3)
print(f"After concatination:  {elements} {str(E2)}")


#sets

my_fruits={"mango","banana","apple"}
f_fruits={"orange","banana","cherry"}
print("union: ",my_fruits | f_fruits)
print("intersection: ",my_fruits & f_fruits)
print("difference: ",my_fruits - f_fruits)


#add new set value

my_fruits.add("greaps")
print(my_fruits)

#removing an elements
my_fruits.remove("apple")
print(my_fruits)

f_fruits.discard("guva")
print(f_fruits)

#tuple and set comparision

numbers=[1,2,3,4,5,6]
print(type(numbers))
print("lists: ",numbers)

#converting list into tuple

numbers2 =tuple(numbers)
print(type(numbers2))
print("tuple: ",numbers2)

#converting tuple into set

numbers3=set(numbers2)
print(type(numbers3))
print("set: ",numbers3)