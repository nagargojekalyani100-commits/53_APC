from abc import ABC, abstractmethod


class Question(ABC):

    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            print("MCQ Answer: Correct")
        else:
            print("MCQ Answer: Incorrect")


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            print("True/False Answer: Correct")
        else:
            print("True/False Answer: Incorrect")


class DescriptiveQuestion(Question):
    def __init__(self, expected_answer):
        self.expected_answer = expected_answer

    def evaluate_answer(self, answer):
        if answer.lower() == self.expected_answer.lower():
            print("Descriptive Answer: Correct")
        else:
            print("Descriptive Answer: Incorrect")


# Create objects
mcq = MCQQuestion("B")
true_false = TrueFalseQuestion("True")
descriptive = DescriptiveQuestion("Python is a programming language")

# Evaluate answers
mcq.evaluate_answer("B")
true_false.evaluate_answer("True")
descriptive.evaluate_answer("Python is a programming language")