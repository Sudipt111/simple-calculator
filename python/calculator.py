print("This is a simple calculator")
print("Choose the respective no u want to perform operation")
print("Enter 1 for addion \nEenter 2 for subtraction \nEnter 3 for multiplication \nEnter 4 for division \nEnter 5 for percentage ")
number=int(input("Choose the number: "))
match number:
    case 1:
        first_number=float(input("Enter the 1st number: " ))
        second_number=float(input("Enter the 2nd number: " ))
        addition=first_number+second_number
        print("the result is :",addition)
    case 2:
        first_number=float(input("Enter the 1st number: " ))
        second_number=float(input("Enter the 2nd number: " ))
        subtraction=first_number-second_number
        print("the result is :",subtraction)
    case 3:
        first_number=float(input("Enter the 1st number: " ))
        second_number=float(input("Enter the 2nd number: " ))
        multiplication=first_number*second_number
        print("the result is :",multiplication)
    case 4:
        first_number=float(input("Enter the divident: " ))
        second_number=float(input("Enter the divisor: " ))
        division=first_number/second_number
        print("the result is :",division)
    case 5:
        first_number=int(input("Enter the total number: " ))
        second_number=int(input("Enter the secured number: " ))
        percentage=float(second_number*100/first_number)
        print("the result is: ",percentage)