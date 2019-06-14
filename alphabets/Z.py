i=1
j=4
for r in range(0,6):
    for c in range(0,6):
        if (r==0 or r==5):
            print("*",end="")
        elif r==i and c==j:
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print("")
