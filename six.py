multiples=[1,2,3,4,5,6,7,8,9,10]
num=int(input('enter num : '))

output=list(map(lambda number:number*num,multiples))
print(output)