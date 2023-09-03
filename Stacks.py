class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]

def is_balanced(expression):
    stack =Stack()

    mapping = {
        "]":"[",
        "}":"{",
        ")":"("
    }

    for char in expression:
        if char in "[({":
            stack.push(char)
        elif char in "])}":
            if stack.is_empty() or stack.peek() != mapping[char]:
                return False
            stack.pop()

    return stack.is_empty()

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False 