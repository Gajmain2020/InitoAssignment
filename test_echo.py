import unittest
import os
from fileSystem import FileSystem
from colorama import Fore

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system = FileSystem()

    def test_echo_new_file(self):
        result = self.file_system.echo("Hello, World!", "new_file.txt")

        self.assertTrue(os.path.exists("new_file.txt"))
        self.assertEqual(result, "Text written to 'new_file.txt'.")
        with open("new_file.txt", 'r') as file:
            content = file.read()
        self.assertEqual(content, "Hello, World!")
        print(Fore.GREEN + 'Test Successful'+ Fore.RESET)

    def test_echo_existing_file(self):
        with open("existing_file.txt", 'w') as file:
            file.write("Initial content")

        result = self.file_system.echo("New content", "existing_file.txt")

        self.assertTrue(os.path.exists("existing_file.txt"))
        self.assertEqual(result, "Text written to 'existing_file.txt'.")

        with open("existing_file.txt", 'r') as file:
            content = file.read()
        self.assertEqual(content, "New content")
        print(Fore.GREEN + 'Test Successful'+ Fore.RESET)

if __name__ == '__main__':
    unittest.main()
