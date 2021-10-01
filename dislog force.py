
X = 7
g = 5
P = 23
i = 1

while i < P:
    temp = pow(g, i, P)
    if X == temp:
        print(i)
        break
    i = i +1

X2 = 43
g2 = 587
P2 = 9001
i2 = 1

while i2 < P2:
    temp2 = pow(g2, i2, P2)
    if X2 == temp2:
        print(i2)
        break
    i2 = i2 + 1
