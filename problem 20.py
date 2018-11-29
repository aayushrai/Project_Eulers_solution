n=100
result = 1
for i in range(1,n+1):
    result *= i

print(result)

final = 0
while(int(result) != 0):
    right_digit = result % 10
    result /= 10
    final += int(right_digit)

print(final)

import math
n = 100
print(sum(map(int, str(math.factorial(n)))))