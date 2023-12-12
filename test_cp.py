import unittest
import os
from fileSystem import FileSystem  

from colorama import Fore

class TestFileSystemCommands(unittest.TestCase):
    def setUp(self):
        self.file_system = FileSystem()

    def test_cp_existing_file(self):
        # Create an existing file with some content
        with open("source_file.txt", 'w') as file:
            file.write("Original content")
        result = self.file_system.cp("source_file.txt", "destination_file.txt")
        self.assertTrue(os.path.exists("destination_file.txt"))
        with open("destination_file.txt", 'r') as file:
            content = file.read()
        self.assertEqual(content, "Original content")
        os.remove("source_file.txt")
        os.remove("destination_file.txt")
        print(Fore.GREEN + "Test Successful"+Fore.RESET)

if __name__ == '__main__':
    unittest.main()
