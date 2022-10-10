class PrefixConverter:
    def __init__(self):
        self.stacklist = " "
        self.expression =" "
        self._data = " "
        self._size = 0
    def push(self, data):
        self.stacklist.__add__(data)
    def is_empty(self):
        return self._size == 0
    def peek(self):
        if self.stacklist:
            return self.stacklist[-1]
        else:
            return "isi stack kosong"
    def pop(self, data):
        if self.stacklist:
            data = self.stacklist.pop[-1]
            return data
        else:
            return "isi stack kosong"
    def cekvalidexpre(self, expression):
        if expression == "+" or expression == "-":
            return 1
        elif expression == "*" or expression == "/":
            return 2
        else:
            return 3
        return 0

    def infixtoprefix(self, expression):
        stack = PrefixConverter()
        stack.push(')')
        expression = expression + '('
        output = ""
        for i in range(len(expression)-1, -1, -1):
            print(i)
            if expression[i].isnumeric() == True:
                output+=expression[i]
            elif expression[i] == ")":
                stack.push(expression[i])
            elif expression[i] == "-" or expression[i] == "+" or expression[i] == "*" or expression[i] == "/" or expression[i] == "^":
                if expression[i] == "^":
                    while self.cekvalidexpre(expression[i]) <= self.cekvalidexpre(stack.pop()):
                        output+=stack.pop()
                else:
                    while self.cekvalidexpre(expression[i]) < self.cekvalidexpre(stack.pop()):
                        output+=stack.pop()
                stack.push(expression[i])
            elif expression[i] == "(":
                while stack.is_empty()== False:
                    if stack.top() != "(":
                        output+=stack.pop()
                    stack.pop()
        while stack.peek()== False:
            output+=stack.pop()
        print(output)
        
if __name__ == '__main__':
        expresi1 = PrefixConverter()
        print(expresi1.infixtoprefix("1+2+3*4/2-1"))
        print(expresi1.infixtoprefix("A * (B + C) / D"))
        print(expresi1.infixtoprefix("(1+2)*3)"))
        print(expresi1.infixtoprefix("20 * 3 - 10 + 289"))
        print(expresi1.infixtoprefix("100 * 30 / 600 - 30 + 100 * 777"))