class HFile:
    def __init__(self, file_path):
        self.abs_path = file_path
        self.include_list = []
        self.extern_var_list = []
        self.extern_func_list = []

    def get_abs_path(self):
        return self.abs_path
    
    def get_include_list(self):
        return self.include_list
    
    def get_extern_var_list(self):
        return self.extern_var_list
    
    def get_extern_func_list(self):
        return self.extern_func_list
