num=int(input("Enter the number of rows:"))
for i in range(num):
    value =i+1
    dec=num-1
    for j in range(i+1):
        print(format(value,"<4"),end=' ')
        value =value+dec
        dec=dec-1
    print()
