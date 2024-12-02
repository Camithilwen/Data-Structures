from stackWithLinkedList import *
import re
import operator
class Process:
    '''Processes provided postfix expressions'''
    def __init__(self, expression):
        global ex 
        #ex = expression.split()
        ex = re.split('\(|\)|\s', expression)
        global stack
        stack = Stack()

    def calc(self):
        '''Process a given postfix expression.
        Leaves a single element stack containing the result.'''
        operators = re.compile('[×/\+\-]')
        operands = re.compile('\d{1,}')
        operatorTable = {
            '×': operator.mul,
            '/': operator.truediv,
            '+': operator.add,
            '-': operator.sub
            }
        for i in ex:
            if operands.match(i):
                stack.push(int(i))
            elif operators.match(i):
                match = operators.match(i).string
                num1 = stack.pop()
                num2 = stack.pop()
                work = operatorTable.get(match)
                stack.push(work(num2, num1))
    def infix(self):
        '''Converts a given postfix expression to infix form.'''
        operators = re.compile('[×/\+\-]')
        operands = re.compile('\d{1,}')
        convertStack = Stack()
        for i in ex:
            if operands.match(i):
                convertStack.push(i)
            elif operators.match(i):
                temp1 = convertStack.pop()
                temp2 = convertStack.pop()
                combination = f"({temp2} {i} {temp1})"
                convertStack.push(combination)
        display = ""
        for i in convertStack:
            display = display + i
        return display
    
    def postfix(self):
        '''Converts a given infix expression to postfix form.'''
        operators = re.compile('[×/\+\-]')
        operands = re.compile('\d{1,}')
        convertStack = Stack()
        operStack = Stack()
        operandCount = 0
        print(ex)
        for i in ex:
            if operands.match(i):
                if operandCount < 1:
                    convertStack.push(i)
                    operandCount += 1
                elif operandCount == 1:
                    #temp = operStack.pop()
                    #convertStack.push(temp)
                    convertStack.push(i)
                    operandCount = 0
            elif operators.match(i):
                if operandCount < 1:
                    operStack.push(i)
                if operandCount == 1:
                    convertStack.push(i)
            print(operandCount)
        display = ""
        for i in convertStack:
            display = display + i
        return display
            

if __name__ == "__main__":
    postString = "5 1 2 + 4 × + 3 -"
    calc = Process(postString)
    calc.calc()
    print(calc.infix(), "=", stack.peek())
    inString = "(5 + ((1 + 2) × 4)) - 3"
    calc2 = Process(inString)
    #print(re.split('\(|\)|\s', inString))
    print(calc2.postfix())