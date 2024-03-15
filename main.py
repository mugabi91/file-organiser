import os 
import shutil


def organize_directory(directory):
   
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip if the item is not a file
        if not os.path.isfile(filepath):
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        
        # Skip if the file extension is empty
        if not file_extension:
            continue

        # Define the destination directory based on the file type
        destination_directory = os.path.join(directory, file_extension.lower()[1:] + 's')
        
        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Move the file to the destination directory
        shutil.move(filepath, os.path.join(destination_directory, filename))
        
    print(" DIR ORGANISED")


while True:
    directory_to_scan = input('Enter path to directory you want organized: ')
    try:
        # Validate the directory path
        if not os.path.isdir(directory_to_scan):
            raise ValueError("Invalid directory path")
        break  # Break out of the while loop if the directory path is valid

    except ValueError as e:
        print("Error:", e)
        # Handle the error (e.g., ask for input again, exit the program, etc.)





if __name__ ==  "__main__":
    organize_directory(directory_to_scan)
