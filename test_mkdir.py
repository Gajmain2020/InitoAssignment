import unittest
import os
import shutil

from colorama import Fore

from fileSystem import FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        # Create an instance of the FileSystem class before each test
        self.file_system = FileSystem()

    def test_mkdir(self):
        # Test creating a new directory
        new_dir_name = 'test_mkdir_directory'
        new_dir_path = os.path.join(self.file_system.current_directory, new_dir_name)
        self.assertFalse(os.path.exists(new_dir_path))
        self.file_system.mkdir(new_dir_name)
        self.assertTrue(os.path.exists(new_dir_path))
        self.assertTrue(os.path.isdir(new_dir_path))
        shutil.rmtree(new_dir_path, new_dir_name)
        print(Fore.GREEN + "Test Successful" + Fore.RESET)

    def test_mkdir_nested(self):
        # Test creating a nested directory
        nested_dir_path = os.path.join(self.file_system.current_directory, 'nested_dir', 'sub_dir')

        self.assertFalse(os.path.exists(nested_dir_path))
        self.file_system.mkdir('nested_dir/sub_dir')
        self.assertTrue(os.path.exists(nested_dir_path))
        self.assertTrue(os.path.isdir(nested_dir_path))
        shutil.rmtree(nested_dir_path,"nested_dir")
        print(Fore.GREEN + "Test Successful" + Fore.RESET)

if __name__ == '__main__':
    unittest.main()
