class CFunc:
    def __init__(self):
        self.func_type = ''
        self.name = ''
        self.func_params_list = []
        self.var_list = []
        self.g_var_list = []
        self.call_func_list = []
        self.return_value = 0

    def get_func_type(self):
        return self.func_type
    
    def get_name(self):
        return self.name
    
    def get_func_params_list(self):
        return self.func_params_list
    
    def get_var_list(self):
        return self.var_list
    
    def get_g_var_list(self):
        return self.g_var_list
    
    def get_call_func_list(self):
        return self.call_func_list
    
    def get_return_value(self):
        return self.return_value
