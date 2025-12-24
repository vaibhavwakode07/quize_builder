import json
from ai.llm_client import call_llm
from ai.prompt import build_prompt
from quiz.models import Question, Quiz

def generate_quiz(topic, context=None):
    prompt = build_prompt(topic, context)
    raw_output = call_llm(prompt)

    data = json.loads(raw_output)
    questions = []

    for q in data["questions"]:
        question = Question(
            q["question"],
            q["options"],
            q["correct_answer"],
            q.get("explanation", "")
        )
        questions.append(question)

    return Quiz(topic, questions)
