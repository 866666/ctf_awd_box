import cv2
import numpy as np


def extract_rgb_pixels_to_txt(image_path, output_path):
    # 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # 检查图像是否成功读取
    if img is None:
        print("无法读取图像，请检查路径")
        return

    # 获取图像的形状
    height, width, _ = img.shape

    # 打开或创建输出文件
    with open(output_path, "w") as f:
        for i in range(height):
            for j in range(width):
                # 提取像素值
                r, g, b = img[i, j]
                # 将RGB值以空格分隔写入文件
                f.write(f"{b} {g} {r}\n")


# 使用函数
image_file = "chall.png"  # 替换为你的图像路径
output_file = "pixels.txt"  # 输出的TXT文件名
extract_rgb_pixels_to_txt(image_file, output_file)
