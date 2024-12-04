from stackWithLinkedList import Stack
import re
import operator

class Process:
    '''Processes provided postfix and infix expressions'''
    
    def __init__(self, expression):
        self.expression = expression
        self.stack = Stack()
        self.postfixExp = []
    
    def calc(self):
        '''Evaluate a given postfix expression'''
        operators = re.compile('[×/+\-]')
        operands = re.compile(r'\d+')
        operatorTable = {
            '×': operator.mul,
            '/': operator.truediv,
            '+': operator.add,
            '-': operator.sub
        }
        
        for token in self.postfixExp:
            if operands.match(token):
                self.stack.push(int(token))
            elif operators.match(token):
                if self.stack.is_empty():
                    raise ValueError("Invalid postfix expression: Stack underflow.")
                num1 = self.stack.pop()
                num2 = self.stack.pop()
                operation = operatorTable[token]
                self.stack.push(operation(num2, num1))
        return self.stack.peek()
    
    def inToPostfix(self):
        '''Convert an infix expression to postfix using the Shunting Yard algorithm'''
        precedence = {'+': 1, '-': 1, '×': 2, '/': 2}
        output = []
        operStack = Stack()
        tokens = re.findall(r'\d+|[×/+\-()]', self.expression)

        for token in tokens:
            if re.match(r'\d+', token):  # Numbers
                output.append(token)
            elif token in precedence:  # Operators
                while (not operStack.is_empty() and
                       operStack.peek() != '(' and
                       precedence[operStack.peek()] >= precedence[token]):
                    output.append(operStack.pop())
                operStack.push(token)
            elif token == '(':  # Left parenthesis
                operStack.push(token)
            elif token == ')':  # Right parenthesis
                while not operStack.is_empty() and operStack.peek() != '(':
                    output.append(operStack.pop())
                operStack.pop()  # Pop the '('

        while not operStack.is_empty():  # Remaining operators
            output.append(operStack.pop())
        
        self.postfixExp = output
        return ' '.join(output)

    def postToInfix(self):
        '''Convert a given postfix expression to infix'''
        operators = re.compile('[×/+\-]')
        operands = re.compile(r'\d+')
        convertStack = Stack()

        for token in self.postfixExp:
            if operands.match(token):
                convertStack.push(token)
            elif operators.match(token):
                if convertStack.is_empty():
                    raise ValueError("Invalid postfix expression: Stack underflow.")
                temp1 = convertStack.pop()
                temp2 = convertStack.pop()
                combination = f"({temp2} {token} {temp1})"
                convertStack.push(combination)

        return convertStack.pop() if not convertStack.is_empty() else ""
    
    def evalInfix(self):
        '''Evaluate an infix expression by converting it to postfix'''
        self.inToPostfix()
        return self.calc()

if __name__ == "__main__":
    # Example: Postfix Evaluation
    postfixExp = "5 1 2 + 4 × + 3 -"
    process1 = Process(postfixExp)
    process1.postfixExp = postfixExp.split()  # Directly assign for postfix calc
    print("Infix form:", process1.postToInfix())
    print("Postfix result:", process1.calc())

    # Example: Infix to Postfix and Evaluation
    infixExp = "(5 + ((1 + 2) × 4)) - 3"
    process2 = Process(infixExp)
    print("Postfix form:", process2.inToPostfix())
    print("Infix result:", process2.evalInfix())
