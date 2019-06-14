for r in range(5):
    print("")
    for c in range(5):
        if(r==0 or r==4):
            print("*",end="")
        elif(c==2):
            print("*",end="")
        else:
            print(" ",end="")
