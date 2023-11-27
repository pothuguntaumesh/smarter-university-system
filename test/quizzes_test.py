import unittest
from datetime import datetime
import math
from app.controllers.quizzes_controller import QuizzesController
class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        quizzesBefore=len(self.ctrl.get_quizzes())
        #Crash at line 63 of Quizzes_controller as bool cannot be added to string
        self.ctrl.add_quiz(True,"text",datetime.now(),datetime.now())
        #Error log: TypeError: unsupported operand type(s) for +: 'bool' and 'str'
        quizzerAfter=len(self.ctrl.get_quizzes())
        self.assertEqual(quizzesBefore,quizzerAfter,"Quiz must not be added because bool cannot be appended to string")


    def test_expose_failure_02(self):
        quizId=self.ctrl.add_quiz("quiz1","text",datetime.now(),datetime.now())
        questionId=self.ctrl.add_question(quizId,"title","text1")
        #Crash at line 84 as a very big integer cannot be converted into a string
        answerId=self.ctrl.add_answer(questionId,math.pow(10,1000),True)
        #Error log: Failed with Error: math range error
        self.assertIsNotNone(answerId,"answerId cannot be None")
    def test_expose_failure_03(self):

        quizId=self.ctrl.add_quiz("title","text",datetime.now(),datetime.now())
        #This will crash the code at line number 78 of quizzes_controller as we cannot encode Unicode code point that's a high surrogate using UTF-8 Encoding
        questionId=self.ctrl.add_question(quizId,"enpm611\U0000D801project","text")
        #Error log: Failed with Error: 'utf-8' codec can't encode character '\ud801' in position 7: surrogates not allowed
        self.assertIsNotNone(questionId,"questionId cannot be None")

    def test_expose_failure_04(self):
        #CAUTION!!!: Once this is run, quizzes_test will have incomplete data, making the whole program invalid.
        quizId=self.ctrl.add_quiz("title2","text3",datetime.now(),datetime.now())
        #This will crash the code at line number 78 of quizzes_controller as we cannot encode bytes array using UTF-8 Encoding
        questionId=self.ctrl.add_question(quizId,b'\x80\x80\x80',"text")
        #Error log: Object of type bytes is not JSON serializable
        self.assertIsNotNone(questionId,"questionId cannot be None")
        

if __name__ == '__main__':
    unittest.main()