#读取图片文件并倒序输出保存为新文件
f = open("123.png", "rb").read()
f1 = open("out.png", "wb")
f1.write(f[::-1])
