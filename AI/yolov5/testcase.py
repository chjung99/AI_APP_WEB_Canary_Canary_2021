import unittest
import os
import argparse
from detect import *

def customf():
    return "Test"

class canaryAiTest(unittest.TestCase):

    def __init__(self):
        self.args = None

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
        #   download_file_from_google_drive()
        assert os.path.exists('weight/yolov5m6.pt')

    def test_attemp_download_weight(self):
        attemp_download_weight()
        assert os.path.exists('weight/yolov5m6.pt')
    
    def test_detect(self):
        detect(self.args)
        # args를 인자로 어떻게 받아서 어떻게 test?
    
    def test_model_work(self):
        assert os.path.exists(self.args.input_image_path)
        assert os.path.exists(self.args.output_image_path)
        assert os.path.exists(self.args.output_warning_path)
        assert os.path.exists(self.args.output_log_path)
        # 각 파일의 내용을 확인해서 하기?
        # detect.py를 리팩토링해서 잘 정리해서 단위로 테스트하기?
        # 음..

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--input_image_path', '-i', help='Input image path')
parser.add_argument('--output_image_path', '-o', help='Output image path')
parser.add_argument('--weight_path', '-w', help='Weight path')
parser.add_argument('--blur', '-b', action="store_true")
parser.add_argument('--output_warning_path', '-o2', help='Warning text path')
parser.add_argument('--strength', '-s', type=int, default=1, choices=[0,1]) # test 후 결과에 따라 강도 조정 예정 --> 찬호님이 자동 적응 mosaic 진행중
parser.add_argument('--user_id', '-d', help='user_id') # user_id from front
parser.add_argument('--output_log_path', '-o3', help='output_log_path') # user_id from front
args = parser.parse_args()
canaryAiTest.args = args
# canaryAiTest.i_path = args.input_image_path
# canaryAiTest.o_path = args.output_image_path
# canaryAiTest.o2_path = args.output_warning_path
# canaryAiTest.o3_path = args.output_log_path

if __name__ == '__main__':
    unittest.main()
    
