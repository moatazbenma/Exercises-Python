class Quiz:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": "C"},
            {"question": "Which programming language is known for web development?", "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"], "answer": "C"},
            {"question": "What is 5 + 7?", "options": ["A. 10", "B. 12", "C. 14", "D. 16"], "answer": "B"},
        ]
        self.score = 0
    
    def run_quiz(self):
        for q in self.questions:
            print(q["question"])
            for option in q["options"]:
                print(option)
            answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
            
            if answer == q["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}\n")
        
        print(f"Quiz Over! Your final score is: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()