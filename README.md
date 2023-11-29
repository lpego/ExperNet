# ExperNet data wrangling

> ⚠️ All the below assumes you are running Windows. 

## Requirements

 - You need to have git installed. run ``git`` in the terminal; if the command is not recognized install [git](https://github.com/git-guides/install-git). 
 - You need to have Anaconda or other package manager installed. Run ``conda info`` in the terminal; if the command is not recognized install [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html). 
 - You need to have FFMPEG installed. Run ``ffmpeg`` in the terminal; if the command is not recognized install [FFMPEG](https://ffmpeg.org/download.html#build-windows). 

## Install

1. Open a terminal in the folder where you want to copy this repository. 
2. Copy-paste and run the following code: 
    ``` bat
    git clone https://github.com/lpego/ExperNet.git
    ```
3. Done. 

*Updating:* if you've been instructed to update the repository or pull changes, open a terminal in the root of the repo and run ``git pull``. 

## What does what

``scripts/rename_copy_imgs.py`` renames images in a way that is more amenable for FFMPEG and subsequent processing. It creates *one folder per day of recording* (named after the first image recorded that day) and copies all images for that day in that folder, renaming them in the process. It also creates a ``file_mapping.csv`` with the old, non-renamed file names and their corresponding new name. 

``scripts/rename_move_imgs.py`` does the same as above but moves the images, not copies. 

``scripts/run_ffmpeg.bat`` calls sequentially FFMPEG on *all* the subfolders of a parent directory, and makes a video out of the images contained in this subfolders. Parameters are set directly in the ``.bat`` file. 


## How to use
**If only renaming or moving the images:** 
1. Navigate to the root directory of this repository and open a terminal
    > 📝 If you don''t know how to open a terminal in a specific folder in Windows, see [here](https://superuser.com/questions/339997/how-to-open-a-terminal-quickly-from-a-file-explorer-at-a-folder-in-windows-7)
2. Type in the following code, substituting the input and output folders with your paths: 
    ``` bat
    python scripts/rename_copy_imgs.py YOUR_INPUT_FOLDER YOUR_OUTPUT_FOLDER
    ```
3. Be patient! There is no feedback on screen if the script is running. When it's done it will show your cursor ready to type again. 
    > ⚠️ There can be no spaces (`` ``) in your file paths!

    > ⚠️ If you are copying from an external hard drive to your local disk (or vice-versa), make sure to use backlashes (``\``) and not forward slashes (``/``) in your file path. 

**If running FFMPEG manually on one folder:** 
1. Navigate to the folder containing the images that you want to make into a video and open a terminal there. 
2. Type the following code, substituting the input file name and output file name: 
    ``` bat
    ffmpeg -framerate 1 -i YOUR_FILE_NAME_%d.jpg YOUR_OUTPUT_NAME.avi
    ```
3. What this does is: make a video at 1 frame per second (it's best if this matches the frequency of images taken in the field), using as input files called ``YOUR_FILE_NAME_`` followed by a sequential number (``%3d``) that are ``.jpg`` format, and saves them as a video named ``YOUR_OUTPUT_NAME`` of format ``.avi``. 
    > 📝 ``%03d`` is a formatting string, specifying how the sequential numbers following the base file name are constructed; see this [StackOverflow answer](https://stackoverflow.com/questions/23718936/explanation-for-sprintf03d-7-functionality) for more details. 
4. There are *many, many* more options in FFMPEG for output, you have to experiment with what works best for you. Have a look [here](https://trac.ffmpeg.org/wiki/Slideshow) for inspiration. 

**If running FFMPEG on all folders:** 
1. Open the file ``scripts/run_ffmpeg.bat`` in a text editor. It should look something like this: 
    ``` bat
    @echo off
    setlocal enabledelayedexpansion

    rem "##########################################################"
    rem Set the path to the directory containing the subdirectories
    set "parentDirectory=YOUR\FILE\PATH\GOES\HERE"

    rem Change to the parent directory
    cd /d "%parentDirectory%"

    rem Iterate through each subdirectory
    for /D %%i in (*) do (
        echo "<=========================================================>"
        echo Processing directory: %%i
        echo "<=========================================================>"

        rem Run the following commands on the contents of each directory
        pushd "%%i"

        rem "##########################################################"
        rem Call FFMPEG with the parameters below
        ffmpeg -framerate 1 -y -i %%i_%%d.jpg %%i.avi

        rem (more commands can be added here)

        rem Return to the parent directory
        popd
    )

    endlocal
    ```
2. The important parts of this script are: 
    - line 6: ``set "parentDirectory=YOUR\FILE\PATH\GOES\HERE"``, where you need to substitute the path of the directory containing the various subfolders that contain the images. 
    - line 22: ``ffmpeg -framerate 1 -y -i %%i_%%d.jpg %%i.avi``, that contains the FFMPEG call. It's the same as the manual call explained above, with the only difference being that we use the contents of variable ``%%i`` instead of specifying the file name directly. This variable is a list of the names of the various subfolder containing the images, therefore *the the images inside the subfolders must be named the same as the subfolders themselves*. You can change the options (e.g. ``-framerate``), file formats (e.g. ``.avi``) and flags (e.g. ``-y``) in the call as you wish. 
    > ⚠️ The ``-y`` flag means FFMPEG will overwrite output files tih the same name without asking! 
3. Once you have modified the script according to your needs, you can save it with a different name than the template; let's say you save it as ``scripts/run_ffmpeg_test.bat``. 
4. Open a terminal in the root of this repo, and type: 
    ``` bat
    scripts/run_ffmpeg_test.bat
    ``` 
5. When you press Enter, the script will run FFMPEG with the specified parameters on all subfolders of your parent directory. 

# ToDo
- [x] rename files so that the last part is sequential
    - preserve data & time info! 
- [x] save in variables/lists the time of start for each day of recording
- [x] ~~use those variables for the "fixed name" part fo the FFMPEG call~~ no need, can grab base file name from dir name instead. 
- [x] make batch script that calls FFMPEG sequentially (once per day of recording) and puts the images in one video file. 