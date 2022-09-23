def solution(n, k):
    def func(n,q):
        rev_base =''
        
        while n>0:
            n,mod = divmod(n,q)
            rev_base += str(mod)
        return rev_base[::-1]
    
    def is_prime_number(x): 
        if x == 1:
            return False
        for i in range(2,x):
            if x%i==0:
                return False
        return True
    
    number = func(n,k)
    count =0
    
    for i in number.split('0'):
        if i =="":continue
        a = int(i)
        if is_prime_number(a) == True:
            count +=1
    
    answer = count
    return answer