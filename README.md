# ExperNet data wrangling

> ⚠️ All the below assumes you are running Windows. 

## Requirements

 - You need to have git installed. run ``git`` in the terminal; if the command is not recognized install [git](https://github.com/git-guides/install-git). 
 - You need to have Anaconda or similar installed. Run ``conda info`` in the terminal; if the command is not recognized install [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html). 
 - You need to have FFMPEG installed. Run ``ffmpeg`` in the terminal; if the command is not recognized install [FFMPEG](https://ffmpeg.org/download.html#build-windows). 
## Install

1. Open a terminal in the folder where you want to copy this. 
2. Copy-paste and run the following code: 
    ```
    git clone https://github.com/lpego/ExperNet.git
    ```
3. Done. 

*Updating:* if you've been instructed to update the repository or pull changes, open a terminal in the root of the repo and run ``git pull``. 

## What does what

``scripts/rename_copy_imgs.py`` renames images in a way that is more amenable for FFMPEG and subsequent processing. It creates *one folder per day of recording* (named after the first image recorded that day) and copies all images for that day in that folder, renaming them in the process. It also creates a ``file_mapping.csv`` with the old, non-renamed file names and their corresponding new name. 

``scripts/rename_move_imgs.py`` does the same as above but moves the images, not copies. 

``scripts/run__ffmpeg.bat`` [...]


## How to use
If only renaming or moving the images: 
1. Navigate to the root directory of this repository and open a terminal
    > 📝 If you don''t know how to open a terminal in a specific folder in Windows, see [here](https://superuser.com/questions/339997/how-to-open-a-terminal-quickly-from-a-file-explorer-at-a-folder-in-windows-7)
2. type and run the following code: 
    	```
        python scripts/rename_copy_imgs.py YOUR_INPUT_FOLDER YOUR_OUTPUT_FOLDER
        ```
3. Be patient! There is no feedback on screen if the script is running. When it's done it will show your cursor again. 

If running FFMPEG: 
1. [...]

# ToDo
- [x] rename files so that the last part is sequential
    - preserve data & time info! 
- [x] save in variables/lists the time of start for each day of recording
- [ ] use those variables for the "fixed name" part fo the FFMPEG call
- [ ] make batch script that calls FFMPEG sequentially (once per day of recording) and puts the images in one video file. 