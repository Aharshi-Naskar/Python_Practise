print("-------COMPOUND INTEREST CALCULATOR SOFTWARE---------")

User_Choice= input("Do you want this software to work?(yes/no):")

if User_Choice=="yes":
 print("You agree to terms and conditions, software has begun")

 User_input=input("Are you a banker , or a common man?(banker/man):")

 if User_input =="banker":
    principal = int(input("Enter the principal to calculate:"))
    rate=int(input("Enter the rate percent "))
    time = int(input("Enter the specific time:"))
    Amount=principal*(100+rate)/100**time
    CI=Amount-principal
    print(f"Your Compound Interest is:",CI)

 elif User_input=="man":
     principal2 = int(input("Enter the principal to calculate:"))
     rate2 = 5
     print("Specified rate is 5%")
     time = int(input("Enter the specific time:"))
     Amount2= principal2*(100+rate2)/100**time
     CompoundInt=Amount2-principal2
     print(f"Your Compound Iterest is:",CompoundInt)

 else:
    print("Please enter a valid word")