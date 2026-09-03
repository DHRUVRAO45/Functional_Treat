def Display_Data_Summary(a):
    print("- Data Summary :- ")
    print("- Total elements : ",len(a))
    print("- Minimum value : ",min(a))
    print("- Maximum value : ",max(a))
    print("- Sum of all values : ",sum(a))
    print("- Average value : ",sum(a)/len(a))

def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)

def Dataset_Statistics(a):
    print("- Dataset Statistics :- ")
    print("- Minimum value : ",min(a))
    print("- Maximum value : ",max(a))
    print("- Sum of all values : ",sum(a))
    print("- Average value : ",sum(a)/len(a))
    

print("Welcome to the Data Analyzer and Transformer Program")
print("")
print("Main Menu :")
print("1. Input Data")
print("2. Display Data Summary (Built-in Functions")
print("3. Calculate Factorial Recursion")
print("4. Filter Data by Threshold (Lambda Function)")
print("5. Sort Data")
print("6. Display Dataset Statistics (Return Multiple Values)")
print("7. Exit Program")
print("")


while True:

   

    print("------------------------------------------------------------------------")
    num=int(input("Please enter your choice : "))
    print("------------------------------------------------------------------------")

    if num==1:
        print("")
        b=input("Enter data for a 1D array (separated by spaces) : ").split()
        a=[]
        for i in b:
            a.append(int(i))
        print("Data has been stored Successfully !")
        print("")

    if num==2:
        print("")
        Display_Data_Summary(a)
        print("")
    
    if num==3:
        print("")
        b=int(input("Enter a number to calculate its factorial : "))
        print("Factorial of ",b,"is : ",factorial(b))
        print("")
        
    if num==4:
        print("")
        y=int(input("Enter a threshold value to filter out data above this value : "))
        print(f"Filtered Data (values >= {y}) : ")
        print(list(filter(lambda x:x>=y,a)))
        print("")

    if num==5:
        print("")
        print("Choose sorting option : ")
        print("1. Ascending")
        print("2. Descending")
        print("")

        d=int(input("Enter your choice : "))
        if d==1:
            print("")
            print("shorted data in Ascending Order : ")
            print(list(sorted(a,reverse=False)))
            print("")
        else:
            print("shorted data in Descending Order : ")
            print(list(sorted(a,reverse=True)))
            print("")
            
    if num==6:
        print("")
        Dataset_Statistics(a)
        print("")

    if num==7:
        print("")
        print("Thank you for using the Data Analyzer and Transformer Program.")
        print("Goodbye !")
        break