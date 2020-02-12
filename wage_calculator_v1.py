
def main():
    while (True):
        #Get employee hours worked
        try:
            hours_worked = float(input("Enter hours worked: "))

            #Do not allow 0 or negative values
            if (hours_worked <= 0):
                print("Enter a number greater than 0")
                continue
            
        except ValueError as err:
            print(err)
            continue

        #Get employee pay rate
        try:
            pay_rate = float(input("Enter pay rate: "))

            #Do not allow 0 or negative values
            if (pay_rate <= 0):
                print("Enter a number greater than 0")
                continue
            
        except ValueError as err:
            print("Please enter a number")
            continue

        #Calclate total pay
        total_pay = hours_worked * pay_rate

        #output name, gender, calculated rate
        print("Total Pay:", total_pay,"\n")

        do_again = input("Press 'y' to enter more data. Press any other key to exit ")

        if do_again != 'y':
            break

main()
