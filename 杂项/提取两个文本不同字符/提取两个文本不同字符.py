with open("python\\提取两个文本不同字符\\1.txt", "r") as file1, open(
    "python\\提取两个文本不同字符\\2.txt", "r"
) as file2:
    # 读取文件内容为字符串
    content1 = file1.read()
    content2 = file2.read()

    # 逐字符比较
    char = ""
    for char1, char2 in zip(content1, content2):
        if char1 != char2:
            char += char1 + char2
            print(char)

    # 检查其中一个文件是否有多余的字符
    for char in content1[content1 != content2]:
        print(char)
    for char in content2[content1 != content2]:
        print(char)
