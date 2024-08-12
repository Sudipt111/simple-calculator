math=int(input("enter the mark of math:" ))
english=int(input("enter the mark of english:" ))
science=int(input("enter the mark of science:" ))
social_science=int(input("enter the mark of social science:" ))
sanskrit=int(input("enter the mark of sanskrit:" ))
mil=int(input("enter the mark of mil:" ))

sum=int(math+english+science+social_science+sanskrit+mil)
print("total mark is: ",sum)

percentage=float(sum*100/600)
print("percentage: ",percentage)

if percentage>85.0:
    print("grade : A")
elif percentage<=85.0 and percentage>60.0:
    print("grade : B")
elif percentage>=45.0 and precentage<60.0:
    print("grade : C")
elif percentage<45.0:
    print("grade :D")