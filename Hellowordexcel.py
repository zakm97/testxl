# Import necessary module
import os

def create_and_write_file(filename, text):
    # Open the file in write mode
    with open(filename, "w") as file:
        # Write the provided text to the file
        file.write(text)
    print(f"File '{filename}' created and text written successfully.")

# Define the filename and text
filename = "hello_world.txt"
text = "Hello, World!"

# Call the function to create the file and write the text
create_and_write_file(filename, text)