num=int(input("enter num : "))

if num==0:
    print("composite number")
elif num<0:
    print("invalid input")
else:
    if num%2==0:
        print("PRIME")
    else:
        print("NOT PRIME")