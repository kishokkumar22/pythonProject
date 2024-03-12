n=5
m=3
for h in range(m) :
    for i in range(1,n+1) :
        for j in range(n,i,-1) :
            print(" ",end="")
        for k in range(i) :
            print("* ",end="")
        print()