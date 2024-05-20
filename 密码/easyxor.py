# output.txt:
# 9b919c9a8685cd8fa294c8a28c88cc89cea2ce9c878480

# 分析脚本：
# urandom(1)就是随机生成一个字符串 赋值给key

# 密文是xor(flag,key)生成的。xor函数就是遍历flag将每一位异或key 最后返回最终的结果

# 密文是16进制。

# 思路：
# 这里的思路就是把key搞出来那就好做了，我们已知flag前缀为flag{，那么可以把前缀与密文的16进制进行异或，得到key


key = 253
cipher = "9b919c9a8685cd8fa294c8a28c88cc89cea2ce9c878480"
flag = ""
for i in range(0, len(cipher), 2):
    flag += chr(int(cipher[i : i + 2], 16) ^ key)
print(flag)
