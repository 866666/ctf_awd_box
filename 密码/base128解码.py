import base128

str = "flag{74b42645-8414-4995-9e99-6e483caed2a9}"
b128 = base128.base128(chars=None, chunksize=7)
m = list(b128.encode(str.encode(encoding="utf-8")))
# m= [b'3\x1b\x0c\x16;ln4', b'1\r\x06#1Pj-', b'\x1c\r\x06\x13!4h9', b'\x1cM%SK\x14r9', b'\x16MLS!`fc', b'0Y,C\x13\x04r}', [0]]  # 编码
c = b"".join(b128.decode(m)).decode()  # 解码
print(m)  # 输出编码后的结果
print(c)  # 输出解码后的结果
