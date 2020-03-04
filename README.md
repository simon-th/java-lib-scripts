# java-lib-scripts

Script to quickly add libraries to Visual Studio Code Java project.

## Pre-requisites

1. Setup a Java project with a .classpath file from VSCode
2. Copy the script to the project root folder where the .classpath file is located
3. Make sure you have the right tools installed

- On Windows, install Powershell (it should be installed on most newer machines)
- On Mac, install wget using the command `brew install wget`
- On Linux, install wget using the command `apt-get install wget`

## Instructions

As of now, there are two ways of using the script: one that quickly adds JUnit 4.13 to the class path and another that prompts a URL for a .jar file and adds that to the class path.

To add JUnit:

1. Run the following command from the command line

- On Windows, run `python add_library_windows.py -u`
- On Mac or Linux, run `python3 add_library_linux.py -u`

To add any other library:

1. Find the download link for a library that you want to add. Make sure that the URL ends with a .jar file.
2. Run the following command from the command line, or open the file from your file explorer

- On Windows, run `python add_library_windows.py`
- On Mac or Linux, run `python3 add_library_linux.py`

3. Enter the URL when prompted, or enter 'x' to quit
