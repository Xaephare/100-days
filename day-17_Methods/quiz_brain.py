class QuizBrain:


    def __init__(self, q_list):
        self.question_num = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Returns True if there are still questions in the list, else False"""
        return self.question_num < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_question.text}. (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_num}.")
        print("\n")
