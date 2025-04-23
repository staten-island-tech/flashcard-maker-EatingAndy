import json
class Role:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def to_dict(self):
        return {"Question": self.question, "Answer": self.answer}
class Student(Role):
    def __init__(self, question):
        self.question = question
        super().__init__(question, "")
    def answer_question(self):
        print(self.question)
        self.answer = input()

def load_flashcards(filename="Flashcard.json"):
    try:
        with open(filename, "r") as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []

def save_flashcards(flashcards, filename="Flashcard.json"):
    with open(filename, "w") as file:
        json.dump(flashcards, file, indent=4)

role = input("What is your role?")

if role == "teacher":
    while True:
        question = input()
        answer = input()
        print("New question added")
        if input() == "done":
            break
        flashcard = Role(question, answer)
        flashcards = load_flashcards()
        flashcards.append(flashcard.to_dict())
        save_flashcards(flashcards)

elif role == "student":
    Streak = 0
    Total = 0
    Topstreak = 0
    flashcard = load_flashcards()
    for question in flashcard:
        student = Student(question["Question"])
        student.answer_question()
        Correct = question["Answer"].lower()
        if student.answer == Correct:
            print("Correct")
            Streak += 1
            Total += 1
        elif student.answer != Correct:
            print("Wrong")
            Topstreak = Streak 
            Streak = 0
        if input() == "I rage quit":
            print(f"Your total is {Total} and your highest streak was {Topstreak}.")

else:
    print("Invalid Role")