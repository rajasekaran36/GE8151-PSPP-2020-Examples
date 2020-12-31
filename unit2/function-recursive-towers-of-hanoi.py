def hanoi(n,source,destination,aux):
    if(n==1):
        print("move disk 1 from "+source+" to "+destination)
        return
    hanoi(n-1,source,aux,destination)
    print("move disk "+str(n)+" from "+source+" to "+destination)
    hanoi(n-1,aux,destination,source)


hanoi(25,"S","D","A")