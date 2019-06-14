j=4
i=0
for r in range(5):
    print("")
    for c in range(5):
        if(c==2 and r==2):
            j=j-1
        if(r==c):
            print("*",end="")
        elif(c==j):
            j=j-1
            print("*",end="")            
        else:
            print(" ",end="")
        
