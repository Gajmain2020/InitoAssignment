# In-Memory File System

## Overview

This Python script implements a simple in-memory file system simulation with basic operations such as navigating directories (cd), listing contents (ls), creating files and directories (touch, mkdir), copying files (cp), removing files or directories (rm), saving and loading the state of the file system (save_state, load_state), and more.

### Functionality implemented

- `mkdir` - to make directory in the folder where the python script is running.
- `cd` - to change the directory where the python script is running.
- `rm` - to remove directory or any file where the python script is running.
- `ls` - to list contents of the directory.
- `touch`
- `cat` - to reads data from the file and gives its content as output.
- `echo` - to write text to a file.

## Components

#### `FileSystemCore`

- `cd (path)`: Change the current directory to the specified path. Supports relative and absolute paths, including parent directory navigation using ".." and moving to the root using "/".
- `ls(path='.')`: List the contents of the specified directory. Handles both existing and non-existing directories gracefully.

#### `FileSystemIO`

-`touch (file_path)`: Create a new empty file at the specified path.

- `cat(file_path)`: Display the contents of a file.
- `echo(text, file_path)`: Write text to a file.

#### FileSystemOps

- `mkdir(path)`: Create a new directory at the specified path.
- `cp(source, destination)`: Copy a file or directory to another location.
- `rm(path)`: Remove a file or directory.

#### FileSystemState

- `save_state(path)`: Save the current state of the file system to a JSON file.
- `load_state(path)`: Load a previously saved state of the file system from a JSON file.

#### FileSystem

The main class that inherits functionalities from FileSystemOps and FileSystemState.

##### `How to Run`

1. Run the script.

   ```{python}
   1. Run fileSystem.py
   2. to run use following command:
       python fileSystem.py
   ```

2. The program will display the current path, waiting for user input.

   ```{python}
   Current Path:: ./
   Enter command:
   ```

3. Enter commands like mkdir, cd, ls, touch, echo, cat, mv, cp, rm, and exit to perform file system operations.
4. The program will execute the command and display the result.
5. Example Commands
   - `mkdir new_directory`: Create a new directory.
   - `cd new_directory`: Change the current directory.
   - `ls`: List the contents of the current directory.
   - `touch new_file.txt`: Create a new empty file.
   - `echo 'Hello, World!' new_file.txt`: Write text to a file.
   - `cat new_file.txt`: Display the contents of a file.
   - `mv source_file.txt destination/`: Move a file or directory.
   - `cp source_file.txt destination/`: Copy a file or directory.
   - `rm file.txt`: Remove a file or directory.
     exit: Exit the file system.

#### Persistent State

The file system supports saving and loading its state using the save_state and load_state commands. Specify a file path to store or retrieve the state in JSON format.

### For Testing

1. Run Scripts
   - There are different files starting with test\_<function_name>.py run these files to test code.
2. Example
   - for testing mkdir function of `fileSystem.py` run `python test_mkdir.py`
3. Test Results
   - Test results are shown in the terminal itself.

### Additional Notes

- `mv` and `cp` commands are not supported properly due to some bugs.
- test might create some `junk folders` in the directory in which the tests are run.
- test cases almost contains all the possible scenarios of testing the `file system`.
- some empty folders and files are already kept in the directory to keep the testing smooth.

`Thankyou for reading!!`
