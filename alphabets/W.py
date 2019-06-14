j=6
for r in range(3):
    print("")
    for c in range(7):
        if (r==c or (r==1 and c==3)):
            print("*",end="")
        elif(c==j):
            j-=1
            print("*",end="")
        else:
            print(" ",end="")
