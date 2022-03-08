f1=open("in.txt","r")
n1=int(f1.readline())
n2=int(f1.readline())
for j in range(n1,n2+1,1):
    for i in range(1,11,1):
        print(j,"*",i,"=",j*i)
    print()
       
    
