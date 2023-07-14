import os

from tkinter import filedialog

class CfileClass():
    def __init__(self, file_path):
        self._file_path = file_path
        self._function_list = []
        self._function_dict = {}
        self._global_variable_list = []
        self._macro_define_list = []
        self._include_file_list = []

    def parse_file(self):
        pass


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