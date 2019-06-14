j=6
for r in range(4):
    print("")
    for c in range(7):
        if(r==c):
            print("*",end="")
        elif(c==j):
            j-=1
            print("*",end="")
        else:
            print(" ",end="")
