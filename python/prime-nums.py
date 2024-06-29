def isPrime(M):
    sqrtM = int(M**(1/2))
    for I in range(2,sqrtM+1):
        if M % I == 0:
            return False 
    return True 

R = int(input())
for N in range(2,R+1):
    if(isPrime(N)):
        print(N,end=' ')