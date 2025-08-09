class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.toppings = []

    def __str__(self):
        return f"Пицца:\nТесто: {self.dough}\nСоус: {self.sauce}\nНачинка: {', '.join(self.toppings)}"
    

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza.dough = dough
        return self
    
    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self
    
    def add_toppings(self, topping):
        self.pizza.toppings.append(topping)
        return self
    
    def build(self):
        return self.pizza
    

builder = PizzaBuilder()
pepperony_pizza = (builder
                   .set_dough("Тонкое")
                   .set_sauce("Томатный")
                   .add_toppings("пепперони")
                   .add_toppings("сыр")
                   .add_toppings("перец")
                   .build()
                   )

print(pepperony_pizza)
    

