class Project:
    def __init__(self, file_path, project_type):
        self.abs_path = file_path
        self.project_type = project_type
        self.cfile_list = []
        self.hfile_list = []

    def get_project_type(self):
        return self.project_type

    def get_abs_path(self):
        return self.abs_path

    def get_cfile_list(self):
        return self.cfile_list

    def get_hfile_list(self):
        return self.hfile_list
