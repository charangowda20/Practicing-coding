num=[1,2,3,4,5,6,7,8,9,10]
print(num)
#insert
num.insert(10,11)
print(num)
#pop removing last element or indexing element
num.pop()
print(num)
num.pop(9)
print(num)
#append addding element at the last
num.append(10)
print(num)
#removing the element
num.remove(10)
print(num)
#modify the element
num[0]=0
print(num)
#slicing
print(num[:8:2])
print(num[5:])
#sorting 
number=[22,1,55,8,6,88,4,4,]
sn=(sorted(number))
print(sn)
print(sum(number))
#revercing the elements
sn.reverse()
print(sn)