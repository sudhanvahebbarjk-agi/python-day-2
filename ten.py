def CheckLeap(year):
    if((year%400==0) or
    (year % 100!=0) and
    (year%4==0)):
        print("given year is a leap year")
    else:
        print("given year is not leap year")

year=int(input("enter year : "))

CheckLeap(year)