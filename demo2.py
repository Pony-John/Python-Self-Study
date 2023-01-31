## 转义字符

# \n表示newline，换行
print("Hello\nWorld")

# \t表示tab，缩进到下一个4个字（即8个字节）位置的制表位
print("\tend")
print("1\tend")
print("12\tend")
print("123\tend")
print("1234\tend")
print("12345\tend")
print("123456\tend")
print("1234567\tend")
print("12345678\tend")
print("123456789\tend")
print("1234567890\tend")
print("12345678901\tend")
print("123456789012\tend")
print("1234567890123\tend")
print("12345678901234\tend")
print("123456789012345\tend")
print("1234567890123456\tend")
print("12345678901234567\tend")
print("123456789012345678\tend")
print("1234567890123456789\tend")
print("12345678901234567890\tend")

print("\t结束")
print("一\t结束")
print("一二\t结束")
print("一二三\t结束")
print("一二三四\t结束")
print("一二三四五\t结束")
print("一二三四五六\t结束")
print("一二三四五六七\t结束")
print("一二三四五六七八\t结束")
print("一二三四五六七八九\t结束")
print("一二三四五六七八九十\t结束")
print("一二三四五六七八九十〇\t结束")

# \r表示return，回车至行首
print("Hello\rWorld") #此时输出只有World，这是因为Hello被\r覆盖掉了

# \b表示backspace，删除前一个字符
print("Hello\bWorld") #此时输出只有HellWorld，这是因为o被\b删除了

# 使用\对其后的一个字符进行转义，使得该字符不会被识别为Python的语法
print("我的文档的路径是D:\\Documents") #此时输出D:\Documents
print("老师说:\"一寸光阴一寸金。\"") #如果不对"符号转义，就会报错
print("老师说：“一寸光阴一寸金。”") #使用中文标点不需要转义

# 如果不希望转义字符起作用，而是希望其与其他字符一样，被原样打印，则可以在字符串前加上r或者R
# 注意：使用此功能时，字符串的最后一个字符不能是反斜线\，但可以最后两个是反斜线\\。
print(r"在Python中，\n可以用来换行。")
print(R"\t是常用的制表位缩进方法。")