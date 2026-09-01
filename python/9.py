#while loop
pin="1234"
trails=1
while trails<=3:
    input_pin= input(f"trail-{trails} pin>> ")
    trails +=1
    if input_pin==pin:
        print("corret")
        break
    else:
        print("incorrect")
print("please try again after 10 mints")