import os
from tkinter import filedialog


class CFileClass:
    def __init__(self, file_path):
        self._file_path = file_path
        self._function_list = []
        self._function_dict = {}
        self._global_variable_list = []
        self._macro_define_list = []
        self._include_file_list = []

    def parse_file(self):
        # 解析文件逻辑
        # 这里只是示例，需要根据实际需求实现具体的解析逻辑
        with open(self._file_path, "r") as file:
            for line in file:
                # 解析函数
                if line.startswith("function"):
                    function_name = line.split()[1]
                    self._function_list.append(function_name)
                    self._function_dict[function_name] = line.strip()

                # 解析全局变量
                if line.startswith("global_variable"):
                    variable_name = line.split()[1]
                    self._global_variable_list.append(variable_name)

                # 解析宏定义
                if line.startswith("#define"):
                    macro_name = line.split()[1]
                    self._macro_define_list.append(macro_name)

                # 解析包含文件
                if line.startswith("#include"):
                    include_file = line.split()[1]
                    self._include_file_list.append(include_file)

    def get_function_list(self):
        return self._function_list

    def get_function_dict(self):
        return self._function_dict

    def get_global_variable_list(self):
        return self._global_variable_list

    def get_macro_define_list(self):
        return self._macro_define_list

    def get_include_file_list(self):
        return self._include_file_list


# step 1: select folder
def select_folder():
    folder_path = filedialog.askdirectory()
    print("select folder: %s" % folder_path)
    return folder_path

# step 2: find all c file
def find_all_c_file(folder_path):
    cfile_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".c"):
                cfile_list.append(file)

    if len(cfile_list) == 0:
        print("no c file found!")
    else:
        print(cfile_list)
    return cfile_list

# step 3: list all functions
def list_all_functions(cfile_list):
    func_list = []
    return func_list

# step 4: list function call relation
def list_func_relation(c_file_object_list):
    pass


if __name__ == "__main__":
    folder_path = select_folder()
    cfile_list = find_all_c_file(folder_path)
    func_list = list_all_functions(cfile_list)
    list_func_relation(func_list)