class Expression:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    
    
    def __str__(self):
        return f"{self.left} {self.operator} {self.right} = {self.evaluate()}"
    
    def __repr__(self):
        return f"Expression({self.left}, '{self.operator}', {self.right})"
    
    def __eq__(self, other):
        if isinstance(other, Expression):
            return self.evaluate() == other.evaluate()
        return True
    
    def evaluate(self):
        if self.operator == '+':
            return self.left + self.right
        elif self.operator == '-':
            return self.left - self.right
        elif self.operator == '*':
            return self.left * self.right
        elif self.operator == '/':
            if self.right == 0:
                return "Error: Division by zero"
            return self.left / self.right
        else:
            return "Error: Invalid operator"
    


expr1 = Expression(3, '+', 4)
expr2 = Expression(2, '*', 3.5)
expr3 = Expression(10, '-', 2)

print(str(expr1)) 
print(expr1 == expr2) 
print(expr1 == expr3)