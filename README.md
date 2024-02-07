


This program, named "File Organizer", is designed to organize files within a specific directory based on their names. Initially intended to handle files with the ".gbc" extension, it has been developed to work with any file extension.

It was created for a specific purpose: to facilitate the process of associating game covers with the Powkiddy x39 pro console. 
This console requires game covers to be present in the "images" folder and to have the same name as the corresponding game.
Additionally, it requires each game to be contained within a folder with the same name.
Here is a graphical example of the directory tree structure:


<code>
/----- GBA ----------------------------------------------------------------\
|                                                                            
|   /--- images --\         /---super_mario--\      /---  ....   ------\    
|   | super_mario |         |                |      |                  |    
|   | ...         |         | super_mario.gba|      |     .....        |    
|   |             |         |                |      |                  |    
|   \-------------/         \----------------/      \------------------/    
|                                                                            
\--------------------------------------------------------------------------/
</code>

The program iterates through the files in the specified directory and, for each file, checks if it meets the requirements of the console. If a file corresponds to a valid game, it creates a new folder with the same name as the game (without an extension), then moves the file into this folder. This way, the program helps organize files so that the console can correctly read game covers and associate them with the corresponding games.



This code is a Python script that organizes files with the ".gbc" extension into folders based on their filenames. Here's what it does:

It imports two modules, os and shutil, which are used for file and directory operations.
It defines a function organizza_files_gba(path) which takes a path argument representing the directory where files should be organized.
Within the function:
a. It iterates through all files in the specified directory using os.listdir(path).
b. For each file, it constructs the full file path using os.path.join(path, filename).
c. It checks if the current file is a regular file (not a directory) and if its name ends with ".gbc" using os.path.isfile(filepath) and filename.endswith(".gbc").
d. If the conditions are met, it extracts the folder name (without the extension) using os.path.splitext(filename)[0].
e. It creates a new folder with the extracted name using os.makedirs(new_folder) if it doesn't already exist.
f. It moves the file into the newly created folder using shutil.move(filepath, new_filepath).
At the end of the script, it checks if the script is being run as the main program (if __name__ == "__main__":) and if so:
a. It specifies the directory to examine for ".gbc" files.
b. It calls the organizza_files_gba() function with the specified directory path.
