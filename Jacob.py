import math
import random

def Fermat(a,N):
    if a >= 2 and a <= N-1 :
        if a**(N - 1) % N != 1 % N :
            print("N is composite")
        else:
            print("N is Prime")
    else:
        print("Nope!")



def Jacob(m,n):
    if m == 1 :
        return 1
    elif m % 2 == 0 :
        if (((n**2 - 1) / 8) % 2) == 0 :
            return Jacob(m/2,n)
        else :
            return -Jacob(m/2,n)
    elif (((m-1) * (n-1) / 4) % 2) == 0 :
        return Jacob(n % m,m)
    else :
        return -Jacob(n % m,m)

def solovay_strassen(n, k=10):  
     if n == 2 or n == 3:  
         return True  
     if not n & 1:  
         return False  
           
     for i in range(k):  
         a = random.randrange(2, n - 1)       # choose any random number from 1 to (n-1)  5
         x = Jacob(a, n)                     # find n's jacobi number  
           
         y = pow(a, int((n - 1) / 2), n)           # calculate legendre symbol from euler criterion formula  
         if y != 1 and y != 0:                          
             y = -1  
         
         if (x == 0) or (y != x):             # if jecobi and eular criterion formula are not same (y != x) then the number is not prime  
             return False         
     return True  

def FermatCom(N):
    x = math.ceil(math.sqrt(N))
    n = 0
    y = 0

    while (y != math.ceil(y) and y != math.floor(y) or y == 0):  
        y = math.sqrt((x**2) - N)
        x = x + 1      
        print(y)
    
    x = x - 1
    print(x)
    n = (x + y) * (x - y)
    print(n)

print(Jacob(2,77))

n = int(input('\nEnter number : '))      # enter number for check it's primality  

if n <= 1 :                                          
     print('Number must be >=2')  
elif(solovay_strassen(n,10)):  
     print (str(n) + ' is Prime!')  
else:  
     print (str(n) + ' is not Prime!')  

FermatCom(15770708441)