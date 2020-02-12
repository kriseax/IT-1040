

def main():
    while (True):
            
        #Get employee name
        emp_name = input("Enter employee name (first last): ")

        if (emp_name == ""):
            print("No input entered. Please enter the valid input \n")
            continue
            
        #Get employee gender
        emp_gender = input("Enter employee gender (m/f): ")

        if (emp_gender == "" or (emp_gender != "m" and emp_gender != "f")):
            print("Invalid gender. Enter 'm' or 'f' \n")
            continue
                            
        #Get employee age
        try:
            emp_age = int(input("Enter employee age: "))
            if (emp_age <= 0):
                print("Negative or 0 values are not allowed \n")
                continue
        except ValueError as err:
            print(err)
            continue
        
        #Get employee hours worked
        try:
            hours_worked = float(input("Enter hours worked: "))
            if (hours_worked <= 0):
                print("Negative or 0 hours worked is not allowed \n")
                continue
        except ValueError as err:
            print(err)
            continue
        
        #Get employee pay rate
        try:
            pay_rate = float(input("Enter pay rate: "))
            if (pay_rate <= 0):
                print("Negative or 0 pay rate is not allowed \n")
                continue
        except ValueError as err:
            print(err)
            continue
        
        #Calclate total pay
        total_pay = hours_worked * pay_rate

        #output name, gender, calculated rate
        print("\nName:", emp_name)
        print("Gender:", emp_gender)
        print("Age:", emp_age)
        print("Total Pay:", total_pay,"\n")

        #Ask user if they would like to enter more data
        do_again = input("Press 'y' to enter more data. Press any other key to exit: ")

        if do_again != "y":
            break

main()
