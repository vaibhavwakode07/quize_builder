def ask_topic():
    return input("Enter quiz topic: ").strip()


def ask_answer():
    while True:
        ans = input("Your answer (A/B/C/D): ").upper()
        if ans in ["A", "B", "C", "D"]:
            return ans
        print("Invalid choice. Please enter A, B, C, or D.")
