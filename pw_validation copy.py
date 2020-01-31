
def validate_user_pass(user_input, min_length, max_length):
    input_length = len(user_input)
    if input_length >= min_length and input_length <= max_length:
        return True
    else:
        return False

def score_to_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def avg_student_scores(score_list):
    sum = 0
    for index in range(len(score_list)):
        sum += score_list[index]

    avg = sum / len(score_list)

    return int(avg)
 
def main():

    invalid_input = True
    
    while invalid_input:
        
        #Get User input
        user_name = input("Please enter your user name (4 - 16 characters): ")

        password = input("Please enter your password (6 - 12 characters): ")

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

    #Ask user how many students they have to enter
    num_students =  input("Please enter number of students to enter grades for: ")
    #Get students and scores. Store in arrays
    student_array = []
    scores_array = []
    letter_grades_array = []

    for counter in range(int(num_students)):
        stu_name = input("\nEnter student name: ")
        stu_score = input("Enter student score: ")

        #Add items to arrays
        student_array.append(stu_name)
        scores_array.append(int(stu_score))
                        
    #Convert scores to letter grades. Write a function to do this
    for index in range(len(scores_array)):
        letter_grades_array.append(score_to_letter(scores_array[index]))
    
    #print student names, scores, letter grade
    print()
    for index in range(len(scores_array)):
        print(student_array[index]+":", scores_array[index], "-->",letter_grades_array[index])

    #calculate average student score
    student_avg = avg_student_scores(scores_array)

    print()
    print("Average Score:", student_avg, "-->", score_to_letter(student_avg))
    
    #print(student_array)
    #print(scores_array)
    
if __name__ == "__main__":
    main()
