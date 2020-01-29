
def validate_user_pass(user_input, min_length, max_length):
    input_length = len(user_input)
    if input_length >= min_length and input_length <= max_length:
        return True
    else:
        return False
 
invalid_input = True

while invalid_input:
    
    #Get User input
    user_name = input("Please enter your user name: 4 - 16 characters ")

    password = input("Please enter your user email. 6 - 12 characters: ")

    #Validate user_name
    valid_user = validate_user_pass(user_name, 4, 16)

    #Validate password with the validate function
    valid_pass = validate_user_pass(password, 6, 12)

    #Check if both username and password are valid
    #If both not valid ask user to enter them again
    if valid_user and valid_pass:
        invalid_input = False
        print("Valid username and password. Thank you", user_name, "\n")
    else:
        invalid_input = True
        print("Invalid username or password. \n")

    
