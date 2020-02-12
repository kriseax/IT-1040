#Wage calculator program

def get_float_input(prompt):
    while True:
        try:
            float_value = float(input(prompt))
            if float_value <= 0:
                raise ValueError("Negative or 0 values are not allowed")
        except ValueError as err:
            print(err)
        else:
            break
            
    return float_value

def get_string_input(prompt):
    while True:
        try:
            string_value = input(prompt)
            if string_value == "":
                raise ValueError("No input entered. Please enter the valid input")

            if "gender" in prompt and (string_value != 'm' and string_value != 'f'):
                raise ValueError("Gender input must be 'm' or 'f'")
        except ValueError as err:
            print(err)
        else:
            break

    return string_value

def get_integer_input(prompt):
    while True:
        try:
            int_value = int(input(prompt))
            if int_value <= 0:
                raise ValueError("Negative or 0 values are not allowed")    
        except ValueError as err:
            print(err)
        else:
            break
    
    return int_value
    
def main():

    loop_again = True
    while loop_again == True:
        
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
        total_pay = hours_worked * pay_rate

        #output name, gender, calculated rate
        print("Name:", emp_name)
        print("Gender:", emp_gender)
        print("Age:", emp_age)
        print("Total Pay:", total_pay,"\n")

        #Ask user if they would like to enter more data
        do_again = input("Press 'y' to enter more data. Press any other key to exit: ")

        if do_again != "y":
            loop_again = False
            
main()
