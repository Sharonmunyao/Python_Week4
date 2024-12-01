# Write initial content to the file (overwrite mode)
with open("newFile.txt", "w") as file:
    file.write("This is the content of the file above")

# Append additional content to the file (append mode)
with open("newFile.txt", "a") as file:
    file.write("\n This is added text \n")
print("File appended successfully")

# Read the content from the file (make sure to reopen for reading)
with open("newFile.txt", "r") as file:
    content = file.read()  # Read all the content into 'content'
    print(content)  # Print the current content of the file

# Modify the content
modified_content = content + "\n Is this how we modify our file? \n"

# Write the modified content to a new file (overwrite mode)
with open("VerynewFile.txt", "w") as new_file:
    new_file.write(modified_content)

print("Modified content written to VerynewFile.txt")




def read_file():
    # Ask the user for the filename
    filename = input("Please enter the filename you want to read: ")

    try:
        # Try to open the file
        with open(filename, "r") as file:
            # If successful, read and display the file's content
            content = file.read()
            print("\nFile Content:")
            print(content)

    except FileNotFoundError:
        # If the file does not exist, handle the error
        print(f"Error: The file '{filename}' does not exist.")
    
    except PermissionError:
        # If the file exists but we don't have permission to read it
        print(f"Error: You do not have permission to read the file '{filename}'.")
    
    except Exception as e:
        # For any other exception, print the error message
        print(f"An unexpected error occurred: {e}")

    else:
        print("File read successfully!")
    
    finally:
        print("Execution of file handling is complete.")

# Run the function
read_file()









