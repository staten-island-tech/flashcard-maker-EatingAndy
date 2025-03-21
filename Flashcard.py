class merchant():
    def __init__(self, name, products):
        self.name=name
        self.products=products
    def sell(self,item):
        self.products.remove(item)
        print(self.products)
Rachel = merchant("Rachel", ["Apples", "Oranges", "Human"])
Kammy = merchant('kammy', ['penguins', 'whales', 'capybaras'])
print(Rachel.sell("Human"))
print(Kammy.sell('capybaras'))