# Lets Build A Simple Intercepter #

参照 [Let's Build A Simple Intercepter](https://ruslanspivak.com/lsbasi-part1/) 实现的解释器 

Interperter_1.py: 一位数加法器  
作业：
- [x] 多位数运算
- [x] 跳过空格
- [x] 减法

Interpreter_2.py: 多位数加减法运算器  
作业： 
- [x] 乘法
- [x] 除法
- [x] 连加连减连乘连除

Interpreter_4.py: 重构后的乘除法运算器  
作业：  
- [x] 使其支持加减乘除四则混合运算  
使用栈来保存'+'、'-'运算符和相应参与运算的数字,直接计算出'*'、'/'运算符的结果  
TODO:  应该是先进先出的形式，在做减法的时候，栈会引起减数 - 被减数

Interpreter_5.py: 支持加减乘除四则混合运算的运算器，使用factor来处理高优先级计算
- [x] 实现括号  
新增了一个"bracket"语法，expr每次调用bracket完成括号的处理


- 学完整个项目
- 改写为对C语言的解释器

