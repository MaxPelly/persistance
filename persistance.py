import math
total = 40000

def persistance(num):
    if num < 10:
        return 0
    result = 1
    for digit in str(num):
        result *= int(digit)
    return persistance(result) + 1
    
max_per = 0    
while True:
    print(f'starting {total}')
    for i in range(total + 1):
        for j in range(total - i + 1):
            k =  total - i - j
            num = 2**i * 3**j * 7**k
            if '0' in str(num):
                per = 1
            else:
                per = persistance(num)
            if per > max_per:
                max_per = per
                print(f"2^{i}  * 3^{j} * 7^{k}, {per+1}")
            
            if i != 0: 
                num = 5**i * 3**j * 7**k
                if '0' in str(num):                                                                                                                          
                    per = 1                                                                                                                                
                else:                                                                                                                                      
                    per = persistance(num)
                if per > max_per:
                    max_per = per
                    print(f"3^{j}  * 5^{i} * 7^{k}, {per+1}")
    total += 1
