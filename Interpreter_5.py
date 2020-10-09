from Utils import Stack

INTEGER, PLUS, MINUS, MUL, DIV, EOF,LEFTBRACKET, RIGHTBRACKET \
    = 'INTEGER', 'PLUS', 'MINUS','MUL', 'DIV', 'EOF', 'LEFTBRACKET', 'RIGHTBRACKET'

# 每个词素
class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Token({type}, {value})".format(type=self.type,value=repr(self.value))

    def __repr__(self):
        return self.__str__()

# 词法分析程序
class Lexer(object):
    def __init__(self,text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalid character")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        if self.current_char is not None:
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
                return Token(MUL, '*')
            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')
            if self.current_char == '(':
                self.advance()
                return Token(LEFTBRACKET,'(')
            if self.current_char == ')':
                self.advance()
                return Token(RIGHTBRACKET,')')
        else:
            return Token(EOF,None)

# 解释器
class Interpreter(object):
    def __init__(self,lexer):
        self.lexer = lexer
        # 获取第一个token，此时lexer.pos 仍然等于 0
        self.current_token = lexer.get_next_token()
        self.operatorStack = Stack()
        self.numberStack = Stack()

    def error(self):
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        if token_type == self.current_token.type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    # 用factor来取代eat，可以获取运算符的下一个字符，并且移动pos
    def factor(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def term(self):
        res = self.factor()
        while self.current_token.type in (MUL,DIV):
            if self.current_token.type == MUL :
                self.eat(MUL)
                res*=self.bracket()
            elif self.current_token.type == DIV :
                self.eat(DIV)
                res/=self.bracket()
        return res

    def bracket(self):
        res = 0;
        if self.current_token.type == LEFTBRACKET:
            self.eat(LEFTBRACKET)
            res = self.term()
            while self.current_token.type != RIGHTBRACKET and self.current_token.type in (PLUS,MINUS):
                if self.current_token.type == PLUS:
                    self.eat(PLUS)
                    res += self.term()
                elif self.current_token.type == MINUS:
                    self.eat(MINUS)
                    res -= self.term()
            self.eat(RIGHTBRACKET)
        else:
            res = self.term()

        return res


    def expr(self):
        result = self.bracket();
        print("pos = ",self.lexer.pos)
        print("char = ",self.lexer.text[self.lexer.pos])
        print("current_token",self.current_token)
        print("1: ",result)
        while self.current_token.type in (PLUS,MINUS,MUL,DIV):
            if self.current_token.type == PLUS:
                self.eat(PLUS)
                result += self.bracket()
            elif self.current_token.type == MINUS:
                self.eat(MINUS)
                result -= self.bracket()
            elif self.current_token.type == MUL:
                self.eat(MUL)
                result *= self.bracket()
            elif self.current_token.type == DIV:
                self.eat(DIV)
                result /= self.bracket()

        return result

def main():
    while True:
        try:
            text = input("cal> ")
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()


