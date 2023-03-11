import sys

# Define a Stack class using linked lists
class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None

def tokenize(expr):
    for p in ['(',')','[',']','{','}']:
        expr = expr.replace(p, f' {p} ')
    return expr.split()

# Define a function to convert infix notation to postfix notation
def infix_to_postfix(expression):
    stack = Stack()
    output_queue = []
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}

    tokens = tokenize(expression)

    for token in tokens:
        if token.isdigit():
            output_queue.append(float(token))
        elif token in operators:
            while (not stack.is_empty() and stack.peek() in operators
                   and operators[token] <= operators[stack.peek()]):
                output_queue.append(stack.pop())
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while stack.peek() != '(':
                output_queue.append(stack.pop())
            stack.pop()
        else:
            raise Exception("Invalid token: {}".format(token))

    while not stack.is_empty():
        output_queue.append(stack.pop())

    return output_queue

# Define a function to parse the postfix notation expression
def parse_postfix_expression(expression):
    stack = Stack()

    for token in expression:
        if isinstance(token, float):
            stack.push(token)
        elif token in ["+", "-", "*", "/"]:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                stack.push(operand1 + operand2)
            elif token == "-":
                stack.push(operand1 - operand2)
            elif token == "*":
                stack.push(operand1 * operand2)
            elif token == "/":
                stack.push(operand1 / operand2)
        else:
            raise Exception("Invalid token: {}".format(token))

    if stack.is_empty():
        raise Exception("Empty expression")
    else:
        return int(stack.pop())

# Get the expression from the command line argument
expression = sys.argv[1]

# Convert the expression from infix to postfix notation
postfix_expression = infix_to_postfix(expression)

# Parse and compute the postfix notation expression
result = parse_postfix_expression(postfix_expression)
print(result)