#sum of numbers 
num=[5,10,1,35,15,20,25]
print(sum(num))

#counting the elements
print(len(num))

#finding largest number 

highest=num[0]
for i in num:
    if i>highest:
        highest=i
print("highest number is: ",highest)

#finding the lowest value
lowest=num[0]
for n in num:
    if n<lowest:
        lowest=n
print("lowest value is: ",lowest)