
#* 判断大小写
s = 'Hello, World'
print(s.isupper())
print(s.islower())

#* replace
s = "I like cats"
print(s.replace("cats", "dogs"))
# I like dogs

#* 去掉空格
s = "  hello  "
print(s.strip())   # "hello"
print(s.lstrip())  # "hello  "
print(s.rstrip())  # "  hello"

#* 转换大小写
s = 'Hello, World'
print(s.lower())
print(s.upper())
print(s.swapcase())

#* 统计字符数量
s = 'Hello, World'
print(s.count('l'))

#* 是否是数字
s = 'limaohui2296'
print(s.isdigit())

#* 分割字符串
s = 'Hello, World'
print(s.split(' '))

#* 是否包含某个字符串
s = 'Hello, World'
print('True') if 'hello' in s else print('False')

def contains_ignore_case(substring, text):
    if substring.lower() in text.lower():
        print("True")
    else:
        print("False")

contains_ignore_case("hello", "Hello, World")

