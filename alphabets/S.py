for r in range(5):
    print("")
    for c in range(3):
        if(r==0 or r==2 or r==4):
            print("*",end="")
        elif(r==3 and c==2 ) :
            print("*",end="")
        elif(r==1 and  c==0):
            print("*",end="")
        else:
            print(" ",end="")

    
            
