
x=90
bca=(80.5,85.0,91.0,95.0,90.0,73.0)
i=0
while i < len(bca):
    if x==bca[i]:
        print(f"{x} number is found at {i} index")
        break
    else:
        print(str(bca[i])," is not found at "+ str(i)+ " index")
    i+=1