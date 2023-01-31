##打印函数print

#1、打印数字
print(520)

#2、打印字符串，需要加双引号
print("压力马斯内")

#3、打印一个运算的结果
print(114*1000+514)

#4、将打印结果输出到文件
fp=open('D:/Documents/Python/test1/text.txt','a+')
#fp=表示：定义变量
#a+表示：若有该text.tx文件则续写该文件，若无该text.tx文件则创建该文件并写入
print("Hello World",file=fp) #将Hello World打印到上述文件
fp.close() #关闭文件(即变量fp)