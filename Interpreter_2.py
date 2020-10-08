INTEGER,PLUS,MINUS,MULTIPLY,DIVIDE,EOF = 'INTEGER','PLUS','MINUS','MULTIPLY','DIVIDE','EOF'

class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, MINUS, or EOF
        self.type = type
        # token value: non-negative integer value, '+', '-', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    # 初始化，获取第一位的字符
    def __init__(self, text):
        self.text = text
        self.pos = 0
        # current token 由 get next token 函数更新
        self.current_token = None
        # current char update by advance
        self.current_char = self.text[self.pos]

    # 自定义错误类型
    def error(self):
        raise Exception("Error parse input")

    # move pos and update current char
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    # erase white space between tokens
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char == ' ':
            self.advance()

    # get continuous digital char and translate to number
    def integer(self):
        number = ''
        while self.current_char is not None and self.current_char.isdigit():
            number += self.current_char
            self.advance()
        return int(number)

    def get_next_token(self):

        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()

            if self.current_char.isdigit():
                return Token(INTEGER,self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS,'+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS,'-')

            if self.current_char == '*':
                self.advance()
                return Token(MULTIPLY,'*')

            if self.current_char == '/':
                self.advance()
                return Token(DIVIDE,'/')


            # 如果读取到的字符串不属于上面任何一种，报错
            self.error()

        # 读到的 current char 是 None, 报错
        return Token(EOF,None)

    def eat(self,type):
        # 如果当前token 和预期一致则读取下一个token
        print("expect type: ",type)
        print("real type: ", self.current_token.type)
        if self.current_token.type == type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()
        left = self.current_token
        result = left.value
        self.eat(INTEGER)
        while self.current_token.value is not None:
            op = self.current_token
            if op.type == PLUS:
                self.eat(PLUS)
            elif op.type == MINUS:
                self.eat(MINUS)
            elif op.type == MULTIPLY:
                self.eat(MULTIPLY)
            elif op.type == DIVIDE:
                self.eat(DIVIDE)
            right = self.current_token
            self.eat(INTEGER)
            if op.type == PLUS:
                result += right.value
            elif op.type == MINUS:
                result -= right.value
            elif op.type == MULTIPLY:
                result = result * right.value
            elif op.type == DIVIDE:
                result = result / right.value
            print("left value: ",left.value)
            print("right value: ",right.value)
            print("result: ",result)
        return result
def main():
    while True:
        try:
            text = input('cal> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()