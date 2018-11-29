



def amacibal_num(i):
    Sum = 0
    for k in range(1, i):
        if i % k == 0:
            Sum += k
    return Sum



if __name__ == "__main__":
       total_sum = 0
       for i in range(2,10000):
           ans=amacibal_num(i)
           sec = amacibal_num(ans)
           if i != ans:
               if sec==i :
                   if ans<10000:
                     total_sum+=ans
                     print(ans)
                   else:
                       break


print(total_sum)
