try:
    #Create file object
    my_file = open("students.txt", "r")

    #Read file line by line
    for line_of_text in my_file:
        #Split each line at the commas
        #Individual values from the line will be stored in a list (line_items)
        line_items = line_of_text.split(",")

        #Assign each item from the line_items list to a variable
        stu_name = line_items[0]
        num1 = int(line_items[1])
        num2 = int(line_items[2])
        num3 = int(line_items[3])
        
        #Calcuate the average
        avg = (num1 + num2 + num3)/ 3
        
        #Print output
        print(stu_name+": ", avg)

    #Close the file
    my_file.close()

#Print any error messages in an exception occurs        
except Exception as err:
    print(err)

#Always check if the files are closed
#The finally block will always execute
#So if an exeption occurs we can close the file
finally:
    if ("my_file" in locals()) and (not my_file.closed):
        my_file.close()
        
    print("We are done")
