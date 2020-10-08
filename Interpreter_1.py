INTEGER,PLUS,MINUS,EOF = 'INTEGER','PLUS','MINUS','EOF'

class Token(object):
    # 初始化，获取token
    def __init__(self,type,value):
        self.type = type
        self.value = value
    # 输出对象内容
    def __str__(self):
        return 'Token({type},{value})'.format(type=self.type,value=repr(self.value))

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self,text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    # 得到下一个词语
    def get_next_token(self):
        text = self.text

        # 如果当前已经超过最后一位
        if self.pos > len(text) - 1:
            return Token(EOF,None)

        # 获取当前字符
        current_char = text[self.pos]
        while current_char==' ':
            print("in space: pos=",self.pos," current char=",current_char )
            self.pos += 1
            if self.pos < len(text):
                current_char = text[self.pos]
            else:
                current_char = None
        if current_char == '+':
            token = Token(PLUS,current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS,current_char)
            self.pos += 1
            return token

        if current_char.isdigit():
            print("in digit: pos=",self.pos," current char=",current_char )

            num = 0
            while current_char is not None and current_char.isdigit():
                num = num*10 + int(current_char)
                self.pos += 1
                if self.pos>=len(self.text):
                    current_char = None
                else:
                    current_char = self.text[self.pos]
            token = Token(INTEGER,num)
            return token
        # 既不是数字也不是加号，报错
        self.error()

    def eat(self, token_type):
        # 如果当前字符类型和传入字符类型相同，吃掉！
        # 主要用于判断连续字符类型，比如数字，空格
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        if op.type == MINUS:
            self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)

        last = self.current_token

        if op.type == PLUS:
            result = left.value + right.value
        if op.type == MINUS:
            result = left.value - right.value
        print("left: ",left)
        print("op: ",op)
        print("right: ",right)
        print("last: ",last)
        return result

def main():
    while True:
        try:
            text = input('calc>')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)
        print('---------------------')
if __name__ == '__main__':
    main()