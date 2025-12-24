import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print("API KEY FOUND:", bool(api_key))

client = OpenAI(api_key=api_key)


def call_llm(prompt):
    try:
        # ===== REAL LLM CALL =====
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content

    except Exception as e:
        # ===== FALLBACK MOCK DATA =====
        print("⚠️ OpenAI unavailable (quota/auth). Using MOCK quiz.")

        return """
        {
          "questions": [
            {
              "question": "What is photosynthesis?",
              "options": {
                "A": "Process of respiration",
                "B": "Process by which plants make food using sunlight",
                "C": "Water absorption method",
                "D": "Soil nutrient cycle"
              },
              "correct_answer": "B",
              "explanation": "Photosynthesis allows plants to convert sunlight into chemical energy."
            },
            {
              "question": "Which gas is required for photosynthesis?",
              "options": {
                "A": "Oxygen",
                "B": "Hydrogen",
                "C": "Carbon dioxide",
                "D": "Nitrogen"
              },
              "correct_answer": "C",
              "explanation": "Carbon dioxide is consumed during photosynthesis."
            },
            {
              "question": "Which part of the plant performs photosynthesis?",
              "options": {
                "A": "Roots",
                "B": "Stem",
                "C": "Leaves",
                "D": "Flowers"
              },
              "correct_answer": "C",
              "explanation": "Leaves contain chlorophyll needed for photosynthesis."
            },
            {
              "question": "What pigment captures sunlight?",
              "options": {
                "A": "Hemoglobin",
                "B": "Chlorophyll",
                "C": "Melanin",
                "D": "Carotene"
              },
              "correct_answer": "B",
              "explanation": "Chlorophyll absorbs light energy."
            },
            {
              "question": "What is released as a by-product?",
              "options": {
                "A": "Carbon dioxide",
                "B": "Oxygen",
                "C": "Nitrogen",
                "D": "Hydrogen"
              },
              "correct_answer": "B",
              "explanation": "Oxygen is released during photosynthesis."
            }
          ]
        }
        """
