#Wage calculator program

def get_float_input(prompt):

    while (True):
        try:
            float_value = float(input(prompt))

            #Do not allow 0 or negative values
            if float_value <= 0:
                print("Enter a value greater than 0")
                continue
        except ValueError as err:
            print("Please enter a number")
        else:
            break
            
    return float_value

def get_string_input(prompt):
    while True:
        string_value = input(prompt)

        #Do not allow an empty string
        if string_value == "":
            print("Please enter a value")
            continue
        else:
            break
        
    return string_value

def get_integer_input(prompt):
    integer_value = input(prompt)

    return integer_value
    
def main():

    while (True):
        
        #Ask user to input employee information
        #Get employee name
        emp_name = get_string_input("Enter employee name (first last): ")

        #Get employee gender
        emp_gender = get_string_input("Enter employee gender (m/f): ")
            
        #Get employee age
        #emp_age = get_integer_input("Enter employee age: ")

        #Get employee hours worked
        hours_worked = get_float_input("Enter hours worked: ")

        #Get employee pay rate
        pay_rate = get_float_input("Enter pay rate: ")

        #Calclate total pay
        total_pay = hours_worked * pay_rate

        #output name, gender, calculated rate
        print()
        print("Name:", emp_name)
        print("Gender:", emp_gender)
        #print("Age:", emp_age)
        print("Total Pay:", total_pay,"\n")

        #Ask user if they would like to enter more data
        do_again = input("Press 'y' to enter more data. Press any other key to exit: ")

        if do_again != "y":
            break
            
main()
