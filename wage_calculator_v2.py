#Wage calculator program

def get_float_input(prompt):
            
    return 

def get_string_input(prompt):
   
    return 

def get_integer_input(prompt):
    
    return 
    
def main():

    while (True):
        
        #Ask user to input employee information
        #Get employee name
        emp_name = get_string_input("Enter employee name (first last): ")

        #Get employee gender
        emp_gender = get_string_input("Enter employee gender (m/f): ")
            
        #Get employee age
        emp_age = get_integer_input("Enter employee age: ")

        #Get employee hours worked
        hours_worked = get_float_input("Enter hours worked: ")

        #Get employee pay rate
        pay_rate = get_float_input("Enter pay rate: ")

        #Calclate total pay
        #total_pay = hours_worked * pay_rate

        #output name, gender, calculated rate
        print("Name:", emp_name)
        print("Gender:", emp_gender)
        print("Age:", emp_age)
        print("Total Pay:", total_pay,"\n")

        #Ask user if they would like to enter more data
        do_again = input("Press 'y' to enter more data. Press any other key to exit: ")

        if do_again != "y":
            break
            
main()
