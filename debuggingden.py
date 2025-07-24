import json
import random
import os

# Load questions from JSON file
def load_questions(filename):
    try:
        # Get the absolute path to this script
        script_dir = os.path.dirname(os.path.abspath(__file__))  # full path to script
        file_path = os.path.join(script_dir, filename)

        print(f"🔍 Loading questions from: {file_path}")  # Debug print

        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        print(f"❌ Error: {filename} not found at {file_path}.")
        return []
    except json.JSONDecodeError:
        print("❌ Error: File is not valid JSON.")
        return []

# Run the quiz
def run_quiz(questions, num_questions=10):
    score = 0
    selected_questions = random.sample(questions, num_questions)

    for idx, q in enumerate(selected_questions, start=1):
        print(f"\nQ{idx}: {q['question']}")
        for i, choice in enumerate(q["choices"], start=1):
            print(f"  {i}. {choice}")

        try:
            answer = int(input("Your answer (1-4): "))
            if q["choices"][answer - 1].strip().lower() == q["answer"].strip().lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Skipping question.")

    print(f"\n🎉 Quiz completed! Your score: {score}/{num_questions}")

# Main execution
if __name__ == "__main__":
    questions = load_questions("quiz_questions.json")
    if questions:
        run_quiz(questions)