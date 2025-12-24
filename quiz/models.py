class Question:
    def __init__(self, question, options, correct_answer, explanation):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation


class Quiz:
    def __init__(self, topic, questions):
        self.topic = topic
        self.questions = questions
