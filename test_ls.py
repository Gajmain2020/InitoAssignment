import unittest
import os

from colorama import Fore

from fileSystem import FileSystem  

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system = FileSystem()

    def test_ls_current_directory(self):
        result = self.file_system.ls()
        self.assertIn("some_file.txt", result)
        self.assertIn("some_directory", result)
        print(Fore.GREEN +"Test Successful" + Fore.RESET)

    def test_ls_specified_directory(self):
        # Create a subdirectory and a file in the current directory
        self.file_system.touch("test_file.txt")

        self.file_system.cd("test_directory")
        result = self.file_system.ls()
        print(Fore.GREEN +"Test Successful" + Fore.RESET)

if __name__ == '__main__':
    unittest.main()
