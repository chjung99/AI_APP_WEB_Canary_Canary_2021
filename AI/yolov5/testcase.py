import unittest
import argparse
import os
import json
from detect import *

global args

def customf():
    return "Test"

class testArgs:
    def __init__(self):
        self.args = None

class canaryAiTest(unittest.TestCase):

    def setUp(self):
        self.file_name = 'testfile.txt'
        with open(self.file_name, 'wt') as f:
            f.write("""Unittest test""".strip())

        self.args = None
        self.results = None
    
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

    def test_check_config(self):
        path = "/config.json"
        check_config()

        if os.path.exists(path):
            with open(path) as json_file:
                json_data = json.load(json_file)
                self.assertIsNotNone(json_data)

    
    def test_download_file_from_google_drive(self):
        #   download_file_from_google_drive()
        assert os.path.exists('weight/yolov5m6.pt')

    def test_attemp_download_weight(self):
        attemp_download_weight()
        assert os.path.exists('weight/yolov5m6.pt')
    
    def test_detect_work(self):
        assert os.path.exists(args.input_image_path)
        global result
        try: 
            results = detect(args)
        except:
            raise ValueError
        self.assertIsNotNone(results)


        # args를 인자로 어떻게 받아서 어떻게 test?
    
    def test_mosaic_work(self):
        try:
            mosaic(results, args)
        except:
            raise ValueError
        assert os.path.exists(args.output_image_path)
        assert os.path.exists(args.output_warning_path)
        assert os.path.exists(args.output_log_path)
        # 각 파일의 내용을 확인해서 하기?
        # detect.py를 리팩토링해서 잘 정리해서 단위로 테스트하기?
        # 음...


parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("--input_image_path", "-i", help="Input image path")
parser.add_argument("--output_image_path", "-o", help="Output image path")
parser.add_argument("--weight_path", "-w", help="Weight path")
parser.add_argument("--blur", "-b", action="store_true")

parser.add_argument("--output_warning_path", "-o2", help="Warning text path")
parser.add_argument("--server_url", "-u", help="Warning text path")

parser.add_argument("--strength", "-s", type=int, default=1, choices=[0,1])
parser.add_argument("--user_id", "-d", help="user_id") # user_id from front
parser.add_argument("--output_log_path", "-o3", help="output_log_path") # user_id from front
# TODO: arg로 mosaic 강도를 입력받고, 그 만큼 면적을 줄여서 return

args = parser.parse_args()


if __name__ == '__main__':
    unittest.main(__name__, argv=['main'], exit=False)
    
