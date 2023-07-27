class CFile:
    def __init__(self, file_path):
        self.include_list = []
        self.var_list = []
        self.func_list = []

    def get_func_list(self):
        return self.func_list

    def get_var_list(self):
        return self.var_list

    def get_include_list(self):
        return self.include_list    

    def generate_cfunc_list(self):
        pass

    def generate_cvar_list(self):
        pass
