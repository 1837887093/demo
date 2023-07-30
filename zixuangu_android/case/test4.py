import unittest
import time

def clear():
    print("开始执行清理函数")

class TestDemo(unittest.TestCase): #自定义一个测试类，需要继承unittest自带的testcase类

    def test_01(self):
        date = [(2,2), (3,3), (1,3), (1,1), (2,2)]
        for i in date:
            with self.subTest(date=i):
                self.assertEqual(i[0],i[1],"判断1和1相等") #assertEqual是断言函数
                print("第1条用例运行")

if "__name__"=="__main__":
    unittest.main() #运行以上代码