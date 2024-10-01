
# Quiz Game

This is a simple True/False quiz game built in Python. The game reads questions from a data source, presents them to the user, and tracks the user's score.

## How it Works

1. **Question Bank**: The quiz questions are stored in `data.py` as a list of dictionaries, where each dictionary contains a question's text and its correct answer.
2. **Classes**:
    - `Question`: This class (defined in `question.py`) represents each question with its text and answer.
    - `QuizBrain`: This class (defined in `quizz.py`) handles the quiz logic, including presenting questions, checking the user's answers, and keeping track of the score.
3. **Game Flow**:
    - The `question_data` is imported and converted into `Question` objects.
    - A `QuizBrain` object is created, which iterates through the questions, asks the user for an answer, and checks if the user's response is correct.

## How to Run

1. Clone the repository or copy the files into your local directory.
2. Ensure you have `data.py`, `question.py`, and `quizz.py` in the same directory as the main script.
3. Add your questions to the `question_data` list in `data.py` like this:

   ```python
   question_data = [
       {"text": "The Earth is flat.", "answer": "False"},
       {"text": "Python is a programming language.", "answer": "True"},
       # Add more questions here
   ]
   ```

4. Run the main script to start the quiz:

   
    python main.py
   ```

5. The game will prompt you with each question, and you can answer with `True` or `False`.

## Example Code

Here’s a snippet of the main game logic:

```python
from data import question_data
from question import Question
from quizz import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You completed the quiz! Your final score was: {quiz.score}/{len(question_bank)}")
```

## License

This project is open-source and available under the MIT License.