square_sum = 0
sum_square = 0

for i in range(0,101):
    sum_square += i
    i = i**2
    square_sum += i

print(sum_square**2)
print(square_sum)
print(sum_square**2-square_sum)