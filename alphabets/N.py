for r in range(5):
    print("")
    for c in range(7):
        if (r==c):
            print("*",end="")
        elif(c==0 or c==4):
            print("*",end="")
        else:
            print(" ",end="")
