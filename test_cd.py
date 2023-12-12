import unittest
import os
from fileSystem import FileSystem  
from colorama import Fore

class TestInMemoryFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system = FileSystem()

    def test_change_to_root_directory(self):
        result = self.file_system.cd('/')
        self.assertEqual(result, "Current directory: /")
        print(Fore.GREEN +"Test Successful" + Fore.RESET)

    def test_change_to_absolute_path(self):
        self.file_system.cd('/some_directory')
        result = self.file_system.cd('/new_directory')
        self.assertEqual(result, "Current directory: /new_directory")
        print(Fore.GREEN +"Test Successful" + Fore.RESET)

    def test_invalid_path(self):
        self.file_system.cd('/existing_directory')
        result = self.file_system.cd('nonexistent_directory')
        expected_path = "/existing_directory\\nonexistent_directory"
        self.assertEqual(result, f"Current directory: {expected_path}")
        print(Fore.GREEN +"Test Successful" + Fore.RESET)

if __name__ == '__main__':
    unittest.main()
