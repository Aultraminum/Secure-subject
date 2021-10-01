N = 18
e = 9007 #public key
cipher = 16765951
import math
j = 0
i = 2
A = []
while i < math.sqrt(N):
    if N%i == 0:
        p = int(i)
        A.append(p)
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
print(A)