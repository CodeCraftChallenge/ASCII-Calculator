from os import name

if name == 'nt':
    print("当前操作系统为windows")
    txt = input() + '\r\n'  # 获得输入文本并手动添加windows环境下的换行符 \r\n
elif name == 'posix':
    print("当前操作系统为:Unix/Linux/MacOS")
    txt = input() + '\n'  # 获得输入文本并手动添加Unix/Linux/MacOS系统环境下的换行符 \n
else:
    print("当前操作系统为:未知系统系统,使用类Unix风格换行符")
    txt = input() + '\n'  # 获得输入文本并手动添加类UnixS系统环境下的换行符 \n

print("输入字符为:", txt)
sum = 0                     # 统计ASCII字符值之和

for character in txt:
    sum += ord(character)
print("ASCII之和为:", sum)
