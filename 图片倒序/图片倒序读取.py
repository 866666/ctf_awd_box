f = open("123.png", "rb").read()
f1 = open("out.png", "wb")
f1.write(f[::-1])
