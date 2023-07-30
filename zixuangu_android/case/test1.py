import unittest
import time
class TestDemo(unittest.TestCase): #自定义一个测试类，需要继承unittest自带的testcase类
    def test_01(self):
        self.assertEqual(1,1,"判断1和1相等") #assertEqual是断言函数
    def test_02(self):
        self.assertEqual(1,1,"判断1和1相等")

class TestDemo1(unittest.TestCase):
    @unittest.expectedFailure
    def test_03(self):
        self.assertEqual(1,2,"判断1和2相等")
    def test_04(self):
        self.assertEqual(1,1,"判断1和1相等")

if "__name__"=="__main__":
    unittest.main() #运行以上代码