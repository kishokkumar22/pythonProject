num = [0,1,0,4,7,14]
num2 = sorted(num)
count = num2.count(0)
for i in range(count) :
    num2.remove(0)
for j in range(count) :
    num2.append(0)
print(num2)