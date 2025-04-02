""" class merchant():
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def sell(self,item):
        self.products.remove(item)
        print(self.products)
Rachel = merchant("Rachel", ["Apples", "Oranges", "Human"])
Kammy = merchant('kammy', ['penguins', 'whales', 'capybaras'])
print(Rachel.sell("Human"))
print(Kammy.sell('capybaras')) """

import json

class Role:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def display_question(self):
        return f"user: {self.question}, answer: {self.answer}"
class student(Role):
    def __init__(self, question, answer):
        super().__init__(question, answer)
    def answer_question(self):
        








    def Q(self, item):
        self.question.append(item)
    def A(self, item):
        self.answer.append(item)
    def to_dict(self):
        return {"Question": self.question, "Answer": self.answer}
Tquestion = input()
Tanswer = input()
teacher = Role(Tquestion, Tanswer)
student = Role(Tquestion, input())
try:
    with open("Flashcard.json", "r") as file:
        Questions = json.load(file)
except FileNotFoundError:
    Questions = []
Questions.append(teacher.to_dict())
with open("Flashcard.json", "w") as file:
    json.dump(Questions, file, indent=4)
