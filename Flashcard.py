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

class role:
    Tquestion = input()
    Tanswer = input()
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def Q(self, item):
        self.question.add(item)
    def A(self, item):
        self.answer.add(item)
    def to_dict(self):
        return {"Question": self.question, "Answer": self.answer}
    new_question = role(Tquestion, Tanswer)
    try:
        with open("Flashcard.json", "r") as file:
            Questions = json.load(file)
    except FileNotFoundError:
        Questions = []
    Questions.data.append(new_question.to_dict())
Tquestion = input()
Tanswer = input()
teacher = role(Tquestion, Tanswer)
student = role(Tquestion, input())