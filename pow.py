import math
from math import ceil 
from math import floor 
from math import sqrt

N = 90668363
e = 9007 #public key
cipher = 16765951
j = 0
i = 2

while i < math.sqrt(N):
    if N%i == 0:
        p = int(i)
        break
    i = i+1
    j = j+1
q = int(N/p)

print(p)
print(q)
def eea(a, b): #Extended Euclidian Algorithm
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t

def inv(n, p):
    gcd, x, y = eea(n, p)
    assert (n * x + p * y) % p == gcd
    if gcd != 1:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
        '{} has no multiplicative inverse '
        'modulo {}'.format(n, p))
    else:
        return x % p

d = inv(e, (p-1)*(q-1))
print(d)

m=pow(cipher,d,N)
print(m)

c=pow(m,e,N)
print(c)

print(j)

def Expmod(c,d,N):
    m = 1
    while d >= 1:
        if d % 2 == 1 :
            m = (m * c) % N
            c = (c ** 2) % N
            d = math.floor(d/2)
        d = d - 1
    print(m)
    return(m)

print(Expmod(cipher, d, N))