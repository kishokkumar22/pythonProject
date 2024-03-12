a = []
n = int(input("Enter the limit : "))
for i in range(1,n+1):
    b = int(input("Enter the "+str(i)+ " value : "))
    a.append(b)
print(max(a))
print(min(a))
