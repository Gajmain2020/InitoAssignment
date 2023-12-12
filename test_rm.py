import unittest

from fileSystem import FileSystem

class TestInMemoryFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system = FileSystem()

    def test_remove_empty_directory(self):
        self.file_system.mkdir('/empty_directory')
        result = self.file_system.rm('/empty_directory')
        if(result!=None):
            print('Test Successful')

    def test_remove_file(self):
        self.file_system.touch('/file.txt')
        result = self.file_system.rm('/file.txt')
        if result!= None :
            print("Test Successful")

    def test_remove_nonexistent_path(self):
        result = self.file_system.rm('/nonexistent_path')
        if(result==None):
            print('Test Successful')
            pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()