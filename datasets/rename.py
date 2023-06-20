import os

# 设置要重命名的路径
path = "../inference/nest"

n = 1
file_list = os.listdir(path)
# old_filepath_list = []
# 遍历该路径的所有文件和目录
for filename in file_list:
        # 构建新的文件名（这里以 "new_" 为前缀）
        new_filename = "nest_" + str(n) + ".jpg"

        # 构建完整的文件路径（注意：使用 os.path.join 可以跨平台构建路径）
        old_filepath = os.path.join(path, filename)
        new_filepath = os.path.join(path, new_filename)

        # 输出信息
        print(f"{old_filepath} => {new_filepath}")

        # 执行文件重命名
        os.rename(old_filepath, new_filepath)
        # old_filepath_list.append(old_filepath)
        n = n + 1

# for remove_list in old_filepath_list:
#     os.remove(remove_list)
