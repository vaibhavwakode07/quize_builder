def build_prompt(topic, context=None):
    base_prompt = f"""
Generate exactly 5 multiple-choice questions on the topic: "{topic}"

Rules:
- Each question must have 4 options labeled A, B, C, D
- Only one option must be correct
- Provide the correct answer letter
- Provide a short explanation

Return ONLY valid JSON in the format:
{{
  "questions": [
    {{
      "question": "",
      "options": {{
        "A": "",
        "B": "",
        "C": "",
        "D": ""
      }},
      "correct_answer": "A",
      "explanation": ""
    }}
  ]
}}
"""
    if context:
        return f"Context:\n{context}\n\n{base_prompt}"

    return base_prompt
