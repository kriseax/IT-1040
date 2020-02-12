

def main():

    #Get employee hours worked
    hours_worked = float(input("Enter hours worked: "))

    #Get employee pay rate
    pay_rate = float(input("Enter pay rate: "))

    #Calclate total pay
    total_pay = hours_worked * pay_rate

    #output name, gender, calculated rate
    print("Total Pay:", total_pay,"\n")

main()
