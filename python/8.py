#trafic signals
signal= input("what's the color of signal: ")
if signal=="red":
    print("stop")
elif signal=="yellow":
    print("ready")
else:
    print("go! ")
#show the time of eating

time=(input("enter the present time: "))
if time=="9:00":
    print("it's time to eat breakfast")
elif time=="13:00":
    print("it's time to eat lunch")
elif time=="21:00":
    print("it's time to eat dinner")
else:
    print("it is not right time to eat anything")

    #boolen

att = 75
teacher_friend =True
if att>=75 or teacher_friend:
    print("eligible for exam")
else:
    print("no exam")

    #bus ticket
gender=input("enter gender: ")
age=int(input("enter passanger age: "))
if gender=="female":
    print("free ticket")
elif gender=="male":
    print("pay money for  ticket")
elif age<5:
    print("free ticket")
elif age<=12:
    print(" pay half ticket")
elif age>12:
    print(" pay full ticket")
else:
    print("ticket not found")