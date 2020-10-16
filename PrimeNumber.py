a=int(input("Enter number:"))

if a>1:
    for x in range(2,a):
        
        if(a%x)==0:
            
            print(a,"is not prime")

            break

    else:
        print(a,"is Prime")

else:
    print(a,"is not prime")
            
