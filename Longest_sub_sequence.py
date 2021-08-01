A=[3,1,8,2,5]
Lis={}
max_size=0
while A:
    temp=A[0]
    Lis[temp] = []
    for elements in A:

        if(elements>temp):
            Lis[temp].append(elements)
    if(len(Lis[temp])>max_size):
        max_size=len(Lis[temp])
    A.pop(0)

print(max(Lis.items(), key=lambda x:len(x[1])),max_size)
