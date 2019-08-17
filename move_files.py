import os

class MoveFiles:

    def __init__(self,start_directory, end_directory):
        self.start_directory = start_directory
        self.end_directory = end_directory

    def move_files_by_names(self, list_of_names):
        self.names = list_of_names
        if len(self.names) > 0:
            for name in self.names:
                for filename in os.listdir(self.start_directory):
                    if filename.startswith(name):
                        os.rename(self.start_directory + "/"+ filename, self.end_directory + "/" + filename)
        else:
            print("Missing names, hence can not move files by names.")
    
    def move_files_by_filetypes(self, list_of_filetypes):
        self.filetypes = list_of_filetypes

        if len(self.filetypes) > 0:
            for filetype in self.filetypes:
                for filename in os.listdir(self.start_directory):
                    if filename.endswith(filetype):
                        filetype_directory = filetype
                        os.rename(self.start_directory + "/"+ filename, self.start_directory + "/" + str.replace(filetype,".","") + "/" + filename)
        else:
            print("missing filetypes")


def get_user_input():
    
    list_of_user_input = []
    
    type_of_sort = int(input('Do you want to sort by name or file extension? For name enter 1, enter 2 for extension '))
    if type_of_sort == 1:
        print("Blabla")

    if type_of_sort == 2:
        try:
            taking_inputs = True

            while taking_inputs is True:
                file_extension_input = str(input("Please type in the file extensions you want to move: "))

                if file_extension_input.startswith("."):
                    list_of_user_input.append(file_extension_input)
                    continue

                if file_extension_input.lower() == 'done':
                    taking_inputs = False
                    
                else:
                    print("Please start file extensions with .")

        except ValueError:
            print(ValueError)

        

    else:
        print("Please enter either 1 or 2")
        get_user_input()

    return list_of_user_input


start_directory = "project_1/"
end_directory = "project_1/project_1_text"

movefiles = MoveFiles(start_directory, end_directory)


movefiles.move_files_by_filetypes(get_user_input())





