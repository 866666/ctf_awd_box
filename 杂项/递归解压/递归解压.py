import pyzipper
import os


def unzip_with_pyzipper(file_path):
    try:
        # password为file_path文件名的第一位字符+第三位字符
        password = file_path[0] + file_path[2]
        with pyzipper.AESZipFile(
            file_path,
            "r",
            compression=pyzipper.ZIP_DEFLATED,
            encryption=pyzipper.WZ_AES,
        ) as zf:
            zf.setpassword(password.encode("utf-8"))
            zf.extractall(path=".", pwd=password.encode("utf-8"))
            print(f"Successfully unzipped {file_path}")
            # 获取被解压的文件名
            file_name = zf.namelist()[0]
        # 如果file_name是txt文件
        if file_name.endswith(".txt"):
            # 以utf-8编码输出file_name文件内容到控制台
            with open(file_name, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"Unzipped file name: {file_name}")
            # 删除file_path文件
            zf.close
            os.remove(file_path)
        print(f"Unzipped file name: {file_name}")
        # 递归调用
        unzip_with_pyzipper(file_name)
    except pyzipper.BadZipFile:
        print(f"Failed to unzip {file_path} - incorrect password or corrupted ZIP file")
    except Exception as e:
        print(f"An error occurred while unzipping {file_path}: {e}")


# zip_file_path为要解压的zip文件路径
zip_file_path = "5101.zip"

unzip_with_pyzipper(zip_file_path)
