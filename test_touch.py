import unittest
import os

from colorama import Fore

from fileSystem import FileSystem 

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system = FileSystem()

    def test_touch_new_file(self):
        result = self.file_system.touch("new_file.txt")

        self.assertTrue(os.path.exists("new_file.txt"))
        print(Fore.GREEN + 'Test Successful'+ Fore.RESET)

    def test_touch_existing_file(self):
        result = self.file_system.touch("existing_file.txt")
        self.assertTrue(os.path.exists("existing_file.txt"))
        self.assertEqual(result, "File './existing_file.txt' created.")
        print(Fore.GREEN + 'Test Successful'+ Fore.RESET)

if __name__ == '__main__':
    unittest.main()
