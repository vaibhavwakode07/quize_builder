def evaluate_quiz(quiz, user_answers):
    score = 0
    results = []

    for question, user_ans in zip(quiz.questions, user_answers):
        correct = user_ans == question.correct_answer
        if correct:
            score += 1

        results.append({
            "question": question.question,
            "correct_answer": question.correct_answer,
            "user_answer": user_ans,
            "explanation": question.explanation,
            "is_correct": correct
        })

    return score, results
