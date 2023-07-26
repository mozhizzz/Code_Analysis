class CVar:
    def __init__(self):
        self.type = ''
        self.name = ''
        self.value = 0
        self.is_global = False

    def get_type(self):
        return self.type
    
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value
    
    def get_is_global(self):
        return self.is_global
