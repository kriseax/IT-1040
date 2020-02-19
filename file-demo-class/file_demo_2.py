#This program will read the contents of students.txt and
#write them to output.txt

try:
    #Create file objects
    #Open students file in read mode
    my_file = open("students.txt", "r")
    #Open output file in write mode. This will overwrite any contents in the file
    output_file = open("output.txt", "w")

    #Read students file line by line
    for line_of_text in my_file:

        #Write the line that was just read into the output file
        output_file.write(line_of_text)

    #Close the files
    my_file.close()
    output_file.close()

#Print any error messages in an exception occurs
except Exception as err:
    print(err)

#Always check if the files are closed
#The finally block will always execute
#So if an exeption occurs we can close the file
finally:
    if "my_file" in locals() and not my_file.closed:
        my_file.close()

    if "output_file" in locals() and not output_file.closed:
        output_file.close()
        
    print("We are done")
