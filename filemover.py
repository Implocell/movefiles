import os
import shutil

def move_files(type_of_sort, file_extension_input, search_base, target_base):
    moved_files = []
    for root, dirs, files in os.walk(search_base):
        for file in files:
            if file.endswith(file_extension_input):
                try:
                    if type_of_sort == 1:
                        shutil.copy(root + "/"+ file, target_base + "/" + root.split(os.sep)[-1] + file)
                    if type_of_sort == 2:
                        shutil.copy(root + "/"+ file, target_base + "/" + file)
                except:
                    print(f'Something failed with file {file}')
                    pass
            
            moved_files.append(file)


    print (f'Files have been copied from {search_base} to {target_base}, this is a list of the files: \n')
    #print([f for f in moved_files])

def get_user_input():
    
    search_base = input('Type where to search from e.g. a drive: ')
    target_base = input('Type where to place files, path to a folder: ')
    type_of_sort = int(input('Rename file to parent folder: 1\
        Keep file name: 2 '))

    if type_of_sort == 1 or type_of_sort == 2:

        try:
            file_extension_input = str(input("Please type in the file extensions you want to move(e.g. .xlsx): "))

            if file_extension_input.startswith("."):
                print("Hang on, moving files.")
                
            else:
                print("Please start file extensions with .")

        except ValueError:
            print(ValueError)
        
    else:
        print("Please enter either 1 or 2")
        get_user_input()

    return move_files(type_of_sort, file_extension_input, search_base, target_base)


if __name__ == "__main__":
    get_user_input()