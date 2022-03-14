from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # question_text = question["text"]          # (q_d 2)  question["question"]
    # question_answer = question['answer']      # (q_d 2)  question['correct_answer']

    new_q = Question(question["text"], question['answer'])   # (q_d 1)  # Alt. new_q = Question(question_text,question_answer)
    # new_q = Question(question["question"],question["correct_answer"])   # (q_d 2)  # Alt. new_q = Question(question_text,question_answer)

    # question_data 1.... "text", "answer"
    # question_data 2.... "question", "correct_answer"

    question_bank.append(new_q)


print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
