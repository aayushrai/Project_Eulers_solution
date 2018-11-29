#find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
for num in range(0,1000):
    if num%3 or num%5:
        sum +=num

print(sum/2)