import os
import shutil
import json

class FileSystemCore:
    def __init__(self):
        self.current_directory = './'
        self.root = {'./': {}}

    def cd(self, path):
        if path == '/':
            self.current_directory = '/'
        elif path.startswith('/'):
            self.current_directory = path
        else:
            self.current_directory = os.path.join(self.current_directory, path)
        return f"Current directory: {self.current_directory}"

    def ls(self, path='.'):
        list_dir = os.path.join(self.current_directory, path)
        try:
            contents = os.listdir(list_dir)
            return "\n".join(contents)
        except FileNotFoundError:
            return f"Directory '{list_dir}' not found."

    
class FileSystemIO:
    def touch(self, file_path):
        new_file = os.path.join(self.current_directory, file_path)
        open(new_file, 'w').close()
        return f"File '{new_file}' created."

    def cat(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return f"File '{file_path}' not found."

    def echo(self, text, file_path):
        with open(file_path, 'w') as file:
            file.write(text)
        return f"Text written to '{file_path}'."


class FileSystemOps(FileSystemCore, FileSystemIO):
    def mkdir(self, path):
        new_dir = os.path.join(self.current_directory, path)
        os.makedirs(new_dir, exist_ok=True)
        return f"Directory '{new_dir}' created."

    def cp(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        dest_path = os.path.join(self.current_directory, destination)
        with open(source_path, 'r') as src, open(dest_path, 'w') as dest:
            dest.write(src.read())
        return f"Copied '{source_path}' to '{dest_path}'."

    def rm(self, path):
        target_path = os.path.join(self.current_directory, path)
        try:
            if os.path.isfile(target_path):
                os.remove(target_path)
                return f"File '{target_path}' removed."
            elif os.path.isdir(target_path):
                shutil.rmtree(target_path)
                return f"Directory '{target_path}' removed."
        except FileNotFoundError:
            return f"Path '{target_path}' not found."


class FileSystemState:
    def save_state(self, path):
        state = {'current_directory': self.current_directory, 'root': self.root}
        with open(path, 'w') as file:
            json.dump(state, file)
        return f"File system state saved to '{path}'."

    def load_state(self, path):
        try:
            with open(path, 'r') as file:
                state = json.load(file)
                self.current_directory = state['current_directory']
                self.root = state['root']
            return f"File system state loaded from '{path}'."
        except FileNotFoundError:
            return f"File '{path}' not found. Unable to load state."


class FileSystem(FileSystemOps, FileSystemState):
    pass


def main():
    file_system = FileSystem()

    while True:
        print("Current Path:: ", file_system.current_directory)
        user_input = input("Enter command: ")

        if user_input.lower() == 'exit':
            break

        # Parse and execute commands
        parts = user_input.split(' ')
        command = parts[0]
        args = parts[1:]

        if hasattr(file_system, command):
            print("_____________________________")
            result = getattr(file_system, command)(*args)
            print(result)
            print("_____________________________")
        else:
            print("_____________________________")
            print(f"Invalid command: {command}")
            print("_____________________________")


if __name__ == "__main__":
    main()

