import os
import shutil
import csv
import argparse

def rename_and_copy_jpg_files(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder with a '.jpg' extension
    files = sorted([f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f)) and f.lower().endswith('.jpg')])

    # Initialize variables
    csv_data = []

    for index, old_filename in enumerate(files, start=1):
        # Extract date part from the old filename
        date_part = old_filename[:8]

        # Generate the new filename
        new_filename = f"{date_part}_{index}.jpg"

        # Create new folder if it doesn't exist
        new_folder = os.path.join(output_folder, f"{date_part}")
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        # Copy the file to the new folder
        old_filepath = os.path.join(input_folder, old_filename)
        new_filepath = os.path.join(new_folder, new_filename)
        shutil.copy2(old_filepath, new_filepath)

        # Record the mapping in the CSV data
        csv_data.append([old_filename, new_filename])

    # Write CSV file
    csv_file_path = os.path.join(output_folder, "file_mapping.csv")
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Old Filename', 'New Filename'])
        csv_writer.writerows(csv_data)

if __name__ == "__main__":
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Rename and copy JPG files.')
    parser.add_argument('input_folder', help='Path to the input folder')
    parser.add_argument('output_folder', help='Path to the output folder')

    # Parse command line arguments
    args = parser.parse_args()

    # Call the function with the provided arguments
    rename_and_copy_jpg_files(args.input_folder, args.output_folder)
