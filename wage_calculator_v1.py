

def main():
    #Get employee name
    emp_name = input("Enter employee name (first last): ")

    #Get employee gender
    emp_gender = input("Enter employee gender (m/f): ")
                    
    #Get employee age
    emp_age = int(input("Enter employee age: "))

    #Get employee hours worked
    hours_worked = float(input("Enter hours worked: "))

    #Get employee pay rate
    pay_rate = float(input("Enter pay rate: "))

    #Calclate total pay
    total_pay = hours_worked * pay_rate

    #output name, gender, calculated rate
    print("Name:", emp_name)
    print("Gender:", emp_gender)
    print("Age:", emp_age)
    print("Total Pay:", total_pay,"\n")

main()
