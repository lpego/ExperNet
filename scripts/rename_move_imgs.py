# # %%
import os
import csv
from datetime import datetime

def rename_and_move_files(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize variables for CSV data
    csv_data = []

    # Iterate over files in the input folder
    for index, filename in enumerate(sorted(os.listdir(input_folder))):
        if filename.endswith(".jpg"):
            # Extract date from the filename
            date_str = filename[:8]
            date_format = "%d%m%Y"
            date_object = datetime.strptime(date_str, date_format)

            # Create new filename with sequential number
            new_filename = f"{date_str}_{index + 1}.jpg"

            # Create new folder based on the pattern DDMMYYYY_HHmmss
            new_folder_name = date_object.strftime("%d%m%Y_%H%M%S")
            new_folder_path = os.path.join(output_folder, new_folder_name)

            # Create the new folder if it doesn't exist
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            # Build the full path for the new file
            new_file_path = os.path.join(new_folder_path, new_filename)

            # Move the file to the new folder
            os.rename(os.path.join(input_folder, filename), new_file_path)

            # Append data to CSV
            csv_data.append((filename, new_filename))

    # Write CSV file
    csv_file_path = os.path.join(output_folder, "filename_remapping.csv")
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Old Filename", "New Filename"])
        csv_writer.writerows(csv_data)

    print(f"Files renamed and moved successfully. CSV file created at: {csv_file_path}")

# # Replace 'input_folder_path' and 'output_folder_path' with your actual paths
# input_folder_path = 'D:\ExperNet\data\memoria 20b'
# output_folder_path = 'D:\ExperNet\data\moved'

# rename_and_move_files(input_folder_path, output_folder_path)

# %%
import os
import csv
from datetime import datetime
import shutil

def rename_and_copy_files(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize variables for CSV data
    csv_data = []

    # Iterate over files in the input folder
    for index, filename in enumerate(sorted(os.listdir(input_folder))):
        if filename.endswith(".jpg"):
            # Extract date from the filename
            date_str = filename[:8]
            date_format = "%d%m%Y"
            date_object = datetime.strptime(date_str, date_format)

            # Extract time from the filename 
            time_str = filename[-14:-4]
            time_format = "%H%M%S"
            time_object = datetime.strptime(time_str, time_format)

            # Create new filename with sequential number and formatted time
            new_filename = f"{date_str}_{index + 1}.jpg"

            # Create new folder based on the pattern DDMMYYYY_HHmmss
            new_folder_name = date_object + "_" + time_object
            new_folder_path = os.path.join(output_folder, new_folder_name)

            # Create the new folder if it doesn't exist
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
            
            # Build the full path for the new file
            new_file_path = os.path.join(new_folder_path, new_filename)
           
            # Copy files to the new folder
            shutil.copy2(os.path.join(input_folder, filename), new_file_path)

            # Append data to CSV
            csv_data.append((filename, new_filename))

    # Write CSV file
    csv_file_path = os.path.join(output_folder, "filename_remapping.csv")
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Old Filename", "New Filename"])
        csv_writer.writerows(csv_data)

    print(f"Files renamed and moved successfully. CSV file created at: {csv_file_path}")

# Replace 'input_folder_path' and 'output_folder_path' with your actual paths
input_folder_path = 'D:\ExperNet\data\memoria 20b'
output_folder_path = 'D:\ExperNet\data\moved_2'

rename_and_copy_files(input_folder_path, output_folder_path)

# %%
