n = 5
count=1
for i in range(n+1) :
    for j in range(n,i,-1) :
        print(" ", end="")
    for k in range(i) :
        print(count," " ,end="")
        count+=1
    print()