print("press 1 for cross product\n"
      "press 2 for perpendicular")
Choice = int(input("enter Choice(1,2)="))
if Choice == 1:     
    a1=int(input("enter a1="))
    a2=int(input("enter a2="))
    a3=int(input("enter a3="))
    b1=int(input("enter b1="))
    b2=int(input("enter b2="))
    b3=int(input("enter b3="))

    a=(a2*b3-a3*b2)
    b=-(a1*b3-a3*b1)
    c=+(a1*b2-a2*b1)

    print("the cross product is=",(a,b,c))

elif Choice == 2:
    #dotprodect
#now X⊥Y if and only if x.y =0

    a1=int(input("enter a1="))
    b1=int(input("enter b1="))
    c1=int(input("enter c1="))

    a2=int(input("enter a2="))
    b2=int(input("enter b2="))
    c2=int(input("enter c2="))

    dotproduct= a1*a2+b1*b2+c1*c2
    print("the dotproduct is :",dotproduct)

    print("press 1 for 'Yes'")
    print("press 2 for 'No'")

    n=int(input("if you want to know this vector are perpadcular each other so entre 'yes' otherwise 'no'= "))

    if n == 1:
        if  dotproduct == 0:
            print("Yes, this vecoter is perpendicular to each other")
        else:
            print("No, this vecoter is not perpendicular to each other")
    else:
       print("_____x_____")
else:
    print("wrong input")