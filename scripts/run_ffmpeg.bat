@echo off
setlocal enabledelayedexpansion

rem "##########################################################"
rem Set the path to the directory containing the subdirectories
set "parentDirectory=D:\ExperNet\data\renamed\testdir"

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
