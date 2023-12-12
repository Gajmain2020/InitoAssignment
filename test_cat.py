import unittest
import os

from colorama import Fore

from fileSystem import FileSystem  

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system = FileSystem()

    def test_cat_existing_file(self):
        # Create a file with some content
        file_content = "This is the content of the file."
        self.file_system.echo(file_content, "test_file.txt")

        # Check if the cat command reads the content correctly
        result = self.file_system.cat("test_file.txt")
        self.assertEqual(result, file_content)
        print(Fore.GREEN +"Test Successful" + Fore.RESET)
        

    def test_cat_nonexistent_file(self):
        # Try to read the content of a nonexistent file
        result = self.file_system.cat("nonexistent_file.txt")
        self.assertEqual(result, "File 'nonexistent_file.txt' not found.")
        print(Fore.GREEN +"Test Successful" + Fore.RESET)

    def tearDown(self):
        # Clean up any files created during the tests
        test_file_path = os.path.join(self.file_system.current_directory, "test_file.txt")

        if os.path.exists(test_file_path):
            os.remove(test_file_path)

if __name__ == '__main__':
    unittest.main()
