fruits = ["orange" , "kiwi", "mango" ,"apple" , "pineapple"]
print(fruits)
print(fruits[0])            #index
fruits[1] = "cherry"        #modifying
print(fruits)
fruits.append(" banana")    #append

print(fruits)
fruits.insert(2, "graps")   #insert
print(fruits)
fruits.remove("mango")      #remove()
print(fruits)
fruits.pop()                #pop()
print(fruits)
print(fruits[0:2])          #slicing
print(fruits[3::])
print(fruits[::3])
print(len(fruits))          #length function
print(sorted(fruits))       #sorted()
number = [1,2,3,1,3,3,3]
print(sum(number))          #sum
print(fruits.index("pineapple"))#index element
print(number.count(3))       #count
number.reverse()             #reverse
print(number)                
matrix = [ [ 1,2,3], [4,5,6], [7,8,9]]   #matrix
print(matrix[1][2])
print(matrix[2])