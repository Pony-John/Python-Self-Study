## 数据类型
# 一、常见的数据类型

# 1、整型：int，如114514
# 可以表示正数、负数和零。
# 默认是十进制，0b开头是二进制，0o开头是八进制，0x开头是十六进制
n1 = 90
n2 = -76
n3 = 0
n4 = 0b10010001
n5 = 0o176
n6 = 0x1A2F
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
print(n4,type(n4))
print(n5,type(n5))
print(n6,type(n6))

# 2、浮点型：float，如3.1415926
# 浮点数由整数部分、小数点、小数部分组成
f1 = 1.1
f2 = 2.2
print(f1+f2)# 此处输出为3.3000000000000003，这是浮点数存储时的误差导致的

# 可以通过引入Decimal库的方式消除误差
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

# 3、布尔型：bool，只有True与False
# True表示1，False表示0，并可以参与整型运算
b1 = True
b2 = False
print(b1,type(b1))
print(b2,type(b2))
print(b1+1,b2+1)

# 4、字符串：str，如"人生苦短，我用Python"
# 字符串又称为不可变的字符序列
# 可以使用单引号'string'、双引号"string"、三个单引号'''string'''或三个双引号""""string"""来定义
str1 = '人生苦短，我用Python'
str2 = "人生苦短，我用Python"
str3 = '''人生苦短，
我用Python'''
str4 = """人生苦短，
我用Python""" #三个引号时，输入的字符串允许分布在连续的多行
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))


# 二、数据类型的转换

# 1、str()函数：将其他类型的数据转化成字符串型
name = '张三'
age = 20
# print('我叫'+name+'今年'+age+'岁')会报错，原因是字符串型与整型不同，不能使用连接符+
print('我叫'+name+',今年'+str(age)+'岁')
#note：str(123)也等效于'123'，但str(age)不等效于'age'，后者会直接输出单词

# 2、int()函数：将其他类型的数据转化成整型。
# 注：文字类、小数类字符串无法转化；浮点数转化时，抹零取整。
IntTest1 = '128' 
IntTest2 = '76.77' #这个无法转化
IntTest3 = 'Hello' #这个无法转化
IntTest4 = 98.7
IntTest5 = True
print(type(IntTest1),type(IntTest2),type(IntTest3),type(IntTest4),type(IntTest5))
print(int(IntTest1),type(int(IntTest1)))
#print(int(IntTest2))
#print(int(IntTest3))
print(int(IntTest4),type(int(IntTest4)))
print(int(IntTest5),type(int(IntTest5)))

# 3、float()函数：将其他类型的数据转化成浮点型
# 注：文字类字符串无法转化；整型转化时，末尾加.0
FloatTest1 = '128.98'
FloatTest2 = '76'
FloatTest3 = 23
FloatTest4 = 'Hello' #这个无法转化
FloatTest5 = False
print(type(FloatTest1),type(FloatTest2),type(FloatTest3),type(FloatTest4),type(FloatTest5))
print(float(FloatTest1),type(float(FloatTest1)))
print(float(FloatTest2),type(float(FloatTest2)))
print(float(FloatTest3),type(float(FloatTest3)))
#print(float(FloatTest4),type(float(FloatTest4)))
print(float(FloatTest5),type(float(FloatTest5)))