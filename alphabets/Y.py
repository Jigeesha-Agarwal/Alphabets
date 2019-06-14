j=4
for r in range(5):
    print("")
    for c in range(5):
        if(r==c and c<=2):
            print("*",end="")
        elif(c==j and j>2):
            print("*",end="")
            j=j-1
        elif(c==2 and r>=2):
            print("*",end="")
        else:
            print(" ",end="")
