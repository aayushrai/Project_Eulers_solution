def reverse_int(number):
    result = 0
    while(int(number)!=0):
        right_digit=number%10
        number/=10
        result = int(result*10+right_digit)
    return result

if __name__ == "__main__":
     palindromic = 0
     for i in range(100,1000):
         for j in range(100,1000):
             product = i*j
             if product == reverse_int(product):
                 if palindromic<product:
                    palindromic = product
     print(palindromic)