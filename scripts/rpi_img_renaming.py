# %% 
import os
from pathlib import Path
import glob
import re

# %% 
path = Path('D:\ExperNet\data\memoria 20b')

# %% 
file_list = os.listdir(path)

# %%
# ### File format: 
# DDMMYYYYHHmmss.jpg
# 22 10 2023 18 00 01 .jpg
# for example: 
# 23102023060003.jpg
# 23102023060004.jpg

# %% 
# ### input format
# 23102023060003.jpg
# ### target output format
# 20231023_060003_frame000000001.jpg

# %%
ffmpeg 25 -i 20231023_060003_frame%05d.jpg output

### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ###

# %%
import re

filename = "23102023060003.jpg"

# Define a regular expression pattern
pattern = re.compile(r'(\d{2})(\d{2})(\d{4})(\d{2})(\d{2})(\d{2})')

# Use the pattern to match the filename
match = pattern.match(filename)

# Extract date and time components
day, month, year, hour, minute, second = match.groups()

# Format the date and time strings
date_str = f"{day}{month}{year}"
time_str = f"{hour}{minute}{second}"

# Print the results
print("Date:", date_str)
print("Time:", time_str)

### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ### 

# %% 

new_filename = date_str + "_" + time_str + "%03d.jpg"
new_filename

# %%
import re

def extract_date_time(filename):
    pattern = re.compile(r'(\d{2})(\d{2})(\d{4})(\d{2})(\d{2})(\d{2})')
    match = pattern.match(filename)
    day, month, year, hour, minute, second = match.groups()
    date_str = f"{day}{month}{year}"
    time_str = f"{hour}{minute}{second}"
    return date_str, time_str

def generate_sequential_string(counter):
    return str(counter).zfill(7)  # Ensure the sequential string is 7 digits long

def construct_new_filename(date_str, time_str, sequential_str):
    return f"{date_str}_{time_str}_{sequential_str}.jpg"

# Example usage
filename = "23102023060003.jpg"
date_str, time_str = extract_date_time(filename)

# Initialize a counter
counter = 1

# Generate a sequential string
sequential_str = generate_sequential_string(counter)

# Construct the new filename
new_filename = construct_new_filename(date_str, time_str, sequential_str)

# Print the result
print("New Filename:", new_filename)
# %%
