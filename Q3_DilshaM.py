start=int(input("Enter the 1st number:"))
end=int(input("Enter the 2nd number:"))
l=[]
for i in range(start,end+1):
    flag =0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        l.append(i)
print("prime number is:",l)
print("Total:",sum(l))