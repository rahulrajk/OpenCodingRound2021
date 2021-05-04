def getReport(V,B,n):
    k = 0
    count = 0
    for i in range(len(V)):
        if k>=len(B):
            break
        else:
            if V[i] == B[k]:
                k=k+1
                count = count+1
    if count == len(B):
        return "POSITIVE"
    else:
        return "NEGATIVE"            

V = input()
V = list(V)
n = int(input())
for i in range(n):
    B = input()
    print(getReport(V,list(B),n))

# coronavirus
# 3
# abcde
# crnas
# onarous