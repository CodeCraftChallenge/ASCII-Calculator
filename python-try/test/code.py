from os import name


if name == 'nt':
    print("当前操作系统为windows")                  # 获得输入文本并手动添加windows环境下的换行符 \r\n
    txt = input() + '\r\n'            
elif name == 'posix':
    print("当前操作系统为:Unix/Linux/MacOS")        # 获得输入文本并手动添加Unix/Linux/MacOS系统环境下的换行符 \n
    txt = input() + '\n'              
else:
    print("当前操作系统为:未知系统系统,使用类Unix风格换行符")        # 获得输入文本并手动添加类UnixS系统环境下的换行符 \n

    txt = input() + '\n'              
print("输入字符串为:", txt)

sum = 0                                           # 统计ASCII字符值之和
for character in txt:
    sum += ord(character)
print("ASCII之和为:", sum)
