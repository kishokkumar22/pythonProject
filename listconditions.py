numbers = [12,75,150,180,145,525,50]


for i in range(len(numbers)) :
    if numbers[i] % 5 == 0:
        if numbers[i] <= 150:
            print(numbers[i])
        if numbers[i] >= 500:
           break

