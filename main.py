from quiz.generator import generate_quiz
from quiz.evaluator import evaluate_quiz
from utils.cli import ask_topic, ask_answer

def main():
    print("=== AI Knowledge Quiz Builder ===")

    topic = ask_topic()
    quiz = generate_quiz(topic)

    user_answers = []

    for idx, q in enumerate(quiz.questions, 1):
        print(f"\nQ{idx}. {q.question}")
        for key, value in q.options.items():
            print(f"{key}) {value}")
        user_answers.append(ask_answer())

    score, results = evaluate_quiz(quiz, user_answers)

    print("\n=== Quiz Results ===")
    print(f"Score: {score} / {len(quiz.questions)}\n")

    for i, r in enumerate(results, 1):
        print(f"Q{i}: Correct = {r['correct_answer']}, Your = {r['user_answer']}")
        print(f"Explanation: {r['explanation']}\n")

if __name__ == "__main__":
    main()
