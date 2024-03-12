def fact(n) :
    if n==1 :
        return 1
    else :
       return n*fact(n-1)

n = int(input("Enter the factorial number : "))
#fact(n)
print("Factorial of",n,"is : ",fact(n))
