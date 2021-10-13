
a = int(input('enter a value :'))
b = int(input('enter b value :'))
def add(a, b):
    print("Sum : ", a+b)


def sub(a, b):
    print("Sub : ",a-b)


def mul(a, b):
    print("Mul : ",a*b)


def div(a, b):
    if a > b:
        print("A%B :",a//b)
    else:
        print("B%A :", b // a)


add(a, b)
sub(a, b)
mul(a, b)
div(a, b)



