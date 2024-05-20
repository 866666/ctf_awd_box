# 输入字符串
string1 = "frjeigoherigeriogherioggg"
string2 = "\x00\x1e\x0b\x02\x12\x14\t\x0e\x0c\x01\r\x00\x01\x1a\x0c\x1d\x00\x00\x00\x00\x19\x00\x15\x02\x1a"

# 将字符串转换为字节
byte1 = string1.encode()
byte2 = string2.encode()

# 异或操作
xor_result = bytes(x ^ y for x, y in zip(byte1, byte2))

# 输出异或结果
print(xor_result)
