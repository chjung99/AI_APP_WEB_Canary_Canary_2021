import os
import glob

os.chdir("C:/Users/CKIRUser/Downloads/n02687172")
files = files = glob.glob("C:/Users/CKIRUser/Downloads/n02687172/deletee/*")
P = "C:/Users/CKIRUser/Downloads/"


def delxml(c):

    os.chdir("C:/Users/CKIRUser/Downloads/"+c)
    files = files = glob.glob("C:/Users/CKIRUser/Downloads/"+c+"/deletee/*")

    for f in files:
        title, _ = os.path.splitext(f)
        t = title.split('/')
        #print(t)
        os.unlink(P+c+"/JPEGImages/"+t[-1].split('\\')[-1]+'.JPEG')


classlist = ['n02687172'] # 지우고자 하는 class 이름 입력, 폴더명은 class 이름으로 할 것
for c in classlist:
    delxml(c)

exit()
