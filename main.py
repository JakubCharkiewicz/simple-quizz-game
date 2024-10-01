from data import question_data
from question import Question
from quizz import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
QuizBrain(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print(f"You completed the quiz! Your final score was: {quiz.score}/{len(question_bank)}")
