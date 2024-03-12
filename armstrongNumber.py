def amstrong() :
    a=int(input("Enter the number  : "))
    number1=a
    sum,rem, cube = 0,None,None

    while number1!=0 :
        rem = number1%10
        cube = rem*rem*rem
        sum = sum+cube
        number1=number1//10

    if sum==a :
        print(a,"is an armstrong number")
    else : print(a,"is not an armstrong Number")

amstrong()