def primitiveroot(a,d):
    #b = d-1
    #A = [ ]
    #i = 2
    #while i <= b :
        #if b%i == 0 :
            #b = b/i
            #A.append(i)
        #else :
            #i = i+1
    #temp = loop(a,d,A)
    temp = 0
    for i in range(1,d-1) :
        if (a**i)%d == 1 :
            temp = 1
            break
    if temp == 1 :
        print(str(a)+" is not primitive root of "+str(d))
    else :
        print(str(a)+" is primitive root of "+str(d))
    #return A
primitiveroot(6,7)
primitiveroot(8,11)
primitiveroot(6,17)
primitiveroot(6,19)
primitiveroot(11,137)
primitiveroot(8,179)
primitiveroot(1551,9001)