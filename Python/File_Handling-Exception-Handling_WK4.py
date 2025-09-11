def process_file():
    # Ask user for the file to read
    filename = input("Enter the filename to read: ")

    try:
        # Open the file safely
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified = modify_content(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified)

        print(f" File processed successfully! Modified version saved as '{new_filename}'")

    except FileNotFoundError:
        print(" Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")
# Run the program
process_file()
