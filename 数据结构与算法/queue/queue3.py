class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.empty():
            return self.stack.pop()

    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    def empty(self):
        return len(self.stack) == 0


def result(n):
    stack = []
    while n:
        n, x = divmod(n, 8)
        stack.append(str(x))
    stack.reverse()
    return ''.join(stack)


def result2(symbol):
    stack = Stack()
    for i in symbol:
        if i == '(' or i == '{' or i == '[':
            stack.push(i)
        elif i == ']':
            if stack.empty():
                print('缺 [')
                return 0
            if stack.top() != '[':
                print('%s与 ] 不匹配' % stack.top())
                return 0
            stack.pop()
        elif i == '}':
            if stack.empty():
                print('缺 {')
                return 0
            if stack.top() != '{':
                print('%s与 } 不匹配' % stack.top())
                return 0
            stack.pop()
        elif i == ')':
            if stack.empty():
                print('缺 (')
                return 0
            if stack.top() != '(':
                print('%s与 ) 不匹配' % stack.top())
                return 0
            stack.pop()
        if stack.empty():
            print('括号配对!')
            return 1
        # else:
        #     while not stack.empty():
        #         if stack.top() == '{':
        #             print('缺少}')
        #             stack.pop()
        #         elif stack.top() == '[':
        #             print('缺少]')
        #             stack.pop()
        #         elif stack.top() == '(':
        #             print('缺少)')
        #             stack.pop()
        #     return 0


def result3(symbol):
    """ 操作后缀表达式 """
    stack = Stack()
    for i in symbol:
        if i == '+' or i == '-' or i == '*' or i == '/':
            y = int(stack.pop())
            x = int(stack.pop())
            if i == '+':
                stack.push(x + y)
            if i == '-':
                stack.push(x - y)
            if i == '*':
                stack.push(x * y)
            if i == '/':
                stack.push(x / y)
        else:
            stack.push(i)
    return stack.top()


if __name__ == '__main__':
    # b = result(8164)
    # print(b)
    # print(isinstance(b, str))

    # res = '([])'
    # symbol = list(res)
    # print(result2(symbol))

    res = '4132-*+99/-'
    symbol = list(res)
    print(result3(symbol))
