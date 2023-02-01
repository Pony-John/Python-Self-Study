## Python中的保留字和标识符

# 保留字：有一些单词被赋予了特定的含义，这些单词在给任何对象取名时都不能使用。
# 以下两行代码导入并打印了Python的保留字
import keyword
print(keyword.kwlist)
# 输出结果为['False', 'None', 'True', 'and', 'as', 'assert', 'async',
#  'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
#  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
# 'raise', 'return', 'try', 'while', 'with', 'yield']

# 标识符：变量、函数、类、模块和其他对象起的名字就叫做标识符。
# 标识符的语法规范为：允许使用字母、数字、下划线；不能以数字开头；区分大小写。

