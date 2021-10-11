import unittest
import os
from detect import *

def customf():
    return "Test"

class canaryAiTest(unittest.TestCase):

    def setUp(self):
        self.file_name = 'testfile.txt'
        with open(self.file_name, 'wt') as f:
            f.write("""Unittest test""".strip())
    
    def tearDown(self):
        """Delete file at end of test"""
        try:
            os.remove(self.file_name)
        except:
            pass

    def test_runs(self):
        customf()
    
    def test_print(self):
        self.assertEqual(customf(), 'Test')

    def test_error(self):
        with self.assertRaises(IndexError):
            a = []
            a[1]

    def test_check_config(self, path='./config.json'):
        check_config(path)

        if os.path.exists(path):
            with open(path) as json_file:
                json_data = json.load(json_file)
                self.assertIsNotNone(json_data)

    
    def test_download_file_from_google_drive(self):
        download_file_from_google_drive()
        assert os.path.exists('weight/yolov5m6.pt')

    def test_attemp_download_weight(self):
        attemp_download_weight()
        assert os.path.exists('weight/yolov5m6.pt')
    
    #def test_detect(self):
        # args를 인자로 어떻게 받아서 어떻게 test?

    


if __name__ == '__main__':
    unittest.main()
    
